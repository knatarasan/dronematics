'''

To read file ../data/DJI_0876.SRT and feed as Drone

'''

import os
import socket,time

class Drone:
    def __init__(self):
        pass
    
    def get_stream(self):
        # echo-server.py

        HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
        PORT = 9997  # Port to listen on (non-privileged ports are > 1023)
    
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            prev_time = ''
            with conn:
                with open('drone_simulator/data/DJI_0876.SRT','r') as f:
                    for line in f.readlines():
                        if line[:2]=='00':
                            prev_time = line[-13:-1]

                        if line[:3]=='GPS':
                            conn.sendall((prev_time+' '+line).encode('utf-8'))
                            time.sleep(0.030)

drone = Drone()

drone.get_stream()
