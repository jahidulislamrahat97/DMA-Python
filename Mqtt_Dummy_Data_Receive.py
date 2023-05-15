from mqtt_client import MqttClient
import random
import time
import asyncio  


SUB_PATH = "Rahat/Test/PUB"
PUB_PATH = "Rahat/Test/Hello"
# TARGET_DID = "8020012302070002"

client = MqttClient(id="aybvdfvbhkdvadvfabfdavdvafvzbkfh", use_id_as_client_id=False)

async def publishData(topic, data, delay):  
    await asyncio.sleep(delay)  
    client.publish(topic=topic,payload = data) 

def execute(msg):
    data = msg.payload.decode('utf-8')
    print(data)
    delay = random.randint(1, 3)
    print("delay time: "+ str(delay))
    asyncio.run(publishData(PUB_PATH, data, delay = delay))


if __name__ == "__main__": 
    client.getMqttSubTopic(SUB_PATH)
    client.getMqttPubTopic(PUB_PATH)
    client.setOnMessageCallbackFunction(execute)
    client.connect()
    
    while True:
        # time.sleep(1)
        client.client.loop()        