#include "Piece.h"
#include <stdlib.h>
#include <iostream>
#include <stdexcept>
#include <string>
#include <random>
#include <time.h>

double _rand(){
    srand(time(NULL));
    return double(rand()/ double(RAND_MAX));
}

Piece::Piece() {
    value = (_rand() < .9) ? 2: 4;
    x = y = 0;
    available = true;
}

Piece::Piece(int _x, int _y) {
    value = (_rand() < .9) ? 2: 4;
    x = _x;
    y = _y;
    available = true;
}

Piece::Piece(int _x, int _y, int _value) {
    x = _x;
    y = _y;
    value = _value;
    available = true;
}

Piece::Piece(const Piece &other) {
    x = other.getX();
    y = other.getY();
    value = other.getValue();
    available = true;
}

Piece::~Piece() {
    //just use if class have pointers
}

std::string Piece::toString() {
    return "";
}

void Piece::setAvailable(bool condition) {
    available = condition;
}

void Piece::setX(int _x) {
    x = _x;
}

void Piece::setY(int _y) {
    y = _y;
}

void Piece::setValue(int _value) {
   /* if (_value % 2 == 0 || _value == 0){
        value = _value;
    }else {
        throw std::invalid_argument("Value must be divisible by 2");
    }*/
	value = _value;
}

Piece Piece::operator+(Piece &other) {
    Piece aux(other);
    aux.setValue(value + other.getValue());
    other.setValue(0);
    return aux;
}

void Piece::generate() {
    value = (_rand() < .9) ? 2: 4;
}

	
	
