import RPi.GPIO as GPIO
from time import sleep

# Direction pin from controller
DIR = 10
# Step pin from controller
STEP = 8
# 0/1 used to signify clockwise or counterclockwise.
CW = 1
CCW = 0

sleeptime = .004

STEP2 = 16
DIR2 = 18

# Setup pin layout on PI
GPIO.setmode(GPIO.BOARD)

# Establish Pins in software
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)

# Set the first direction you want it to spin
GPIO.output(DIR, CCW)
GPIO.output(DIR2,CCW)

try:
	# Run forever.

	"""Change Direction: Changing direction requires time to switch. The
	time is dictated by the stepper motor and controller. """
	sleep(1.0)
	# Esablish the direction you want to go
	GPIO.output(DIR,CW)
	GPIO.output(DIR2,CW)
	

	# Run for 200 steps. This will change based on how you set you controller
	for x in range(400):

		# Set one coil winding to high
		GPIO.output(STEP,GPIO.HIGH)
		# Allow it to get there.
		sleep(sleeptime) # Dictates how fast stepper motor will run1
		# Set coil winding to low
		GPIO.output(STEP,GPIO.LOW)
		sleep(sleeptime) # Dictates how fast stepper motor will run
		
					# Set one coil winding to high
		# GPIO.output(STEP2,GPIO.HIGH)
		# # Allow it to get there.
		# sleep(sleeptime) # Dictates how fast stepper motor will run1
		# # Set coil winding to low
		# GPIO.output(STEP2,GPIO.LOW)
		# sleep(sleeptime) # Dictates how fast stepper motor will run
		
		
		
	
	print('Saat yonunde 90')
		
	GPIO.output(DIR,CCW)
	GPIO.output(DIR2,CCW)
	
		
			# Run for 200 steps. This will change based on how you set you controller
	for x in range(400):

		# Set one coil winding to high
		GPIO.output(STEP,GPIO.HIGH)
		# Allow it to get there.
		sleep(sleeptime) # Dictates how fast stepper motor will run1
		# Set coil winding to low
		GPIO.output(STEP,GPIO.LOW)
		sleep(sleeptime) # Dictates how fast stepper motor will run
		
					# # Set one coil winding to high
		# GPIO.output(STEP2,GPIO.HIGH)
		# # Allow it to get there.
		# sleep(sleeptime) # Dictates how fast stepper motor will run1
		# # Set coil winding to low
		# GPIO.output(STEP2,GPIO.LOW)
		# sleep(sleeptime) # Dictates how fast stepper motor will run
		
		
		
		
	print('HOME')
		
	
	for x in range(400):

		# Set one coil winding to high
		GPIO.output(STEP,GPIO.HIGH)
		# Allow it to get there.
		sleep(sleeptime) # Dictates how fast stepper motor will run1
		# Set coil winding to low
		GPIO.output(STEP,GPIO.LOW)
		sleep(sleeptime) # Dictates how fast stepper motor will run
		
					# # Set one coil winding to high
		# GPIO.output(STEP2,GPIO.HIGH)
		# # Allow it to get there.
		# sleep(sleeptime) # Dictates how fast stepper motor will run1
		
		
		# # Set coil winding to low
		# GPIO.output(STEP2,GPIO.LOW)
		# sleep(sleeptime) # Dictates how fast stepper motor will run
		
		
		
		
		
	# GPIO.output(DIR,CW)
	# GPIO.output(DIR2,CW)  
	
	# print('Terse 90')
	
			# # Run for 200 steps. This will change based on how you set you controller
	# for x in range(400):

		# # Set one coil winding to high
		# GPIO.output(STEP,GPIO.HIGH)
		# # Allow it to get there.
		# sleep(.001) # Dictates how fast stepper motor will run1
		# # Set coil winding to low
		# GPIO.output(STEP,GPIO.LOW)
		# sleep(.001) # Dictates how fast stepper motor will run
		
					# # Set one coil winding to high
		# GPIO.output(STEP2,GPIO.HIGH)
		# # Allow it to get there.
		# sleep(.005) # Dictates how fast stepper motor will run1
		# # Set coil winding to low
		# GPIO.output(STEP2,GPIO.LOW)
		# sleep(.005) # Dictates how fast stepper motor will run
		
		
		# sleep(.003)
		
		
	# print('HOME')



# Once finished clean everything up
except KeyboardInterrupt:
	print("cleanup")
	GPIO.cleanup()
