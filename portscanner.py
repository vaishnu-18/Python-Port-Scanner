from typing import List
from functions.take_input import take_input
from functions.scan_iterator import scan_iterator
from functions.write_to_console import write_to_console
from functions.store_to_file import store_to_file
from functions.validate_input import validate_ip, validate_port, validate_port_range
import logging
import argparse

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
# main -->  argparse belongs to the interface layer, not inside the logic modules

def portscanner(ip_address: str, ports: List[int]): #Focus does the scanning

    #Configure Threads and Rate Limiting
    max_threads = 100
    max_connections_per_sec = 10.0

    scan_result: List[tuple[int,bool]] = scan_iterator(ip_address, ports, max_threads, max_connections_per_sec)

    #Writes the scan results to the console
    write_to_console(ip_address, scan_result)

    #Writes the scan results to a .json file
    store_to_file(ip_address, scan_result)

def main(): #prepares input (CLI, input, validation)

    #Instanciate argparse
    parser = argparse.ArgumentParser(description="Python Port Scanner")

    #This is our arguments
    parser.add_argument(
        "-t", "--target",
        type= str,
        help="Target IP address (example: 192.168.1.10)"
    )

    parser.add_argument(
        "-p", "--ports",
        type= str,
        help="Port or range of ports (example: 80 or 20-100)"
    )

    #Reads the command line arguments
    args = parser.parse_args()

    # If CLI args not provided → interactive mode
    if not args.target or not args.ports:
        ip_address, ports = take_input()
    else:
        try:
            ip_address = validate_ip(args.target)

            if args.ports.count("-") == 1 and not args.ports.startswith("-"):
                ports = validate_port_range(args.ports)
            else:
                ports = validate_port(args.ports)
        
        except ValueError as e:
            print(f"INPUT ERROR : {e}")
            exit(1)
    
    portscanner(ip_address, ports)

if __name__ == "__main__":
    main()