from easystep.motor import Motor
import threading
from CONSTANTS import *
import RPi.GPIO as GPIO

def run_sequence(chair: Motor, assembly: Motor):
    # Turn chair 45 cw
    t1 = threading.Thread(target=chair.turn, args=(120, CW, 20))
    t1.start()

    t2 = threading.Thread(target=assembly.turn, args=(120, CW, 20))
    t2.start()

    t1.join()
    t2.join()
    print("Threads finished")

def seq2test(chair: Motor):
    t1 = threading.Thread(target=chair.turn_to, args=(0,20))
    t1.start()




def main():
    GPIO.setmode(GPIO.BOARD)
    
    print("Import successful.")
    
    m1 = Motor(10, 8, 800)
    m2 = Motor(18, 16, 1600)

    run_sequence(m1, m2)
    seq2test(m1)
    seq2test(m2)
    




    print(m1.introduce_yourself())

    m1.cleanup()
    m2.cleanup()
    return 0

if __name__ == '__main__':
    main()
