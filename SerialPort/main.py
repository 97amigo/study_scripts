import pyfirmata
import datetime

led_pin = 13
board = pyfirmata.Arduino("COM5")

while True:
    fr = input("Введите частоту мигания светодиода(Гц): ")
    t1 = datetime.datetime.now()
    while True:
        board.digital[led_pin].write(1)
        board.pass_time(1 / (int(fr)*2))
        board.digital[led_pin].write(0)
        board.pass_time(1 / (int(fr)*2))
        t2 = datetime.datetime.now()
        if (t2 - t1).seconds > 5:
            break
