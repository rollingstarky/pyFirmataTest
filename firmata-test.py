from tkinter import *
from tkinter.simpledialog import askinteger
from pyfirmata import Arduino, PWM
from serial.tools.list_ports import comports

root = Tk()

# a radiobutton menu to list and choose serial port


class PortsMenu(Menu):

    def __init__(self, parent=None, ports=[]):
        Menu.__init__(self, parent)

        self.ports = ports
        self.port = StringVar()

        self.add_menu()

    def add_menu(self):
        for port in self.ports:
            self.add_radiobutton(
                label=port,
                variable=self.port, value=port,
                command=self.choose_port)

    def choose_port(self):
        global board
        try:
            board = Arduino(self.port.get())
            print("connected to the serial port: %s" % self.port.get())
        except:
            print("please make sure you choose the right serial port")


# new Frame class contains a label to display it's function
# a button with quick menu to choose pin & display current pin number,
# and a button to change & display pin status
class Block(Frame):

    def __init__(self, parent=None, text="", pins=[]):
        Frame.__init__(self, parent)
        self.pins = {}
        self.init_pin(pins)

        self.current_pin = IntVar()
        self.current_pin.set(pins[0])

        self.add_label(text)
        self.menu_button = self.add_options(pins)
        self.button = CustomButton(self, text="LOW", command=self.click_button)
        self.pack()

    def init_pin(self, pins):
        for pin in pins:
            self.pins[pin] = 0

    def get_pin(self):
        return self.current_pin.get()

    def add_label(self, text):
        label = Label(self, text=text)
        label.config(width='15', height='3', font=('courier', 16, 'bold'))
        label.pack(side=LEFT)

    def add_options(self, pins):
        menu_button = CustomButton(self, text="Pin " + str(pins[0]))
        menu_button.bind(
            '<Button-1>', (lambda event: menu.post(event.x_root, event.y_root)))

        menu = Menu(tearoff=False)
        for pin in self.pins.keys():
            menu.add_radiobutton(
                label="Pin " + str(pin),
                command=self.update_status,
                variable=self.current_pin, value=pin)
        return menu_button

    def update_status(self):
        current_pin = self.get_pin()
        self.menu_button.config(text="Pin " + str(current_pin))
        if self.pins[current_pin]:
            self.button.config(text='HIGH', fg='red')
        else:
            self.button.config(text='LOW', fg='black')

    def click_button(self):
        current_pin = self.get_pin()
        self.pins[current_pin] = 1 - self.pins[current_pin]
        try:
            board.digital[current_pin].write(self.pins[current_pin])
            if self.pins[current_pin]:
                self.button.config(text="HIGH", fg="red")
                print("Pin %s sets to HIGH" % current_pin)
            else:
                self.button.config(text="LOW", fg="black")
                print("Pin %s sets to LOW" % current_pin)
        except:
            print("please make sure you choose the right serial port")

# a custom button class to create buttons with some common properties


class CustomButton(Button):

    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, **config)
        self.config(width='10', height='2', font=(
            'courier', 18, 'bold'), bd=1, relief=RAISED)
        self.pack(side=LEFT, padx=20, pady=20)

# new Frame class contains a label, a button with quick menu to choose pin
# and a scale to change & display pwm_output value


class PwmBlock(Block):

    def __init__(self, parent=None, text="", pins=[]):
        Block.__init__(self, parent, text, pins)

        self.scale_var = IntVar()
        self.scale_var.set(0)

        self.add_scale()
        self.button.config(text="0")

    def update_status(self):
        current_pin = self.get_pin()
        self.menu_button.config(text="Pin " + str(current_pin))
        self.button.config(text=self.pins[current_pin])
        self.scale_var.set(self.pins[current_pin])

    def click_button(self):
        input_value = askinteger(
            "PWM value", "Please input a number between 0-1023",
            minvalue=0, maxvalue=1023, initialvalue=0)
        if input_value is not None:
            self.onMove(input_value)
            self.scale_var.set(input_value)

    def add_scale(self):
        Scale(self, label="Drag to choose an output value",
              command=self.onMove,
              variable=self.scale_var,
              from_=0, to_=1023, length=300,
              orient='horizontal').pack(side=LEFT)

    def onMove(self, value):
        current_pin = self.get_pin()
        self.pins[current_pin] = int(value)
        self.button.config(text=value)
        value = int(value) / 1024
        try:
            board.digital[current_pin].mode = PWM
            board.digital[current_pin].write(value)
            print("Pin %s sets PWM output: %d" %
                  (current_pin, self.pins[current_pin]))
        except:
            print("please make sure you choose the right serial port")


# the ports menu of menubar, to choose arduino serial port
serial_ports = [port[0] for port in comports()]
menu = Menu(root)
root.config(menu=menu)
ports_menu = PortsMenu(menu, serial_ports)
menu.add_cascade(label="Ports", menu=ports_menu)


# digital output pin2 to pin13
digital_pins = [x + 2 for x in range(12)]
digital_pins_block = Block(root, "Digital Write", digital_pins)


pwm_pins = [3, 5, 6, 9, 10, 11]
pwm_pins_block = PwmBlock(root, "PWM Write", pwm_pins)
pwm_pins_block.pack(side=BOTTOM)


if __name__ == '__main__':
    root.mainloop()
