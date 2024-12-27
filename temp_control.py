
"""
TEMP SENSOR (DS18B20)
yellow = data
red = power
black = ground

connect data wire to pin 7 (GPIO 4)
connect power wire to pin 2 or 4 (5V)
connect ground wire to pin 6 (GND)
connect 4.7kOhm resistor between data and power
"""

"""
RELAY (Digital Loggers IoT Relay)
connect pin 22 (GPIO 25) of Pi to positive side of IoT Relay input
connect pin 20 (GND) of Pi to negative side of IoT Relay input
"""

import sys
import keyboard
import threading
from time import sleep
import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor

RELAY_PIN = 22
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RELAY_PIN, GPIO.OUT)

sensor = W1ThermSensor()

def main():
    global TEMP

    if len(sys.argv) == 1:
        TEMP = 82
    elif len(sys.argv) == 2:
        TEMP = float(sys.argv[1])
    else:
        print("Usage: python temp_control.py <temp-in-celcius>, e.g. python temp_control.py 82")
        quit()

    def handle_user_input():
        global TEMP
        while True:
            user_input = input("\nAt any time, you can change the target temperature by typing a new target temperature in deg C in the command line and pressing Enter\n\n")
            try:
                new_temp = float(user_input)
                if 0 < new_temp and new_temp < 102:
                    TEMP = new_temp
                else:
                    print("New target temp must be between 0 and 102 deg C")
            except:
                print("Error handling input temperature")


    input_thread = threading.Thread(target=handle_user_input)
    input_thread.daemon = True
    input_thread.start()

    status = "OFF"
    while True:
        temp = sensor.get_temperature()

        if temp < TEMP and status == "OFF":
            GPIO.output(RELAY_PIN, GPIO.HIGH)
            status = "ON"
        elif temp >= TEMP and status == "ON":
            GPIO.output(RELAY_PIN, GPIO.LOW)
            status = "OFF"

        print("Current: {:.1f}C, Target: {:.1f}C, Now: {}".format(temp, TEMP, status))
        sleep(5)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
    except KeyboardInterrupt:
        GPIO.output(RELAY_PIN, GPIO.LOW)
        GPIO.cleanup()
        quit()
    finally:
        GPIO.output(RELAY_PIN, GPIO.LOW)
        GPIO.cleanup()
        quit()
