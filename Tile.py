import random

class Tile:
	def __init__(self, _x, _y):
		self.value = 2 if random.random() < 0.9 else 4
		self.position = {'x': _x, 'y': _y}
		self.moveTo = {'x': 0, 'y':0}
		self.available =  False
		self.dieOnMerge = False
	
	def move(self, dir):
		if dir == 'l':
			self.position['x'] -= 0.25
		if dir == 'r':
			self.position['x'] += 1
		if dir == 'u':
			self.position['y'] -= 1
		if dir == 'd':
			self.position['y'] += 1
	
	def setMoveTo(self, _x, _y, _die):
		self.moveTo = {'x': _x, 'y':_y}
		self.dieOnMerge = _die
		print(self.position)
		print(self.moveTo)

	def shouldMove(self):
		return self.position != self.moveTo

	def getValue(self):
		return self.value

	def __str__(self):
		return str(self.value)



