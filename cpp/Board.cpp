#include <string>
#include <iostream>
#include "Piece.h"
#include <vector>
#include <tuple>
#include <map>
#include "Board.h"
#include <time.h>
#include <stdexcept>

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
	if(can_move_by_line(1)) {
    		for(int i = 0; i < getSize(); i ++) {
        		mergeLine(i);
    		}
   		generateRandomPosition();
		counterMovements["right"] ++;
		cout << "Moved right" << endl;
	}else{
		cout << "Not Moved right" << endl;
	}
}

void Board::moveLeft() {
	if(can_move_by_line(0)) {
		rotate_board_by_line();
    		for(int i = 0; i < getSize(); i ++) {
			mergeLine(i);
   		 }
    		rotate_board_by_line();
    		generateRandomPosition();
    		counterMovements["left"] ++;
		cout << "Moved Left " << endl;
	}else {
		cout << "Not Moved left " << endl;
	}
}

void Board::moveUp() {

	if(can_move_by_column(1)) {
    		rotate_board_by_column();
    		for(int i = 0; i < getSize(); i ++) {
	    		mergeColumn(i);
    		}
    		rotate_board_by_column();
		generateRandomPosition();
		counterMovements["up"] ++;
		cout << "Moved up" << endl;
	}else {
		cout << "Not moved up" << endl;
	}
}

void Board::moveDown() {
	if(can_move_by_column(0)) {
		for(int i = 0; i < getSize(); i ++) {
	   		mergeColumn(i);
		}
		generateRandomPosition();
    		counterMovements["down"] ++;
		cout << "Moved Down" << endl;
	}else {
		cout << "Not moved down " << endl;
	}
}


void Board::rotate_board_by_line() {

	int aux[getSize()][getSize()];
	for(int i = 0; i < getSize(); i++) {
		for(int j = getSize() - 1; j >= 0; j--) {
			aux[i][j] = board[i][getSize() - j - 1].getValue();
		}
	}

	for(int i = 0; i < getSize(); i++) {
		for(int j = 0; j < getSize(); j++) {
			board[i][j].setValue(aux[i][j]);
		}
	}
}

void Board::rotate_board_by_column() {

	int aux[getSize()][getSize()];
	for(int i = 0; i < getSize(); i++) {
		for(int j = getSize() - 1; j >= 0; j--) {
			aux[j][i] = board[getSize() - j - 1][i].getValue();
		}
	}

	for(int i = 0; i < getSize(); i++) {
		for(int j = 0; j < getSize(); j++) {
			board[j][i].setValue(aux[j][i]);
		}
	}
}

bool Board::can_move_by_line(int direction) {
	//1 -> right
	//0 -> left
	if(direction == 0) {
		for(int lin = 0; lin < getSize(); lin++){
			for(int col = getSize() - 1; col > -1; col--) {
				if (col - 1 >= 0) {
					if(board[lin][col].getValue() != 0 && board[lin][col - 1].getValue() == 0) return true;
					else if(board[lin][col].getValue() == board[lin][col - 1].getValue() && board[lin][col].getValue() != 0) return true;
				}
			}
		}
		return false;
	}else if(direction == 1) {
		for(int lin = 0; lin < getSize(); lin++){
                        for(int col = 0; col < getSize(); col++) {
                                if (col + 1 < getSize()) {
                                        if(board[lin][col].getValue() != 0 && board[lin][col + 1].getValue() == 0) return true;
                                        else if(board[lin][col].getValue() == board[lin][col + 1].getValue() && board[lin][col].getValue() != 0) return true;
                                }
                        }
                }
                return false;
	}else{
		throw std::invalid_argument("Direction must be 1 or 0");
	}
}


bool Board::can_move_by_column(int direction) {
        //1 -> right
        //0 -> left
        if(direction == 0) {
                for(int lin = 0; lin < getSize(); lin++){
                        for(int col = getSize() - 1; col > -1; col--) {
                                if (col - 1 >= 0) {
                                        if(board[col][lin].getValue() != 0 && board[col - 1][lin].getValue() == 0) return true;
                                        else if(board[col][lin].getValue() == board[col - 1][lin].getValue() && board[col][lin].getValue() != 0) return true;
                                }
                        } 
                }
                return false;
        }else if(direction == 1) {
                for(int lin = 0; lin < getSize(); lin++){
                        for(int col = 0; col < getSize(); col++) {
                                if (col + 1 < getSize()) {
                                        if(board[col][lin].getValue() != 0 && board[col + 1][lin].getValue() == 0) return true;
                                        else if(board[col][lin].getValue() == board[col + 1][lin].getValue() && board[col][lin].getValue() != 0) return true;
                                }
                        }
                }
                return false;
        }else{
                throw std::invalid_argument("Direction must be 1 or 0");
        }
}


bool Board::game_over() {
    if(!can_move_by_column(0) && !can_move_by_column(1) && !can_move_by_line(0) && !can_move_by_line(1)) return true;
    return false;
}

int Board::get_points() {
    int max = 0;
    for(int lin = 0; lin < getSize(); lin++){
        for(int col = 0; col < getSize(); col++) {
            if (board[lin][col].getValue() > max) max = board[lin][col].getValue();
        }
    }
    return max;
}