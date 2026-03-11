from typing import List, Tuple

def validate_port(input_port: str) -> List[int]:
    """
    Validate a port or port range input string.

    Args:
        input_port (str): Port or port range string (e.g., '80' or '20-25').

    Returns:
        List[int]: List of port numbers.

    Raises:
        ValueError: If the input is invalid.
    """

    # Check if input is a single port
    if "-" not in input_port:
        
        # Validate that the input is a number
        if not input_port.isdigit():
            raise ValueError("Invalid port : Should be a number !")
        
        port = int(input_port)
        
        # Validate port range
        if not (0 <= port <= 65535):
            raise ValueError("Invalid port : Must be between 0 and 65535.")
    
        return [port]

    else:
        # Handle port range
        ports = input_port.split("-")
        
        if len(ports) != 2:
            raise ValueError("Invalid ports : Needs to be in 'start_port-end_port' format.")
    
    start_port, end_port = ports[0], ports[1]
    
    # Validate that start and end ports are numeric
    if not start_port.isdigit() or not end_port.isdigit():
        raise ValueError("Ports should be numbers above 0.")
    
    start_port, end_port = int(start_port), int(end_port)
    
    # Validate port range
    if not (0 <= start_port <= 1024 and 0 <= end_port <= 1024):
        raise ValueError("Ports must be between 0 and 1024.")
    
    if start_port > end_port:
        raise ValueError("Start port should be less than or equal than end port.")
    
    # Generate list of ports in the range, removing duplicates if any
    return list(range(start_port, end_port + 1))

def validate_ip(ip_address: str) -> str:
    """
    Validate the IP address and ports input.
    
    Args:
        ip_address (str): The IP address string given by the user.
        
    Returns:
        str: The validated IP address.
    
    Raises:
        ValueError: If the IP or ports are invalid.
    """
    
    #Check for spaces in IP address
    if " " in ip_address:
        raise ValueError(f"Invalid IP : Spaces are not allowed !")

    # Split the IP into a list octets
    octets = ip_address.split(".")

    # Validate the correct number of octets
    if len(octets) != 4:
        raise ValueError(f"Invalid IP : Should have 4 octets.")
    
    # Validate each octet
    for o in octets:
        if not o.isdigit() or not (0 <= int(o) <= 255):
            raise ValueError(f"Invalid IP : Each octets should be numbers between 0 and 255.")
    
    return ip_address

#-----------------TEST------------------
# def run_test():
#     test_case = [
#         ("192.168.0.1", "n"),
#         ("192.168.0.1", "-1"),
#         ("192.168.0.1", "70000"),
#         ("192.168.0.1", "20"),
#         ("192.168.0.1", "1-100-150"),
#         ("192.168.0.1", "1-1c0"),
#         ("192.168.0.1", "0-1025"),
#         ("192.168.0.1", "30-10"),
#         ("192.168.0.1", "20-20"),
#         ("192.168.0.  1", "1-100"),
#         ("192.168.0", "1-100"),
#         ("192.168.0.a", "1-100"),
#         ("192.168.256.1", "1-100"),
#         ("192.168.-1.1", "1-100"),
#         ("192.168.0.1", "10-15")
# ]

#     for i, (ip, port_range) in enumerate(test_case, start=1): #i = each () element, key = ip, value = port
#         try:
#             validate_ip(ip)
#         except ValueError as e:
#             print(f"Test {i} with IP {ip} and port(s) {port_range} raised a ValueError: {e}")
#             continue
        
#         try:
#             validate_port(port_range)
#             print(f"Test {i} with IP {ip} and port(s) {port_range} : {ip} and {port_range} are correct !")
#         except ValueError as e:
#             print(f"Test {i} with IP {ip} and port(s) {port_range} raised a ValueError: {e}")

# run_test()