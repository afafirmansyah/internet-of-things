import paho.mqtt.client as mqtt 
import time
import json
import sqlite3


def on_connect(client, data, flags, rc):
  client.subscribe("nsone/smartlamp")

def on_message(client, data, msg):
  
  conn = sqlite3.connect("database.db")
  cursor = conn.cursor()
  print(msg.topic, msg.payload)
  mdata = msg.payload.decode()
  mdata = json.loads(mdata)  # json -> dict
  sensor = mdata["sensor"]
  nilai = mdata["nilai"]  
  print(sensor, nilai)
  cursor.execute("INSERT INTO iot (sensor, nilai, tanggal, waktu, stamp) VALUES ( '%s', %s, current_date, current_time, current_timestamp )" % ( sensor, nilai ))
  conn.commit()
  cursor.close()
  conn.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com",1883)
client.loop_start()

while True:
  conn = sqlite3.connect("database.db")
  cursor = conn.cursor()

  cursor.execute("SELECT sensor, nilai, tanggal, waktu FROM iot")
  rows = cursor.fetchall()
  for row in rows:
    print(row[0], row[1], row[2], row[3])
  cursor.close()
  conn.close()
  time.sleep(10)
