import board 

lightsensor = AnalogIn(board.A1)

LED = AnalogOut(board.A0)

while True:
   light = lightsensor.value
   LED.value = light 
   time.sleep(0.1)
