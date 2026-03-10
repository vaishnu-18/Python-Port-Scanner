from typing import List, Tuple
from functions import iteration, socket_connection,store_to_file,take_input,validate_input,write_to_console

#file: portscanner.py
def portscanner():

    scan_input: tuple[str,str] = take_input()

    validated_input: tuple[str,List[int]] = validate_input(scan_input)

    scan_result: tuple[int,bool] = iteration(validated_input)

    ip_address = validated_input[0]

    store_to_file(ip_address, scan_result)

    write_to_console(ip_address, scan_result)

