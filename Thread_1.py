from mqtt_client import MqttClient
import random
import time

SUB_PATH = "Rahat/Test/PUB"
PUB_PATH = "Rahat/Test/Hello"
# TARGET_DID = "8020012302070002"

if __name__ == "__main__":
    def execute(msg):
        data = msg.payload.decode('utf-8')
        print(data)
        client.publish(topic=PUB_PATH,payload = data)
       
    client = MqttClient(id="aybvdfvbhkdvadvfabfdavdvafvzbkfh", use_id_as_client_id=False)
    client.getMqttSubTopic(SUB_PATH)
    client.getMqttPubTopic(PUB_PATH)
    client.setOnMessageCallbackFunction(execute)
    client.connect()
    
    while True:
        # time.sleep(1)
        client.client.loop()
        