#!/usr/bin/env python3

import socket
import sys



HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST, PORT)

def main(ADDR):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        number = 0
        s.connect(ADDR)  
       
        while number < 26:
            message = str(number) + '\n'
            message = message.encode()
            s.send(message)
            number += 1
        
            msg = s.recv(1024)
            print(msg.decode())

main(ADDR)

