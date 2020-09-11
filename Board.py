#!/usr/bin/python3
# -*- coding: utf8 -*-

import Piece
import random
from pynput.keyboard import Key, Listener
import os
import pygame

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

    def getBoard(self) -> list:
        return self.board
        
    def getAvaialblePositions(self) -> None:
        self.availablePositions = list()
        max = 0
        for i in range(len(self.board[0])):
            for j in range(len(self.board[0])):
                if self.board[i][j].value > max:
                    max = self.board[i][j].value
                if self.board[i][j].value == 0:
                    self.availablePositions.append((i, j))
        if len(self.availablePositions) == 0:
            print("Sua pontuação foi {}".format(max))
            print("Game Over")
            print('Seu tabuleiro: ')
            print(self)
            exit()

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

    def _merge_column_up(self, _y: int) -> None:
        flag = True
        while flag:
            flag = False
            for i in range(4):
                j = i
                while i > 0:
                    if (self.board[j][_y].value != 0) and (self.board[j - 1][_y].value == 0):
                        self.board[j - 1][_y].value = self.board[j][_y].value
                        self.board[j][_y].value = 0
                        flag = True
                    elif (self.board[j][_y].value != 0) and (self.board[j - 1][_y].value != 0):
                        if (self.board[j][_y].value == self.board[j - 1][_y].value) and (self.board[j][_y].isAvailable() and self.board[j - 1][_y].isAvailable()):
                            self.board[j - 1][_y].value = self.board[j][_y].value + \
                                self.board[j - 1][_y].value
                            self.board[j][_y].value = 0
                            self.board[j][_y].setAvailable(False)
                            self.board[j - 1][_y].setAvailable(False)
                            flag = True
                    i -= 1

    def generate(self):
        position = self.generateRandomPosition()
        self.board[position[0]][position[1]].generate()


    def move_up(self) -> None:
        self.board = self.board[::-1]
        for i in range(len(self.board[0])):
            self.mergeColumn(i)
        self.board = self.board[::-1]
        position = self.generateRandomPosition()
        self.board[position[0]][position[1]].generate()

    def move_down(self) -> None:
        for i in range(len(self.board[0])):
            self.mergeColumn(i)
        position = self.generateRandomPosition()
        self.board[position[0]][position[1]].generate()

    def move_right(self) -> None:
        for i in range(len(self.board[0])):
            self.mergeLine(i)
        position = self.generateRandomPosition()
        self.board[position[0]][position[1]].generate()

    def move_left(self) -> None:
        # self.board = self.board[::-1]
        for i in range(len(self.board)):
            self.board[i] = self.board[i][::-1]
        for i in range(len(self.board[0])):
            self.mergeLine(i)
        for i in range(len(self.board)):
            self.board[i] = self.board[i][::-1]
        # self.board = self.board[::-1]
        position = self.generateRandomPosition()
        self.board[position[0]][position[1]].generate()

    def mergeColumn(self, y):
        moved = True
        while(moved):
            moved = False
            for i in range(len(self.board[0]) - 2, -1, -1):
                if (self.board[i+1][y].value == 0 and self.board[i][y].value != 0):
                    self.board[i][y].value, self.board[i + 1][y].value = self.board[i+1][y].value, self.board[i][y].value
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

    def mergeLine(self, x):
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

b = Board()
print(b)
# b.move_down()
# print(b)
# # while True:
# #     print(b)
# #     input()
# #     b.move_up()


# def on_press(key):
#     # print('{0} pressed'.format(
#     #     key))
#     os.system('clear')
#     print("Pressed: ", key)
#     if key == Key.left:
#         b.move_left()
#         b.generate()
#     if key == Key.up:
#         b.move_up()
#         b.generate()
#     if key == Key.down:
#         b.move_down()
#         b.generate()
#     if key == Key.right:
#         b.move_right()
#         b.generate()
#     print(b)


# def on_release(key):
#     if key == Key.esc:
#         # Stop listener
#         return False


# # Collect events until released
# with Listener(on_press=on_press,
#               on_release=on_release) as listener:
#     listener.join()
