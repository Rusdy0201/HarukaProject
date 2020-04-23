import time

from pyfirmata import Arduino, util

board = Arduino ('/dev/ttyACM0')

led_pin = 13
it = util.Iterator(board)
it.start()

def blink():
    while True:
        board.digital[led_pin].write(1)
        board.pass_time(1)
        board.digital[led_pin].write(0)
        board.pass_time(1)
