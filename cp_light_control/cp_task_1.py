import time 
import board
Analog_in = AnalogIn(board.A1) 


while True:
    print(analog_in.value)
    time.sleep(0.5)

