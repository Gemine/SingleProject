import socket
import subprocess
import sys
import os
import numpy as np
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Create a TCP/IP socket
server_ip = np.array(["111"])
thu_tu = 0
hostname="192.168.1."
ketQua = np.array([])
for ip in server_ip:
    rep = subprocess.Popen(["ping.exe",hostname+ip],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in rep):
		ketQua= np.append(ketQua,ip)
print(ketQua)