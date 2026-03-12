from typing import List
import re

def validate_port(input_port: str) -> List[int]:
    """
    Validate a port input string.

    Args:
        input_port (str): Port string (e.g., '80').

    Returns:
        List[int]: List of port number.

    Raises:
        ValueError: If the input is invalid.
    """

    input_port = input_port.strip()

    if input_port == "":
        raise ValueError("PORT ERROR : Port n° is empty !")

    try:
        port = int(input_port)
    except ValueError:
        if " " in input_port:
            raise ValueError("PORT ERROR : Port n° can't contain spaces between characters !")
        else:
            raise ValueError("PORT ERROR : Port n° must be a valid number between 0 and 65535 !")
        
    if port < 0:
        raise ValueError("PORT ERROR : Port n° can't be negative !")
    
    elif port > 65535:
        raise ValueError("PORT ERROR : Port n° can't be bigger than 65535 !")
    
    return [port]

def validate_port_range(input_port: str) -> List[int]:
    """
    Validate a port range input string.

    Args:
        input_port (str): Port range string (e.g., '20-25').

    Returns:
        List[int]: List of port numbers.

    Raises:
        ValueError: If the input is invalid.
    """

    ports = [p.strip() for p in input_port.split("-")]

    if len(ports) != 2:
        raise ValueError("PORT ERROR : Port range needs to be in 'start-end' format !")
    
    elif "" in ports:
        raise ValueError("PORT ERROR : Port n° can't be empty !")
    
    start_port_str, end_port_str = ports

    try:
        start_port = int(start_port_str)
    except ValueError:
        raise ValueError("PORT ERROR : The first port n° is invalid !")
    try:
        end_port = int(end_port_str)
    except ValueError:
        raise ValueError("PORT ERROR : The last port n° is invalid !")
    
    if start_port < 0 or end_port < 0:
        raise ValueError("PORT ERROR : Port n° can't be negative !")
    
    elif start_port > 65535 or end_port > 65535:
        raise ValueError("PORT ERROR : Port n° can't be bigger than 65535 !")
    
    elif start_port > end_port:
        raise ValueError("PORT ERROR : the first port should be less than or equal to the last port !")
    
    # Generate list of ports in the range
    return list(set(range(start_port, end_port + 1)))

def validate_ip(ip_address: str) -> str:
    """
    Validate an IPv4 address.
    
    Args:
        ip_address (str): The IP address string given by the user.
        
    Returns:
        str: The validated IP address.
    
    Raises:
        ValueError: If the IP is invalid.
    """
    
    ip_address = ip_address.strip()

    #Check for spaces in IP address
    if " " in ip_address:
        raise ValueError(f"IP ERROR : Spaces between characters are not allowed !")

    # Split the IP into a list octets
    octets = ip_address.split(".")

    # Validate the correct number of octets
    if len(octets) != 4:
        raise ValueError(f"IP ERROR : The IP address should have 4 octets !")
    
    # Validate each octet
    for o in octets:
        try:
            value = int(o)
        except ValueError:
            raise ValueError(f"IP ERROR : Octets must be numeric !")
        
        if not (0 <= value <= 255):
            raise ValueError("IP ERROR: Octets must be between 0 and 255 !")
    
    return ip_address

def validate_filename(filename: str) -> str:
    """
    Validate output filename.

    Only allows letters, numbers, underscores, dashes.
    Must end with .json
    """

    filename = filename.strip()

    if not filename.endswith(".json"):
        raise ValueError("FILE ERROR: Output file must end with .json")

    if not re.match(r'^[A-Za-z0-9_\-\.]+$', filename):
        raise ValueError("FILE ERROR: Filename contains invalid characters")

    return filename

#-----------------TEST------------------
if __name__ == "__main__":
    def run_test():
        test_case = [
            ("192.168.0.1", "n"),
            ("192.168.0.1", "-1"),
            ("192.168.0.1", "70000"),
            ("192.168.0.1", "20"),
            ("192.168.0.1", "1-100-150"),
            ("192.168.0.1", "1-1c0"),
            ("192.168.0.1", "0-1025"),
            ("192.168.0.1", "30-10"),
            ("192.168.0.1", "20-20"),
            ("192.168.0.  1", "1-100"),
            ("192.168.0", "1-100"),
            ("192.168.0.a", "1-100"),
            ("192.168.256.1", "1-100"),
            ("192.168.-1.1", "1-100"),
            ("192.168.0.1", "10-15")
    ]

        for i, (ip, port_range) in enumerate(test_case, start=1): #i = each () element, key = ip, value = port
            try:
                validate_ip(ip)
            except ValueError as e:
                print(f"Test {i} with IP {ip} and port(s) {port_range} raised a ValueError: {e}")
                continue
            
            try:
                validate_port(port_range)
                print(f"Test {i} with IP {ip} and port(s) {port_range} : {ip} and {port_range} are correct !")
            except ValueError as e:
                print(f"Test {i} with IP {ip} and port(s) {port_range} raised a ValueError: {e}")

    run_test()