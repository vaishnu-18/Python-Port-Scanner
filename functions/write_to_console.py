from typing import List, Tuple  # For type hints

def write_to_console(ip_address: str, scan_result: List[Tuple[int, bool]]):
    """
    Prints a formatted table of port scan results to the console.
    Each result is a tuple: (port:int, status:bool)
    True  -> OPEN
    False -> CLOSED
    """
    
    # Print header
    print("\nScan Results")
    
    # Dividing line
    print("-" * 40)
    
    # Column headers: IP, PORT, STATUS
    print(f"{'IP':<15}{'PORT':<10}{'STATUS'}")
    
    # Another dividing line
    print("-" * 40)
    
    # Loop through results
    for port, status in scan_result:
        state = "OPEN" if status else "CLOSED"
        print(f"{ip_address:<15}{port:<10}{state}")


# Example usage
ip_address = "192.168.1.1"
scan_results = [
    (21, True),
    (22, False),
    (23, False)
]

# Call the function
write_to_console(ip_address, scan_results)