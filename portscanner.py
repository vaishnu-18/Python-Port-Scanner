from typing import List, Tuple
from functions.take_input import take_input
from functions.scan_iterator import scan_iterator
from functions.write_to_console import write_to_console
from functions.store_to_file import store_to_file
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def portscanner():

    #Asks the user to enter ip address and a single port or range of ports
    #Validates the result and stores it
    ip_address, ports = take_input()

    #Configure Threads and Rate Limiting
    max_threads = 100
    max_connections_per_sec = 10.0

    #For each port given, tries to establishes a connection to the ip address given
    #Stores the status of each port; true = OPEN, false = CLOSED
    scan_result: tuple[int,bool] = scan_iterator(ip_address, ports, max_threads, max_connections_per_sec)

    #Writes the scan results to the console
    write_to_console(ip_address, scan_result)

    #Writes the scan results to a .json file
    store_to_file(ip_address, scan_result)

# Testing
portscanner()

