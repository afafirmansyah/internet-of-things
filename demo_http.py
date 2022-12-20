import network
import time
import umqttsimple as mqtt
import machine
import ubinascii
import json
import urequests

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

response = urequests.get("http://jsonplaceholder.typicode.com/albums/1")
print(response.text)
parsed = response.json()

print(parsed["userId"])
print(parsed["id"])
print(parsed["title"])
