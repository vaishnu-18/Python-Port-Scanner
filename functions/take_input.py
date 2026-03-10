from typing import List, Tuple

def take_input() -> tuple[str,str]:
    #Ask the user to enter an ip address
    #Store it in a variable (Str)
    ip_address = input("Enter the IP address: ")
    #Ask the user to enter a list of ports
    #Store it in a variable (Str)
    ports = input("Enter the port range: ")
    #Return the result
    return ip_address, ports