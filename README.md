# Constant Simmer

Constant Simmer is a Python script for RaspberryPi that interfaces with a [DS18B20 temperature sensor](https://www.adafruit.com/product/381) and the [Digital Loggers IoT Relay](https://dlidirect.com/products/iot-power-relay), and allows you to keep your pots at a constant simmer! No need to tend to the stove, and no risk of boiling over!

## Ingredients
You will need:
1. Raspberry Pi with GPIO pins
2. DS18B20 temperature sensor
3. Digital Loggers IoT Relay
4. 4.7k Ohm Resistor
5. Leads (recommend an assortment of Female to Female, Male to Male & Female to Male)
6. Either a breadboard or a circuitboard and a soldering kit
7. A hot plate or other device to control

## Instructions
### Temperature Sensor
1. Connect data wire (yellow) to pin 7 (GPIO 4)
2. Connect power wire ( to pin 2 or 4 (5V)
3. Connect 4.7k Ohm resistor between data and power
4. Connect ground wire (black) to pin 6 (GND)

### Relay
1. Connect pin 22 (GPIO 25) to positive input of IoT Relay
2. Connect pin 20 (GND) to negative input of IoT Relay

### Usage
1. Plug in the IoT Relay to the wall
2. Plug in the Raspberry Pi to the "Always On" plug of the IoT Relay
3. Plug in the hot plate to the "Normally Off" plug of the IoT Relay
4. Put your pot on the hot plate and hang the temperature sensor inside, so the sensor is submerged (careful that the cable is not touching the hot plate)
5. Turn the hot plate to it's max setting
6. SSH to the Raspberry Pi* and run `python temp_control.py` in the terminal. The hot plate should turn on and you should start seeing temperature readings in the terminal.
7. By default, `temp_control.py` has a target simmer temperature of 82 deg C, but you can adjust the target temperature while the program is running by typing a new temperature in deg C in the terminal or by providing a command line argument like `python temp_control.py 75`
8. Go for a bike ride, read a book, visit a friend, and know that your pot is being kept at a constant simmer! (NOTE! Keep the SSH terminal open and running!)

* If you have not connected via SSH before, I recommend downloading the iPhone App PiHelper, or the Windows program PuTTY. Both devices (Raspberry Pi and phone/computer) must be on the same WiFi network. If in doubt, you can connect a keyboard and monitor to your Raspberry Pi and set your default network, which it will automatically join upon startup in the future. If you will be using Constant Simmer in a location with no internet, you can set your Raspberry Pi to [run `temp_control.py` upon startup](https://www.youtube.com/watch?v=Gl9HS7-H0mI).
