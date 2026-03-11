
from typing import List, Tuple  # Import type hints for better code clarity

def write_to_console(scan_result: List[Tuple[int, bool]]):
    """
    Prints a formatted table of port scan results to the console.
    Each result is a tuple: (port:int, status:bool)
    True  -> OPEN
    False -> CLOSED
    """

    # Print a header for the scan results
    print("\nScan Results")
    
    # Print a dividing line for readability
    print("-" * 30)
    
    # Print column headers for PORT and STATUS
    # '<10' aligns the text left with 10 character width
    print(f"{'PORT':<10}{'STATUS'}")
    
    # Another dividing line after headers
    print("-" * 30)

    # Loop through each tuple in the scan results
    for port, status in scan_result:
        # Convert boolean status to readable text
        # True  -> "OPEN"
        # False -> "CLOSED"
        state = "OPEN" if status else "CLOSED"

        # Print port number and its status in formatted table style
        print(f"{port:<10}{state}")


# Example scan results as a list of tuples (port, status)
results = [
    (21, True),   # Port 21 is OPEN
    (22, False),  # Port 22 is CLOSED
    (23, False)   # Port 23 is CLOSED
]

# Call the function to display results in the console
write_to_console(results)