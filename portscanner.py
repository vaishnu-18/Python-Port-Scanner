from typing import List, Tuple
from functions import port_scanner, socket_connection,store_to_file,take_input,validate_input,write_to_console

#file: portscanner.py
def portscanner():

    scan_input: tuple[str,List[int]] = take_input()

    validate_input(scan_input)

    scan_result: tuple[int,bool] = port_scanner(scan_input)

    ip_address = scan_input[0]

    store_to_file(ip_address, scan_result)

    write_to_console(ip_address, scan_result)

