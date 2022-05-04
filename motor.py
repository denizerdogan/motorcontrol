import RPi.GPIO as GPIO
from time import sleep

class Motor:
	
	def __init__(self, dirpin, steppin, steps_per_revolution=800):
		self.dirpin = dirpin
		self.steppin = steppin
		self.spr = steps_per_revolution
	
	
	
	# Setters
	def set_spr(self, spr):
		self.spr = spr
	
	
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
	
	
