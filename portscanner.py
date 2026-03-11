from typing import List, Tuple
from functions.take_input import *
from functions.validate_input import *
from functions.iteration import *
from functions.write_to_console import *
from functions.store_to_file import *

def portscanner():

    ip_address, ports = take_input()

    scan_result: tuple[int,bool] = iteration(ip_address, ports)

    write_to_console(ip_address, scan_result)

    store_to_file(ip_address, scan_result)

portscanner()

