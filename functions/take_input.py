from typing import List, Tuple
from .validate_input import validate_ip, validate_port

#Ask the user to enter an ip address
def get_ip() -> str:
    """
    Prompt the user to enter an IP address and validate it.
    Keeps asking until a valid IP address is provided.

    Returns:
        str: A valid IP address.
    """

    ip = input("Enter an IP address : ")
    while True:
        try:
            validate_ip(ip)
            return ip
        except ValueError as e:
            ip = input(f"{e} Please Enter a valid IP address : ")

def get_port() -> List[int]:
    """
    Ask the user whether to scan a single port or a range of ports.
    For a single port, validate and return as a list with one integer.
    For a range, validate both ends and return as a list of all ports in the range.

    Returns:
        List[int]: List of ports to scan.
    """
    choice = input("Do you want to scan a single port or a range ? (Enter 'single' or 'range') : ").strip().lower()
    
    while choice not in ("single", "range"):
        choice = input("Invalid choice. Please enter 'single' or 'range' : ").strip().lower()
    
    if choice == "single":
        single_port = input("Enter a port number : ").strip()
        while True:
            try:
                single_port_int = validate_port(single_port)
                return single_port_int
            except ValueError as e:
                single_port = input(f"{e} Please enter a valid port : ")

    elif choice == "range":
        start_port = input("Enter the first port : ").strip()
        end_port = input("Enter the last port : ").strip()
        range_port = f"{start_port}-{end_port}"

        while True:
            try:
                range_port_int = validate_port(range_port)
                return range_port_int
            except ValueError as e:
                start_port = input(f"{e} Please enter a valid starting port : ")
                end_port = input(f"{e} Please enter a valid ending port : ")
                range_port = f"{start_port}-{end_port}"

def take_input() -> Tuple[str, List[int]]:
    """
    Collect IP address and port(s) inputs from the user.

    Returns:
        Tuple[str, List[int]]: The IP address and list of ports.
    """
    ip = get_ip()
    port = get_port()
    return ip, port