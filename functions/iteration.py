from typing import List, Tuple
from socket_connection import socket_connection
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def iteration(scan_input: tuple[str,List[int]]) -> List[tuple[int,bool]]:
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
    
    #Gather the ip address
    ip_address: str = scan_input[0]

    #Gather the list of ports to scan
    input_port_list: List[int] = scan_input[1]

    #Create the scan result output list (empty at first)
    output_port_list: List[tuple[int,bool]] = []

    logging.info(f"starting port scan on address {ip_address} and range {input_port_list[0]} - {input_port_list[-1]}")

    #Loop through the list of ports
    for port in input_port_list:
        # Try to connect to the port on the specified ip address
        # Gather the result (true/false)
        is_open: bool = socket_connection(ip_address, port)

        #Store the scanned port and the result of the scan in a single variable
        port_status: tuple[int,bool] = (port,is_open)

        #Add the result to the output list
        output_port_list.append(port_status)

    logging.info(f"port scan finished!")

    return output_port_list


test = ("192.168.56.101",[0,22,23,60])
result = iteration(test)
print(result)