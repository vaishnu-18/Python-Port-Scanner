import json
from typing import List, Tuple

def store_to_file(scan_result: List[Tuple[int, bool]], filename: str = "scan_results.json"):
    """
    Stores port scan results in a JSON file.
    
    Parameters:
    - scan_result: List of tuples (port:int, status:bool)
      True  -> OPEN
      False -> CLOSED
    - filename: Name of the JSON file to save results (default: "scan_results.json")
    """

    # Convert the list of tuples into a list of dictionaries for readable JSON
    # Each dictionary has "port" and "status" keys
    data = []
    for port, status in scan_result:
        data.append({
            "port": port,
            "status": "OPEN" if status else "CLOSED"  # Convert boolean to string
        })

    # Open the file in write mode ("w"). This will create the file if it does not exist
    with open(filename, "w") as file:
        # Write the data to JSON with indentation for readability
        json.dump(data, file, indent=4)


# Example usage
results = [
    (21, True),   # Port 21 is OPEN
    (22, False),  # Port 22 is CLOSED
    (23, False)   # Port 23 is CLOSED
]

# Save results to JSON
store_to_file(results, "scan_results.json")
