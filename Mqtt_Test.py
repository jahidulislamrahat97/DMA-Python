import paho.mqtt.client as mqtt
import time

BROKER = "broker.hivemq.com"
PORT = 1883
KEEP_ALIVE = 120
SUB_TOPIC = "Rahat/Test/PUB"
PUB_TOPIC = "Rahat/Test/Hello"
client = mqtt.Client()
flag_connected = 0

def on_connect(client, userdata, flags, rc):
    global flag_connected
    print("mqtt connected")
    client.subscribe(PUB_TOPIC,qos=2)
    flag_connected = 1

def on_disconnect(client, userdata, rc):
    global flag_connected
    print("mqtt not connected")
    flag_connected = 0

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

# def execute(msg):
#     data = msg.payload.decode('utf-8')
#     print(data)

if __name__ == "__main__":
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.connect(BROKER,PORT,KEEP_ALIVE)
    client.on_message = on_message
    client.loop_forever()
    client.publish(topic=SUB_TOPIC,payload="Helllooo",qos=2)
    while True:
        if flag_connected == 1:
            print("")  
        else:
            client.reconnect()
            print("mqtt not connected")
        time.sleep(1)
        client.loop()
        
