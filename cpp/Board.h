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
        /*
            TODO:
                - implementar as funções que verificam se o movimento é possível para usar nos movimentadores
                - Só criar peças novas se o movimento foi concretizado (se houve peças movimentadas)
                - Implementar game over
        */
        void moveRight(); 
        void moveLeft(); 
        void moveUp(); 
        void moveDown();
        bool game_over();
        map<string, int> get_counter_movements() { return counterMovements; }
        int get_points();
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
        void mergeLine(int x);
        void mergeColumn(int y);
        void resetAvaialablePieces();
        void rotate_board_by_line();
        void rotate_board_by_column();
	    bool can_move_by_line(int direction); // 1 -> right, 0, left
        bool can_move_by_column(int direction); // 1 -> up, 0 -> down
};


#endif // __BOARD_H__
