from typing import List, Tuple
from .validate_input import validate_ip, validate_port, validate_port_range #uncomment before pushing !
#from validate_input import validate_ip, validate_port, validate_port_range #for testing

def get_ip() -> str:
    """
    Prompt the user to enter an IP address and validate it.
    Keeps asking until a valid IP address is provided.

    Returns:
        str: A valid IP address.
    """
    
    ip = input("Enter an IP address : ").strip()
    
    while True:
        try:
            validate_ip(ip)
            return ip
        except ValueError as e:
            ip = input(f"{e} Please Enter a valid IP address : ").strip()

def get_port() -> List[int]:
    """
    Ask the user whether to scan a single port or a range of ports.

    Returns:
        List[int]: List of ports to scan.
    """
    
    choice = input("Scan a range of ports ? (y/n) : ").strip().lower()
    
    while choice not in ("yes", "y", "no", "n"):
        print("You can only type 'yes/no' or 'y/n'.")
        choice = input("Scan a range of ports ? ").strip().lower()
    
    # SINGLE PORT
    if choice in ("no", "n"):
        
        single_port = input("Port n° : ").strip()
        
        while True:
            try:
                return validate_port(single_port)
            except ValueError as e:
                single_port = input(f"{e} - Please enter a valid port : ").strip()

    # RANGE OF PORTS
    elif choice in ("yes", "y"):
        
        MAX_LENGTH = 100
        
        start_port = input("Starting port : ").strip()
        end_port = input("Ending port : ").strip()

        while True:
            try:
                ports = validate_port_range(f"{start_port}-{end_port}")
                
                #check if the list is too large
                if len(ports) > MAX_LENGTH:
                    
                    print(f"WARNING : This range contains {len(ports)} ports.")
                    print(f"Recommended maximum is {MAX_LENGTH}.")

                    #Ask user if they want to continue
                    while True:
                        continue_choice = input("Continue anyway ? (y/n): ").strip().lower()

                        if continue_choice in ("y", "yes"):
                            return ports
                        
                        elif continue_choice in ("n", "no"):
                            print("Please enter a smaller range.")
                            start_port = input("Starting port : ").strip()
                            end_port = input("Ending port : ").strip()
                            break
                        
                        else:
                            print("You can only type 'yes/no' or 'y/n'.")
                else:
                    return ports
                
            except ValueError as e:
                print(f"{e} Please enter valid ports :")
                start_port = input("Starting port : ").strip()
                end_port = input("Ending port : ").strip()

def take_input() -> Tuple[str, List[int]]:
    """
    Collect IP address and port(s) inputs from the user.

    Returns:
        Tuple[str, List[int]]: The IP address and list of ports.
    """
    ip = get_ip()
    port = get_port()
    return ip, port

if __name__ == "__main__":
    print(take_input()) #only for testing