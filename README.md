# pyFirmataTest
A simple Firmata test program for Arduino Uno through Python's Tkinter and pyFirmata framework

#### Features
* A simple GUI window created by Python's Tkinter

* Can choose which Serial port to connect through a "Ports" menu

![choose serialport](https://github.com/rollingstarky/pyFirmataTest/blob/master/screenshots/choose_port.png)

* Choose board's pin through a "Pin" button and change it's value by clicking another button or dragging the scale tool (**for PWM output**)

![choose pin](https://github.com/rollingstarky/pyFirmataTest/blob/master/screenshots/choose_pin.png)

![change_value](https://github.com/rollingstarky/pyFirmataTest/blob/master/screenshots/change_value.png)

#### Requirements

* Install Python's pyFirmata framework: ``pip install pyfirmata``

* Flash the Firmata firmware into your Arduino board through the Arduino IDE or other tools

* Connect arduino to your computer and use ``python firmata-test.py`` to run the program

