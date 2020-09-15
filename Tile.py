import random

class Tile:
	velocidade = 0.25

	def __init__(self, _x, _y):
		_x = _x*1.0
		_y = _y*1.0
		self.value = 2 if random.random() < 0.9 else 4
		self.position = {'x': _x, 'y': _y}
		self.moveTo = {'x': _x, 'y': _y}
		self.available =  False
		self.dieOnMerge = False
	
	def move(self, dir):
		if dir == 'l':
			self.position['x'] -= Tile.velocidade
		if dir == 'r':
			self.position['x'] += Tile.velocidade
		if dir == 'u':
			self.position['y'] -= Tile.velocidade
		if dir == 'd':
			self.position['y'] += Tile.velocidade
	
	def setMoveTo(self, _x, _y, _die):
		self.moveTo = {'x': _x, 'y':_y}
		self.dieOnMerge = _die
		print(self.position)
		print(self.moveTo)

	def shouldMove(self):
		if self.position != self.moveTo: return True
		return False

	def getValue(self):
		return self.value

	def getPosition(self):
		return self.position
	
	def getMoveTo(self):
		return self.moveTo

	def __str__(self):
		return str(self.value)



