from typing import List
from functions.take_input import take_input
from functions.scan_iterator import scan_iterator
from functions.write_to_console import write_to_console
from functions.store_to_file import store_to_file
from functions.validate_input import validate_ip, validate_port, validate_port_range, validate_filename
import logging
import argparse

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def portscanner(ip_address: str, ports: List[int], max_threads: int, max_connections_per_sec: float, output_file: str):

    scan_result: List[tuple[int,bool]] = scan_iterator(ip_address, ports, max_threads, max_connections_per_sec)

    #Writes the scan results to the console
    write_to_console(ip_address, scan_result)

    #Writes the scan results to a .json file
    store_to_file(ip_address, scan_result, output_file)

def main():

    #Instanciate argparse
    parser = argparse.ArgumentParser(
        description="Python Port Scanner",
        epilog="Example: python3 portscanner.py -t 192.168.56.101 -p 20-100"
        )

    #These are our arguments
    parser.add_argument(
        "-t", "--target",
        type=str,
        help="Target IP address (example: 192.168.1.10)"
    )

    parser.add_argument(
        "-p", "--ports",
        type=str,
        help="Port or range of ports (example: 80 or 20-100)"
    )

    parser.add_argument(
        "-th", "--threads",
        type=int,
        default=100,
        help="Maximum number of threads (default = 100)"
    )

    parser.add_argument(
        "-r", "--rate",
        type=float,
        default=100.0,
        help="Maximum connections per seconds (default = 100.0)"
    )

    parser.add_argument(
        "-ti", "--timeout",
        type=float,
        default=1.0,
        help="Socket timeout in seconds (default: 1.0)"
    )

    parser.add_argument(
        "-o", "--output",
        default="scan_results.json",
        help="Output JSON file (default: scan_results.json)"
    )

    #Reads the command line arguments
    args = parser.parse_args()

    max_threads = args.threads
    max_connections_per_sec = args.rate
    
    # If CLI args not provided → interactive mode
    if not args.target or not args.ports:
        ip_address, ports = take_input()
    else:
        try:
            ip_address = validate_ip(args.target)

            try:
                ports = validate_port_range(args.ports)
            except ValueError:
                ports = validate_port(args.ports)

            output_file = validate_filename(args.output)

        except ValueError as e:
            print(f"{e}")
            exit(1)
    
    portscanner(ip_address, ports, max_threads, max_connections_per_sec, output_file)

if __name__ == "__main__":
    main()