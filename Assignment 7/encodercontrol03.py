#automatically rotate the wheel for one rotation and test the encoder
import RPi.GPIO as gpio
import time
import numpy as np

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(31,gpio.OUT) #IN1
    #gpio.setup(33,gpio.OUT) #IN2
    #gpio.setup(35,gpio.OUT) #IN3
    gpio.setup(37,gpio.OUT) #IN4
    #right back wheel encoder
    gpio.setup(12,gpio.IN,pull_up_down = gpio.PUD_UP)
    #left front wheel encoder
    gpio.setup(7,gpio.IN,pull_up_down = gpio.PUD_UP)
def gameover():
    gpio.output(31,False)
    #gpio.output(33,False)
    #gpio.output(35,False)
    gpio.output(37,False)

#MAIN CODE
    
init()

counter = np.uint64(0)
counter2 = np.uint64(0) 
button = int(0)
button2 = int(0)

#initialize pwm signal to control motor

pwm = gpio.PWM(37,50)
val = 16
pwm.start(val)
time.sleep(0.1)

list_of_gpio = []
list_of_gpio_2 = []
for i in range(0,200000):

    print("counter = ",counter,"GPIO state ( 12 ): ",gpio.input(12))
    print("counter = ",counter,"GPIO state ( 7 ): ",gpio.input(7))
    list_of_gpio.append(gpio.input(12))
    list_of_gpio_2.append(gpio.input(7))
    if int (gpio.input(12)) != int(button):
        button = int(gpio.input(12))
        counter+= 1
    if int (gpio.input(7)) != int(button2):
        button2 = int(gpio.input(7))
        counter2+=1
    if counter >= 20:
         pwm.stop()
         gameover()
         print("THANKS")
         gpio.cleanup()
         break

file = open('gpio_values_03_1.txt','w')
for i in list_of_gpio:
    file.write(str(i))
    file.write('\n')
file.close()


file = open('gpio_values_03_2.txt','w')
for i in list_of_gpio_2:
    file.write(str(i))
    file.write('\n')
file.close()
