#!/usr/bin/python3
# -*- coding: utf8 -*-

import Piece
import random
from pynput.keyboard import Key, Listener
import os
import pygame
from datetime import datetime
import json


class Board(object):
	def __init__(self):
		super(Board, self).__init__()
		self.board: list = list()
		aux: list = []
		for i in range(4):
			for j in range(4):
				aux.append(Piece.Piece(i, j))
			self.board.append(aux)
			aux = []

		aux: int = 0
		while aux < 2:
			_x: int = random.randint(0, 3)
			_y: int = random.randint(0, 3)
			if self.board[_x][_y].value == 0:
				self.board[_x][_y].generate()
				aux += 1
		self.availablePositions: list = []
		self.counterMovements = {'up': 0, 'down': 0, 'left': 0, 'right': 0}

	def getBoard(self) -> list:
		return self.board

	def points(self) -> int:
		max = 0
		for i in range(len(self.board[0])):
			for j in range(len(self.board[0])):
				if self.board[i][j].value > max:
					max = self.board[i][j].value
		return max

	def getAvaialblePositions(self) -> None:
		self.availablePositions = list()
		for i in range(len(self.board[0])):
			for j in range(len(self.board[0])):
				if self.board[i][j].value == 0:
					self.availablePositions.append((i, j))
		print(self.availablePositions)	
		if len(self.availablePositions) == 0:
			print("Sua pontuação foi {}".format(self.points()))
			print("Game Over")
			print('Seu tabuleiro: ')
			print(self)
			self.serialize()
			exit()

	def serialize(self) -> None:
		save = {}
		b = []
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				b.append(self.board[i][j].value)
		save['board'] = b
		save['movements'] = self.counterMovements
		save['points'] = self.points()
		now = datetime.now()
		with open('./saves/' + now.strftime("%d_%m_%Y%H_%M_%S") + '.json', 'w') as jsf:
			json.dump(save, jsf, ensure_ascii=False, indent=4)

	def generateRandomPosition(self) -> tuple:
		self.getAvaialblePositions()
		if len(self.availablePositions) > 0:
			index: int = random.randint(0, (len(self.availablePositions) - 1))
			return self.availablePositions[index]
		else:
			return (-1, -1)

	def __str__(self) -> str:
		st: str = ''
		for i in range(4):
			for j in range(4):
				st += str(self.board[i][j]) + '\t'
			st += '\n'
		return str(st)

	def generate(self) -> None:
		position = self.generateRandomPosition()
		self.board[position[0]][position[1]].generate()

	def __can_move_hor(self, mov):
		"""
			mov = 1 = right
			mov = -1 = left
		"""
		if mov == -1:
			for lin in range(len(self.board)):
				for col in range(len(self.board[lin]) - 1, -1, -1):
					if col - 1 >= 0:
						if self.board[lin][col].value != 0 and self.board[lin][col - 1].value == 0:
							return True
						elif self.board[lin][col].value == self.board[lin][col - 1].value and self.board[lin][col].value != 0:
							return True
			return False
		if mov == 1:
			for lin in range(len(self.board)):
				for col in range(len(self.board[lin])):
					if col + 1 < len(self.board[lin]):
						if self.board[lin][col].value != 0 and self.board[lin][col + 1].value == 0:
							return True
						elif self.board[lin][col].value == self.board[lin][col + 1].value and self.board[lin][col].value != 0:
							return True
			return False
	def __can_move_ver(self, mov):
		"""
			mov = 1 = Up
			mov = -1 = Down
		"""
		if mov == 1:
			for col in range(len(self.board)):
				for lin in range(len(self.board[col]) - 1, -1, -1):
					if lin - 1 >= 0:
						if self.board[lin][col].value != 0 and self.board[lin - 1][col].value == 0:
							return True
						elif self.board[lin][col].value == self.board[lin - 1][col].value and self.board[lin][col].value != 0:
							return True
			return False
		if mov == -1:
			for col in range(len(self.board)):
				for lin in range(len(self.board[col]) - 1, -1, -1):
					if lin + 1 < len(self.board[col]):
						if self.board[lin][col].value != 0 and self.board[lin + 1][col].value == 0:
							return True
						elif self.board[lin][col].value == self.board[lin + 1][col].value and self.board[lin][col].value != 0:
							return True
			return False

	def move_up(self) -> None:
		print(self.__can_move_ver(1))
		if self.__can_move_ver(1):
			self.board = self.board[::-1]
			for i in range(len(self.board[0])):
				self.mergeColumn(i)
			self.board = self.board[::-1]

			position = self.generateRandomPosition()
			self.board[position[0]][position[1]].generate()
			self.counterMovements['up'] += 1

	def move_down(self) -> None:
		print(self.__can_move_ver(-1))
		if self.__can_move_ver(-1):
			for i in range(len(self.board[0])):
				self.mergeColumn(i)

			position = self.generateRandomPosition()
			self.board[position[0]][position[1]].generate()
			self.counterMovements['down'] += 1

	def move_right(self) -> None:
		print(self.__can_move_hor(1))
		if self.__can_move_hor(1):
			for i in range(len(self.board[0])):
				self.mergeLine(i)
			position = self.generateRandomPosition()
			self.board[position[0]][position[1]].generate()
			self.counterMovements['right'] += 1

	def move_left(self) -> None:
		print(self.__can_move_hor(-1))
		if self.__can_move_hor(-1):
			for i in range(len(self.board)):
				self.board[i] = self.board[i][::-1]
			for i in range(len(self.board[0])):
				self.mergeLine(i)
			for i in range(len(self.board)):
				self.board[i] = self.board[i][::-1]
			position = self.generateRandomPosition()
			self.board[position[0]][position[1]].generate()
			self.counterMovements['left'] += 1

	def mergeColumn(self, y: int) -> None:
		moved = True
		while(moved):
			moved = False
			for i in range(len(self.board[0]) - 2, -1, -1):
				if (self.board[i+1][y].value == 0 and self.board[i][y].value != 0):
					self.board[i][y].value, self.board[i +
													   1][y].value = self.board[i+1][y].value, self.board[i][y].value
					aux = self.board[i][y].isAvailable()
					self.board[i][y].setAvailable(
						self.board[i+1][y].isAvailable())
					self.board[i + 1][y].setAvailable(aux)
					moved = True
				elif(self.board[i+1][y].value == self.board[i][y].value and self.board[i+1][y].isAvailable() and self.board[i][y].isAvailable()):
					self.board[i][y].value, self.board[i +
													   1][y].value = 0, 2*self.board[i][y].value
					self.board[i][y].setAvailable(True)
					self.board[i + 1][y].setAvailable(False)
					moved = True
		self.__resetAvailable()

	def mergeLine(self, x: int) -> None:
		moved = True
		while(moved):
			moved = False
			for i in range(len(self.board[0]) - 2, -1, -1):
				if (self.board[x][i+1].value == 0 and self.board[x][i].value != 0):
					self.board[x][i].value, self.board[x][i +
														  1].value = self.board[x][i+1].value, self.board[x][i].value
					aux = self.board[x][i].isAvailable()
					self.board[x][i].setAvailable(
						self.board[x][i+1].isAvailable())
					self.board[x][i + 1].setAvailable(aux)
					moved = True
				elif(self.board[x][i+1].value == self.board[x][i].value and self.board[x][i + 1].isAvailable() and self.board[x][i].isAvailable()):
					self.board[x][i].value, self.board[x][i +
														  1].value = 0, 2*self.board[x][i].value
					self.board[x][i].setAvailable(True)
					self.board[x][i + 1].setAvailable(False)
					moved = True
		self.__resetAvailable()

	def __resetAvailable(self) -> None:
		for i in range(4):
			for j in range(4):
				self.board[i][j].setAvailable(True)
	
	def isOver(self):
		if not self.__can_move_hor(1) and not self.__can_move_hor(-1) and not self.__can_move_ver(1) and not self.__can_move_ver(-1):
			return True
		return False