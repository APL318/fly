#
# Tello Python3 Control Demo
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

import threading
import socket
import sys
import time

#Local IP
host = ''
port = 9000
locaddr = (host,port)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(locaddr)

#Tello IP
tello_address = ('192.168.10.1', 8889)

#Define the send command and send the commands in send to the Telo
def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break


recvThread = threading.Thread(target=recv)
recvThread.start()









try:
        msg = "command" ;
        # Send data
        msg = msg.encode(encoding="utf-8")
        sent = sock.sendto(msg, tello_address)

        msg1 = "takeoff";
        # Send data
        msg1 = msg1.encode(encoding="utf-8")
        sent = sock.sendto(msg1, tello_address)
        
        time.sleep(8)
        msg2 = "up 100";
        # Send data
        msg2 = msg2.encode(encoding="utf-8")
        sent = sock.sendto(msg2, tello_address)

        time.sleep(12)
        msg2 = "forward 200";
        # Send data
        msg2 = msg2.encode(encoding="utf-8")
        sent = sock.sendto(msg2, tello_address)
        
        time.sleep(12)
        msg2 = "ccw 180";
        # Send data
        msg2 = msg2.encode(encoding="utf-8")
        sent = sock.sendto(msg2, tello_address)
        
        time.sleep(12)
        msg2 = "forward 200";
        # Send data
        msg2 = msg2.encode(encoding="utf-8")
        sent = sock.sendto(msg2, tello_address)
        
        time.sleep(12)
        msg2 = "battery?";
        # Send data
        msg2 = msg2.encode(encoding="utf-8")
        sent = sock.sendto(msg2, tello_address)
        
        time.sleep(12)
        msg2 = "cw 180";
        # Send data
        msg2 = msg2.encode(encoding="utf-8")
        sent = sock.sendto(msg2, tello_address)
        
        time.sleep(5)
        msg6 = "land";
        # Send data
        msg6 = msg6.encode(encoding="utf-8")
        sent = sock.sendto(msg6, tello_address)
        
        print ('\n . . .\n')
        sock.close()

except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()
