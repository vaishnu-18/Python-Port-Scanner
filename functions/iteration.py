from typing import List, Tuple
from .socket_connection import socket_connection
import time
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def iteration(ip_address: str, ports: List[int]) -> List[tuple[int,bool]]:
    """
        Loops through a list of ports and attempts to connect to each of them on the
        specified IP address

        Inputs:
            A tuple composed of:
                An IP address (str)
                A list of ports to check (List[int])

        Output:
            A list of tuples composed of:
                A port (int)
                Whether the port is open or not (bool)
    """

    #Create the scan result output list (empty at first)
    output_port_list: List[tuple[int,bool]] = []

    logging.info(f"starting port scan on address {ip_address} and range {ports[0]} - {ports[-1]}")

    start_time = time.time()

    # max_workers=100: one thread per host — optimal for 100 small IO tasks
    with ThreadPoolExecutor(max_workers=100) as executor:
        output_port_list = list(executor.map(socket_connection, repeat(ip_address), ports))
    # executor.map preserves ORDER — results match the order of hostnames

    elapsed_time = time.time() - start_time

    logging.info(f"port scan finished in {elapsed_time:.5} seconds!")

    return output_port_list


# Testing

#result = iteration("192.168.56.101",[0,22,23,60])
#print(result)