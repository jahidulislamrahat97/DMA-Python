from mqtt_client import MqttClient
import random
import time

SUB_PATH = "Rahat/Test/SUB"
PUB_PATH = "Rahat/Test/PUB"

data_limit = 100

if __name__ == "__main__":
    def execute(msg):
        data = msg.payload.decode('utf-8')
        print(data)
       
    client = MqttClient(id="aybvdfvbhkfdavdvafvzbkfh", use_id_as_client_id=False)
    client.getMqttSubTopic(SUB_PATH)
    client.getMqttPubTopic(PUB_PATH)
    client.setOnMessageCallbackFunction(execute)
    client.connect()
    
    while True:
        for i in range(data_limit):
            data = str(i)+" Hello"
            print(data)
            client.publish(topic=PUB_PATH,payload = data)
            client.client.loop()

        # i=0
        # time.sleep(1)
        exit()
        