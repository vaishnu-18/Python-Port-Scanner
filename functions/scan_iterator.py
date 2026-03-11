from typing import List, Tuple
from .socket_connection import socket_connection
import time
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
from threading import Lock
import logging

# A rate limiter object will be shared between all threads
# It keeps a timer and only allows a certain amount of threads to run per second
class RateLimiter:
    """
    Shared thread-safe rate limiter.

    rate = number of scan attempts allowed per second globally.
    Example:
        rate = 5.0  -> about 1 scan every 0.2 seconds total
        rate = 10.0 -> about 1 scan every 0.1 seconds total
    """

    def __init__(self, rate: float) -> None:

        # Prevent invalid configuration (cannot have zero or negative rate)
        if rate <= 0:
            raise ValueError("rate must be greater than 0")

        # Time interval required between two scan attempts
        # Example: rate = 5 -> interval = 0.2 seconds
        self.interval = 1.0 / rate

        # Lock ensures that only one thread updates the limiter at a time
        # Without this, multiple threads could start scans simultaneously
        self.lock = Lock()

        # The earliest time when the next scan attempt is allowed
        # Using monotonic time avoids issues if the system clock changes
        self.next_allowed_time = time.monotonic()

    # The wait function will be called by each thread
    # This will force them to sleep for a certain amount of time before executing,
    # To ensure rate limiting
    def wait(self) -> None:

        # Only one thread can execute this block at a time
        # This guarantees correct global rate limiting
        with self.lock:

            # Get the current monotonic time
            now = time.monotonic()

            # If we are too early, wait until the next allowed scan time
            if now < self.next_allowed_time:
                time.sleep(self.next_allowed_time - now)

            # Schedule the next allowed scan time
            # max() ensures that if the system is already behind schedule,
            # we don't accumulate unnecessary delays
            self.next_allowed_time = max(
                self.next_allowed_time + self.interval,
                time.monotonic()
            )

def scan_port(ip: str, port: int, limiter: RateLimiter) -> bool:
    """
        Tries to connect to an ip address:port

        A rate limiter prevents it from running 
        more than a specified amount of times per second

        Output:
        True if the port is open, False otherwise
    """
    limiter.wait()
    return socket_connection(ip, port)

def scan_iterator(ip_address: str, ports: List[int], max_threads: int, max_connections_per_sec: int) -> List[tuple[int,bool]]:
    """
        Loops through a list of ports and attempts to connect to each of them on the
        specified IP address

        Inputs:
            An IP address
            A list of ports to check
            The maximum threads that can be ran simultaneously
            The maximum connections allowed per second

        Output:
            A list of tuples composed of:
                A port
                Whether the port is open or not (true/false)
    """
    # Check if at least one port was provided
    if not ports:
        return []

    # Create the scan result output list (empty at first)
    output_port_list: List[tuple[int,bool]] = []

    logging.info(f"starting port scan on address {ip_address} and range {ports[0]} - {ports[-1]} "
                 f"with max threads: {max_threads}, and max connections/sec: {max_connections_per_sec}")
    start_time = time.time()
    rate_limiter = RateLimiter(max_connections_per_sec)

    # Use multiple worker threads for concurrent port scans
    # executor.map preserves the order of ports initially provided
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        output_port_list = list(executor.map(scan_port, repeat(ip_address), ports, repeat(rate_limiter)))
   
    elapsed_time = time.time() - start_time
    logging.info(f"port scan finished in {elapsed_time:.5} seconds!")

    return output_port_list


# Testing
#result = scan_iterator("192.168.56.101",[0,22,23,60],100,10)
#print(result)