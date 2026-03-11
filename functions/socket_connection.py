from typing import List, Tuple
import socket
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def socket_connection(ip_address: str, port: int) -> tuple[int,bool]:
    """
        Attempts to connect to a single TCP port

        Inputs:
            A target IP address (str)
            A target TCP port number (int)

        Output:
            A boolean indicating if the port is open
    """
    # Creates a socket (necessary for a network connection)
    # The arguments specify the format (outside of the scope of this project)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Sets a timeout after which the accempt is interrupted
    sock.settimeout(1)

    # Do a "try" to handle exceptions raised during the connection attempt
    try:
            # Try to connect to a specified port on a specified ip address
            # Returns an integer, 0 = success, otherwise => error code
            result = sock.connect_ex((ip_address, port))

            # We check the result, if it's 0 the port is open, otherwise it is closed
            is_open: bool = (result == 0)

            # Logging the attempt
            if is_open: logging.info(f"finished scanning {ip_address} : {port} - port open") 
            else: logging.info(f"finished scanning {ip_address} : {port} - port closed")

            port_status = (port,is_open)

            return port_status
    
    # Exception - Name resolution failed
    except socket.gaierror:
            logging.debug("aborted - name resolution failed")
            port_status = (port,False)
            return port_status
    
    # Exception - Network/socket error
    except OSError:
            logging.debug("aborted - network/socket error")
            port_status = (port,False)
            return port_status
    finally:
            sock.close()


# Testing
#is_open = socket_connection("192.168.56.101",22)
#print(is_open)



