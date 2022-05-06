import RPi.GPIO as GPIO
from time import sleep
from math import floor
from CONSTANTS import *
from time import sleep


class Motor:
	
	def __init__(self, dirpin, steppin, steps_per_revolution=800):
		# assign parameters
		self.dirpin = dirpin
		self.steppin = steppin
		self.spr = steps_per_revolution
		self.current_angle = 0
		
		# initialize pins
		GPIO.setup(dirpin, GPIO.OUT)
		GPIO.setup(steppin, GPIO.OUT)
		

		# calculate necessary values
		self.calculate_params()

	def dummy_wait(self, angle, direction):
		sleep(5)
		return

	def cleanup(self):
		GPIO.output(self.steppin,GPIO.LOW)



	
	# Given an angle and direction, turns the motor by that amount
	# relative to the current state.
	# Direction given: CW or CCW
	# Angle : in degrees
	# time : in seconds
	# if no time is given, SLEEPTIME from CONSTANTS.py is used
	def turn(self, angle, direction, time=None):
		step_count = floor(angle / self.get_step_angle())

		

		if time:
			print("TIME!!!")
			sleep_dur = time / step_count
		else:
			print("NO TIME!!!")
			sleep_dur = SLEEPTIME

		# set direction here
		GPIO.output(self.dirpin,direction)

		for _ in range(step_count):
			# Set one coil winding to high
			GPIO.output(self.steppin,GPIO.HIGH)
			# Allow it to get there.
			sleep(sleep_dur) # Dictates how fast stepper motor will run1
			# Set coil winding to low
			GPIO.output(self.steppin,GPIO.LOW)
			# sleep(SLEEPTIME) # Dictates how fast stepper motor will run
			
			#sleep(0.1)

			if direction is CW:
				self.current_angle += self.get_step_angle()
			else:
				self.current_angle -= self.get_step_angle()
			

			print("Motor current angle is:", self.current_angle)

		return


	# Turn the motor to the given angle.
	# This is the absolute angle, not the relative.
	def turn_to(self, angle):
		angle_to_turn = angle - self.current_angle
		direction =  CW if angle_to_turn > 0 else CCW
		self.turn(abs(angle_to_turn), direction)


	# Calculate step angle fior given microstep condition
	def calculate_params(self):
		self.step_angle = 360 / self.get_spr()


	# Return the current state of the motor
	def introduce_yourself(self):
		s = "My dirpin is :" + str(self.dirpin) + "\nMy steppin is : " + str(self.get_steppin()) + \
			 "\nMy spr is : " + str(self.get_spr()) + "\nMy step angle is : " + str(self.step_angle) + \
				 "\nMy current angle is : " + str(self.current_angle)
		return s
	
	
	
	# Setters
	def set_spr(self, spr):
		self.spr = spr
		self.step_angle = 360 / spr
	
	
	def set_dirpin(self, dirpin):
		self.dirpin = dirpin
	
	def set_steppin(self, steppin):
		self.steppin = steppin
		

		
	#Getters
	def get_dirpin(self):
		return self.dirpin
	
	def get_steppin(self):
		return self.steppin
		
	def get_spr(self):
		return self.spr

	def get_step_angle(self):
		return self.step_angle
	
	
