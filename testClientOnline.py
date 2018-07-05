import socket
import subprocess
import sys
import os
import numpy as np
import paho.mqtt.client as mqtt

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    print( str(msg.payload))
    # print("http://192.168.116.38:8540/QuanLyThungRac/AddStatusFromMQTT?status="+msg.topic+"_"+str(msg.payload));
    
    
	
    # try:
    #     #contents = urllib2.urlopen("http://192.168.116.38:8540/QuanLyThungRac/AddStatusFromMQTT?status="+msg.topic+"_"+str(msg.payload)).read()
    #     r = requests.get("http://192.168.116.38:8540/QuanLyThungRac/AddStatusFromMQTT?status="+msg.topic+"_"+str(msg.payload))
    #     print(r.text)
    # except Exception: 
    #    print("Loi!")
    #    pass


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
mqttc.connect("192.168.1.105", 1883, 60)
mqttc.subscribe("ip", 0)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Create a TCP/IP socket
server_ip = np.array(["110","117","118","220"])
thu_tu = 0
hostname="192.168.1."
ketQua = np.array([])
for ip in server_ip:
  rep = subprocess.Popen(["ping.exe",hostname+ip],stdout = subprocess.PIPE).communicate()[0]
  print(rep)
  if ('unreachable' in rep):
    ketQua= np.append(ketQua,ip)
    mqttc.subscribe(ip,0)
    mqttc.publish(ip, payload="disconnect", qos=0, retain=False)

print(ketQua)
