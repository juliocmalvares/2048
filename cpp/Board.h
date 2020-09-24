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
};


#endif // __BOARD_H__