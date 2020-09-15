#!/usr/bin/python3
# -*- coding: utf8 -*-

import random


class Piece(object):
	def __init__(self, _x, _y, _value=0):
		super(Piece, self).__init__()
		self.x = _x
		self.y = _y
		self._value = _value
		self.available = True

	def generate(self) -> None:
		self._value = 2 if random.random() < .9 else 4

	@property
	def value(self):
		return self._value
	
	@value.setter
	def value(self, v):
		self._value = v

	def isAvailable(self) -> bool:
		return self.available

	def setAvailable(self, value) -> None:
		self.available = value

	def __add__(self, other):
		self._value += other.value
		other.value = 0
		return self

	def __str__(self) -> str:
		return str(self._value)


# p1 = Piece(1,2,_value=2)
# p2 = Piece(1,2,_value=4)
# p1 = p1 + p2
# print(p1, p2)
