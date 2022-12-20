import paho.mqtt.client as mqtt 
import json

m = {"sensor":"TEMP", "nilai":28.3}

client = mqtt.Client()

client.connect("broker.hivemq.com",1883)
client.loop_start()

while True:
  minput = input("Press anykey")
  client.publish("nsone/smartlamp", json.dumps(m))
