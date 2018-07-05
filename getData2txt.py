import paho.mqtt.client as mqtt
import os

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    #Open file data.txt and write data
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    fo=open("data.txt","a")
    fo.write(msg.topic + " " + str(msg.qos) + " " + str(msg.payload)+"\n")
    fo.close()
    #print( str(msg.payload))
    


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
mqttc.subscribe("cokhi/#", 0)
mqttc.loop_forever()