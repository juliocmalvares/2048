#ifndef __PIECE_H__
#define __PIECE_H__

#include <string>
#include <iostream>
using namespace std;

class Piece {
    public:
        Piece();
        Piece(int _x, int _y);
        Piece(int _x, int _y, int _value);
        Piece(const Piece &other);
        virtual ~Piece();
        Piece operator+(Piece &other);
        int getValue() const { return value; }
        int getX() const { return x; }
        int getY() const { return y; }
        bool isAvailable() const { return available; }
        std::string toString();
        void setValue(int _value);
        void setX(int _x);
        void setY(int _y);
        void setAvailable(bool condition);
    private:
        friend ostream &operator<<(ostream &out, const Piece  &p) {
            out << p.getValue();
            return out;
        }
        int x, y, value;
        bool available;
};

#endif // __PIECE_H__