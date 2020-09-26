
#include <string>
#include <iostream>
#include "Piece.h"
#include <vector>
#include <tuple>
#include <map>
#include "Board.h"
#include <time.h>

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
    generateRandomPosition();

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

    generateRandomPosition();
}

Piece* Board::operator[](int index) {
    if (index < boardSize) {
        return board[index];
    }else {
        throw std::invalid_argument("index out or range");
    }
}

void Board::setAvailablePositions() {
    availablePositions.clear();
    for(int i = 0; i < getSize(); i ++) {
        for(int j = 0; j < getSize(); j ++) {
            if(board[i][j].getValue() == 0) {
                tuple<int, int> aux(i,j);
                availablePositions.push_back(aux);
            }
        }
    }

}

void Board::printAvailablePositions() {
    for(int i = 0; i < availablePositions.size(); i ++) {
        cout << "(" << get<0>(availablePositions[i]) << ", " << get<1>(availablePositions[i]) << ")" << " ";
    }
    cout << endl;
}

tuple<int,int> Board::getRandomPosition() {
    setAvailablePositions();
    srand(time(NULL));
    if(availablePositions.size() > 0) {
        int position = rand() % availablePositions.size();
        tuple<int, int> aux(availablePositions[position]);
        availablePositions.erase(availablePositions.begin() + position);
        return aux;
    }else {
        tuple<int, int> aux(-1, -1);
        return aux;
    }
}

void Board::generateRandomPosition() {
    tuple<int, int> pos(getRandomPosition());
    board[get<0>(pos)][get<1>(pos)].generate();
}

void Board::resetAvaialablePieces() {
    for(int i = 0; i < getSize(); i ++) {
        for(int j = 0; j < getSize(); j ++) {
            board[i][j].setAvailable(true);
        }
    }
}

void Board::mergeLine(int x) {
    bool moved = true;
    while(moved) {
        moved = false;
        for(int i = getSize() - 2; i > -1; i --) {
            if(board[x][i + 1].getValue() == 0 && board[x][i].getValue() != 0) {
                int aux = board[x][i].getValue();
                board[x][i].setValue(board[x][i + 1].getValue());
                board[x][i + 1].setValue(aux);

                bool flag = board[x][i].isAvailable();
                board[x][i].setAvailable(board[x][i].isAvailable());
                board[x][i + 1].setAvailable(flag);
                moved = true;
            }else if(board[x][i + 1].getValue() == board[x][i].getValue() && board[x][i].isAvailable() && board[x][i + 1].isAvailable()) {
                int aux = board[x][i].getValue();
                board[x][i].setValue(0);
                board[x][i + 1].setValue(2 * aux);
                board[x][i].setAvailable(true);
                board[x][i + 1].setAvailable(false);
                moved = true;
            }
        }
    }
    resetAvaialablePieces();
}

void Board::mergeColumn(int y) {
    bool moved = true;
    while(moved) {
        moved = false;
        for(int i = getSize() - 2; i > -1; i --) {
            if(board[i + 1][y].getValue() == 0 && board[i][y].getValue() != 0) {
                int aux = board[i][y].getValue();
                board[i][y].setValue(board[i + 1][y].getValue());
                board[i + 1][y].setValue(aux);

                bool flag = board[i][y].isAvailable();
                board[i][y].setAvailable(board[i][y].isAvailable());
                board[i + 1][y].setAvailable(flag);
                moved = true;
            }else if(board[i + 1][y].getValue() == board[i][y].getValue() && board[i][y].isAvailable() && board[i + 1][y].isAvailable()) {
                int aux = board[i][y].getValue();
                board[i][y].setValue(0);
                board[i + 1][y].setValue(2 * aux);
                board[i][y].setAvailable(true);
                board[i + 1][y].setAvailable(false);
                moved = true;
            }
        }
    }
    resetAvaialablePieces();
}

void Board::moveRight() {
    for(int i = 0; i < getSize(); i ++) {
        mergeLine(i);
    }

    generateRandomPosition();
}
