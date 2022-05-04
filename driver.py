from motor import Motor
import threading
from CONSTANTS import *
import RPi.GPIO as GPIO

def run_sequence(chair: Motor, assembly: Motor):
    # Turn chair 45 cw
    t1 = threading.Thread(target=chair.turn, args=(180, CW))
    t1.start()

    t2 = threading.Thread(target=chair.turn, args=(180, CW))
    t2.start()

    t1.join()
    t2.join()
    print("Threads finished")


def main():
    GPIO.setmode(GPIO.BOARD)
    
    print("Import successful.")
    
    m1 = Motor(10, 8, 800)
    m2 = Motor(18, 16, 800)

    run_sequence(m1, m2)
    




    print(m.introduce_yourself())
    return 0

if __name__ == '__main__':
    main()
