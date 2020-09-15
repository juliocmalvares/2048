import pygame
from pygame.locals import *
import sys
import os
from math import *
from Tile import Tile
map = [[0,0,0,1],[0,0,1,1],[0,1,0,1],[1,0,0,1]]
class App:
	def __init__(self):
		self._running = True
		self._display = None
		self.size = [400, 400]
		self.gameState = []
		self.tileImage = {}
		self.tileGap = 8
		self.tileArea = 90
		self.animating = False
		
	def on_init(self):
		print("Starting . . .")
		pygame.init()
		self._display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		self._running = True

		for i in range(4):
			line = []
			for j in range(4):
				if map[i][j] == 1:
					tile = Tile(j, i)
					line.append(tile)
				else:
					line.append(None)
			self.gameState.append(line)


		pygame.display.set_caption("2048")
		self.background = pygame.image.load(os.path.join('images', 'Board.png'))

		for i in range(1, 12):
			self.tileImage[2**i] = pygame.image.load(os.path.join('images',str(2**i)+'.png')).convert_alpha()

	def move(self, dir):
		if dir == 'l':
			for lin in range(4): #line
				for col in range(4): #column
					if type(self.gameState[lin][col]) != type(None):
						self.gameState[lin][col].setMoveTo( 0, lin  , False)
		elif dir == 'r':
			for lin in range(4): #line
				for col in range(4): #column
					if type(self.gameState[lin][col]) != type(None):
						self.gameState[lin][col].setMoveTo( 3, lin  , False)
		elif dir == 'u':
			for lin in range(4): #line
				for col in range(4): #column
					if type(self.gameState[lin][col]) != type(None):
						self.gameState[lin][col].setMoveTo( col, 0  , False)
		elif dir == 'd':
			for lin in range(4): #line
				for col in range(4): #column
					if type(self.gameState[lin][col]) != type(None):
						self.gameState[lin][col].setMoveTo( col, 3  , False)
		

	def on_event(self, event):
		if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
			self._running = False
		if event.type == KEYDOWN:
			if event.key == pygame.K_RIGHT:
				self.move('r')
			if event.key == pygame.K_LEFT:
				#self.tile['x'] -= 1
				self.move('l')
			if event.key == pygame.K_UP:
				self.move('u')
			if event.key == pygame.K_DOWN:
				self.move('d')
	
	def drawTile(self, tile: Tile):
		line = tile.position['y']
		column = tile.position['x']
		value = tile.getValue()
		lineGap = floor((floor(line)+1) * self.tileGap + line*self.tileArea)
		columnGap = floor((floor(column) + 1) * self.tileGap + column * self.tileArea)
		self._display.blit(self.tileImage[value], (columnGap, lineGap ))


	def on_loop(self):
		self.animating = False
		for lin in range(4):
			for col in range(4):
				tile = self.gameState[lin][col]

				if type(tile) != type(None):
					print(f'{lin} {col} {tile.shouldMove()}')
					if tile.shouldMove():
						if tile.position['x'] > tile.moveTo['x']:
							tile.move('l')
						if tile.position['x'] < tile.moveTo['x']:
							tile.move('r')
						if tile.position['y'] > tile.moveTo['y']:
							tile.move('u')
						if tile.position['y'] < tile.moveTo['y']:
							tile.move('d')
						self.animating = True
		
						
	
	def on_render(self):
		pygame.display.flip()
		self._display.blit(self.background, (0,0))
		for lin in range(4):
			for col in range(4):
				if type(self.gameState[lin][col]) != type(None):
					self.drawTile(self.gameState[lin][col])
		pygame.display.update() 
			

	
	def on_cleanup(self):
		print("Ending . . . ")
		pygame.quit()
		sys.exit()
 
	def on_execute(self):
		if self.on_init() == False:
			self._running = False
 
		while( self._running ):
			FPS = pygame.time.Clock()
			if not self.animating:					
				for event in pygame.event.get():
					self.on_event(event)

			self.on_loop()

			self.on_render()

			FPS.tick(60)
		self.on_cleanup()
 
if __name__ == "__main__" :
	theApp = App()
	theApp.on_execute()
