from motor import Motor
import threading
from CONSTANTS import *
import RPi.GPIO as GPIO

def run_sequence(chair: Motor, assembly: Motor):
    chair.turn(180,CW)

    print("Thread finished")


def main():
    GPIO.setmode(GPIO.BOARD)
    
    print("Import successful.")
    
    m = Motor(10, 8, 800)
    
    t = threading.Thread(target=run_sequence, args=(m,m))
    t.start()
    t.join()



    print(m.introduce_yourself())
    return 0

if __name__ == '__main__':
    main()
