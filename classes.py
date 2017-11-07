classes.py

class house:

	def __init__(self, x, y, voltage):
		self.x = x
		self.y = y
		self.voltage = voltage
		self.battery_no = None

	def add_battery(self, battery_no):
		self.battery_no = battery_no		


class battery:

	def __init__(self, x, y, min_x, max_x, voltage, d_voltage):	
		x = self.x
		y = self.y
