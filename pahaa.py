import paho.mqtt.client as mqtt
import time

def on_connect(client, data, flags, rc):
  client.subscribe("nsone/smartlamp")

def on_message(client, data, msg):
  print(msg.topic, msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com",1883)
client.loop_start()
while True:
  m = input("Message: ")
  client.publish("nsone/smartlamp", m)
