import pygame
from pygame.locals import *
import sys
import os
import math
from Tile import Tile
map = [[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1]]
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

	def move(self):
		for i in range(4): #line
			for j in range(4): #column
				if type(self.gameState[i][j]) != type(None):
					self.gameState[i][j].setMoveTo( 3, i , False)
		

	def on_event(self, event):
		if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
			self._running = False
		if event.type == KEYDOWN:
			if event.key == pygame.K_RIGHT:
				self.tile['x'] += 1
			if event.key == pygame.K_LEFT:
				#self.tile['x'] -= 1
				self.move()
			if event.key == pygame.K_UP:
				self.tile['y'] -= 1
			if event.key == pygame.K_DOWN:
				self.tile['y'] += 1

	def on_loop(self):
		for lin in range(4):
			for col in range(4):
				if type(self.gameState[lin][col]) != type(None):
					print(self.gameState[lin][col].shouldMove())
					pass

	
	def on_render(self):
		pygame.display.flip()
		self._display.blit(self.background, (0,0))
		for lin in range(4):
			for col in range(4):
				if type(self.gameState[lin][col]) != type(None):
					self._display.blit(self.tileImage[self.gameState[lin][col].getValue()], (self.tileGap*(col+1) + col*self.tileArea, (lin+1)* self.tileGap + lin*self.tileArea))
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

			FPS.tick(30)
		self.on_cleanup()
 
if __name__ == "__main__" :
	theApp = App()
	theApp.on_execute()