from mqtt_client import MqttClient
import random
import time

SUB_PATH = "DMA/MoreFish/Padma_Shrimps"
PUB_PATH = "DMA/MoreFish/Padma_Shrimps"
# SUB_PATH = "DMA/MoreFish/Test"
# PUB_PATH = "DMA/MoreFish/Test"
TARGET_DID = "8020012302070002"


def publishData(data,waitingTime):
    time.sleep(waitingTime)
    if (client.publish(topic=SUB_PATH, payload=data)):
        print("Data Published Failed")
    else:
        print("Data Published Successfully")


if __name__ == "__main__":
    def execute(msg):
        data = msg.payload.decode('utf-8')
        print(data)
        decoded_data = data.split(',')
        data_len = len(decoded_data)
        # print("data len:" + str(data_len))

        if(data_len == 5):
            GID = decoded_data[0]
            DID = decoded_data[1]
            TDS = int(decoded_data[2])
            TEMP = int(decoded_data[3])
            PH = int(decoded_data[4])

            print(GID)
            print(DID)
            print(TDS)
            print(TEMP)
            print(PH)

            if(DID == TARGET_DID):
                data = GID+ ","+ "8020012302070005," + str(TDS + random.randint(-5,5))+ "," + str(TEMP + random.randint(-5,5))+ "," + str(PH + random.randint(-5,5))
                print("Target Data: " + data)
                waitingTime =  random.randint(20, 40)
                print("Waiting Time:", str(waitingTime))
                publishData(data, waitingTime)
                
                


        
    client = MqttClient(id="aybvdfvbhkfdavbkfh", use_id_as_client_id=False)
    client.getMqttSubTopic(SUB_PATH)
    client.getMqttPubTopic(PUB_PATH)
    client.setOnMessageCallbackFunction(execute)
    client.connect()
    
    while True:
        # dummy_data = {
        # 'compass_heading': random.randint(0,360),
        # 'gps_heading': random.randint(0, 255),
        # 'bot_speed': random.randint(1, 25),
        # 'gps_speed': random.randint(1, 25),
        # 'rudder_angle': random.randint(0, 30),
        # 'satellite': random.randint(1, 25),
        # 'valid': random.randint(0, 1)
        # }
        
        # payload = json.dumps(dummy_data)
        # client.publish(topic=SUB_PATH,payload = payload)
        time.sleep(1)
        client.client.loop()
        