from typing import List, Tuple
import socket
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def socket_connection(ip_address: str, port: int) -> bool:
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
            logging.info(f"scanning {ip_address} : {port} ...")

            result = sock.connect_ex((ip_address, port))

            # We check the result, if it's 0 the port is open, otherwise it is closed
            is_open: bool = (result == 0)

            #print("attempt succeeded")
            if is_open: logging.info("finished - port open") 
            else: logging.info("finished - port closed")
            

            return is_open
    
    # Exception - Name resoltuion failed
    except socket.gaierror:
            logging.debug("aborted - name resolution failed")
            return False
    
    # Exception - Network/socket error
    except OSError:
            logging.debug("aborted - network/socket error")
            return False
    finally:
            sock.close()


#is_open = socket_connection("192.168.56.101",22)
#print(is_open)



