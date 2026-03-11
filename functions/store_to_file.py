import json
from typing import List, Tuple

def store_to_file(ip_address: str, scan_result: List[Tuple[int, bool]], filename: str = "scan_results.json"):
    """
    Declaring the function
    Stores port scan results in a JSON file.
    
    Parameters:
    - ip_address: str -> The IP address scanned
    - scan_result: List of tuples (port:int, status:bool)
      True  -> OPEN
      False -> CLOSED
    - filename: Name of the JSON file to save results (default: "scan_results.json")
    """

    # Convert the list of tuples into a list of dictionaries
    data = []
    for port, status in scan_result:
        data.append({
            "ip": ip_address,
            "port": port,
            "status": "OPEN" if status else "CLOSED"
        })

    # Write the data to JSON file with indentation for readability
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# Example usage
ip_address = "192.168.1.1"
results = [
    (21, True),
    (22, False),
    (23, False)
]

# Save results to JSON
store_to_file(ip_address, results, "scan_results.json")