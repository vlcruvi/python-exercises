#!/usr/bin/env python3
import socket
import sys
#from time import sleep
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST, PORT)
def main():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(ADDR)
            answer =  0
            switch = True
            while switch == True:
                msg = s.recv(1024)
                # print(msg)
                msg = msg.decode()
                msg = msg.strip()
                # print(msg)
                if "RCN" in msg:
                    # print("found rcn")
                    print(msg.split()[-1])
                    switch = False
                else:
                    msg = msg.split()[-1]
                    answer = int(msg) + 1
                    answer = str(answer) + '\n'
                    #print("answer: "  + answer)
                    answer = answer.encode()
                    s.send(answer)
                    #sleep(1)
            if switch == True:
                print("found rcn")
                print(msg)
main()
