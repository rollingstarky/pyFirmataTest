# pyFirmataTest
A simple Firmata test program for Arduino Uno through Python's Tkinter and pyFirmata framework

#### Features
1. A simple GUI window created by Python's Tkinter

2. Choose which Serial port to connect through a "Ports" menu
![choose serialport](https://github.com/rollingstarky/pyFirmataTest/blob/master/screenshots/choose_port.png)

3. Choose board's pins through a "Pin" button
![choose pin](https://github.com/rollingstarky/pyFirmataTest/blob/master/screenshots/choose_pin.png)

4. Change output value by clicking buttons or dragging the scale tool. There is also a dialog for [PWM](https://www.arduino.cc/en/Tutorial/PWM) output
![change_value](https://github.com/rollingstarky/pyFirmataTest/blob/master/screenshots/change_value.png)

#### Requirements

* Install Python's [pyFirmata](https://github.com/tino/pyFirmata) framework: ``pip install pyfirmata``

* Flash the [Firmata](http://firmata.org/wiki/Main_Page) into your Arduino board through the Arduino IDE or other tools

* Connect arduino to your computer and use ``python firmata-test.py`` to run the program

