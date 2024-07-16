from machine import Pin
import time

# Define the LED pin
led = Pin(17, Pin.OUT)

# Blink the LED in an infinite loop
while True:
    led.on()
    time.sleep(1)  # LED on for 1 second
    led.off()
    time.sleep(1)  # LED off for 1 second
