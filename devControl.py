import time

from pyfirmata import Arduino, util

board = Arduino ('/dev/ttyACM0')

it = util.Iterator(board)
it.start()

#define pin Digital Input Arduino
d1Input = board.get_pin('d:1:i')
d2Input = board.get_pin('d:2:i')
d3Input = board.get_pin('d:3:i')
d4Input = board.get_pin('d:4:i')
d5Input = board.get_pin('d:5:i')
d6Input = board.get_pin('d:6:i')
d7Input = board.get_pin('d:7:i')
d8Input = board.get_pin('d:8:i')
d9Input = board.get_pin('d:9:i')
d10Input = board.get_pin('d:10:i')
d11Input = board.get_pin('d:11:i')
d12Input = board.get_pin('d:12:i')
d13Input = board.get_pin('d:13:i')

#define pin Digital Output Arduino
d1Output = board.get_pin('d:1:o')
d2Output = board.get_pin('d:2:o')
d3Output = board.get_pin('d:3:o')
d4Output = board.get_pin('d:4:o')
d5Output = board.get_pin('d:5:o')
d6Output = board.get_pin('d:6:o')
d7Output = board.get_pin('d:7:o')
d8Output = board.get_pin('d:8:o')
d9Output = board.get_pin('d:9:o')
d10Output = board.get_pin('d:10:o')
d11Output = board.get_pin('d:11:o')
d12Output = board.get_pin('d:12:o')
d13Output = board.get_pin('d:13:o')
