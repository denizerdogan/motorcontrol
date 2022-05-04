from motor import Motor
import threading
from CONSTANTS import *
# import RPi.GPIO as GPIO

def run_sequence(chair: Motor, assembly: Motor):
    chair.turn(45,CW)
    t = threading.Thread(target=run_sequence, args=(chair,assembly))
    t.start()
    t.join()
    print("Thread finished")


def main():
    
    print("Import successful.")
    
    m = Motor(8, 10, 800)



    print(m.introduce_yourself())
    return 0

if __name__ == '__main__':
    main()
