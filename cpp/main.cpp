#include <iostream>
#include "Piece.h"
#include <random>
#include <time.h>
#include <tuple>
#include <map>
#include "Board.h"

using namespace std;



int main() {
    // srandom(time(NULL));
    // srand(time(NULL));
    // Piece p(0,0), p1(0,0,4), p3;
    // cout << "Valor: " << p1.getValue() << " " << p.getValue() << endl;
    // p1 = p1 + p;
    // cout << "Valor: " << p1.getValue() << " " << p.getValue() << endl;
    // cout << p3 << endl;

    // tuple<int, int> pos(1,2);
    
    // cout << get<0>(pos) << endl;
    // cout << get<1>(pos) << endl;

    // map<string, int> aux = {
    //     {"up", 8},
    //     {"down", 0},
    //     {"left", 0},
    //     {"right", 0}
    // };
    // cout << aux["up"] << endl;
    // aux["up"] ++;
    // cout << aux["up"] << endl;

    Board b;
    
    cout << b << endl;
    
    b.moveRight();
    cout << b<< endl;
  
    return 0;
}