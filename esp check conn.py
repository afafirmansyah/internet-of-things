import network
import time
import umqttsimple as mqtt
import machine
import ubinascii

clientID = ubinascii.hexlify(machine.unique_id())

wlan = network.WLAN(network.STA_IF)
if not wlan.isconnected():
    print("Connecting...")
    wlan.active(True)
    wlan.connect("TP-Link_4B8F", "25700086")
    while not wlan.isconnected():
        print(".", end='')
        time.sleep(0.5)
    print("\nNetwork config: ", wlan.ifconfig())

def subcallbacl(topic, msg)
    print(topic, msg)


print("ID: ", cliendID)
client = mqtt.MQTTClient(clientID, "broker.hivemq.com")
client.set_callback(subcallback)
client.connect()
client.subscribe(b "nsone/smartlamp")
print("Connected")

while True:
    client.check_msg()
    