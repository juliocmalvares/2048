
#include <string>
#include <iostream>
#include "Piece.h"
#include <vector>
#include <tuple>
#include <map>
#include "Board.h"

Board::Board() {
    boardSize = 4;
    board = (Piece**)malloc(boardSize * sizeof(Piece*));
    for(int lin = 0; lin < 4; lin ++) {
        board[lin] = (Piece*)malloc(boardSize * sizeof(Piece));
        for(int col = 0; col < 4; col ++) {
            board[lin][col] = Piece(lin, col, 0);
        }
    }

    counterMovements = {
        {"up", 0},
        {"down", 0},
        {"left", 0},
        {"right", 0}
    };
}

Board::Board(int _boardSize) {
    boardSize = _boardSize;
    board = (Piece**)malloc(boardSize * sizeof(Piece*));
    for(int lin = 0; lin < 4; lin ++) {
        board[lin] = (Piece*)malloc(boardSize * sizeof(Piece));
        for(int col = 0; col < 4; col ++) {
            board[lin][col] = Piece(lin, col, 0);
        }
    }
    
    counterMovements = {
        {"up", 0},
        {"down", 0},
        {"left", 0},
        {"right", 0}
    };
}

Piece* Board::operator[](int index) {
    if (index < boardSize) {
        return board[index];
    }else {
        throw std::invalid_argument("index out or range");
    }
}