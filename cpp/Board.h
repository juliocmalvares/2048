#ifndef __BOARD_H__
#define __BOARD_H__

#include <string>
#include <iostream>
#include "Piece.h"
#include <vector>
#include <tuple>
#include <map>

class Board {
    public:
        Board();
        Board(int _boardSize);
        Piece* operator[](int index);
        int getSize() { return boardSize; }
        void setAvailablePositions();
        vector<tuple<int, int>> getAvailablePositions() { return availablePositions; }
        void printAvailablePositions();
        tuple<int, int> getRandomPosition();
        void generateRandomPosition();
        void moveRight();
        void moveLeft(); //finish
        void moveUp(); //finish
        void moveDown(); //finish
    private:
        Piece **board;
        int boardSize;
        vector<tuple<int, int>> availablePositions;
        map<string,int> counterMovements;

        friend ostream &operator<<(ostream &out, const Board  &b) {
            for(int lin = 0; lin < 4; lin ++) {
                for(int col = 0; col < 4; col ++) {
                    out << b.board[lin][col] << "\t";
                }
                out << std::endl;
            }
            return out;
        }
        void rotateBoard(); //finish
        void mergeLine(int x);
        void mergeColumn(int y);
        void resetAvaialablePieces();
};


#endif // __BOARD_H__