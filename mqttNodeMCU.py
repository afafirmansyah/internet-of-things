import network
import time
import umqttsimple as mqtt
import machine
import ubinascii
import json

clientID = ubinascii.hexlify(machine.unique_id())

led = machine.Pin(2, machine.Pin.OUT)
led.value(1)

wlan = network.WLAN(network.STA_IF)
if not wlan.isconnected():
    print("Connecting...")
    wlan.active(True)
    wlan.connect("TP-Link_4B8F", "25700086")
    while not wlan.isconnected():
        print(".", end='')
        time.sleep(0.5)
    print("\nNetwork config: ", wlan.ifconfig())

def subcallback(topic, msg):
    print(topic, msg)
    mdata = json.loads(msg.decode())
    print(mdata["sensor"], mdata["nilai"])
    if mdata["nilai"] > 37.0:
        led.value(0)
    else:
        led.value(1)


print("ID: ", clientID)
client = mqtt.MQTTClient(clientID, "broker.hivemq.com")
client.set_callback(subcallback)
client.connect()
client.subscribe(b"nsone/smartlamp")
print("Connected")

lastime = time.time()
while True:
    client.check_msg()
    
    if time.time() - lastime >5:
        mdata = {"sensor":"TEMP", "nilai":39.3}
        message = json.dumps(mdata)
        client.publish(b"nsone/smartlamp", message.encode())
        lastime = time.time()

