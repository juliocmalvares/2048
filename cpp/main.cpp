#include <iostream>
#include "Piece.h"
#include <random>
#include <time.h>
#include <tuple>
#include <map>
#include "Board.h"

using namespace std;

int main() {

    Board b;
   	cout << "Original" << endl;
	cout << b << endl << endl;  

    int counter = 0;

    random_device dev;
    mt19937 rng(dev());
    uniform_int_distribution<mt19937::result_type> dist4(0, 3);

    while(b.game_over() == false) {
        int move = dist4(rng);
        cout << move << " ";
        switch(move) {
            case 0:
                b.moveUp();
                cout << b << endl;
                counter++;
                break;
            case 1:
                b.moveDown();
                cout << b << endl;
                counter++;
                break;
            case 2:
                b.moveLeft();
                cout << b << endl;
                counter++;
                break;
            case 3:
                b.moveRight();
                cout << b << endl;
                counter++;
                break;
        }
    }
    cout << " >> Counter movements << " << endl;
    cout << "Movimentos tentados: " << counter << endl;
    cout << "left: " << b.get_counter_movements()["left"] << endl;
    cout << "right: " << b.get_counter_movements()["right"] << endl;
    cout << "up: " << b.get_counter_movements()["up"] << endl;
    cout << "down: " << b.get_counter_movements()["down"] << endl << endl;
    cout << "Points: " << b.get_points() << endl;


    return 0;
}
