#ifndef PLAYER_H
#define PLAYER_H

class Player
{
private:
	int coord_x, coord_y;

	int get_input(const char & c);

public:

	// Acessor
	int & get_x() { return this->coord_x; }
	int & get_y() { return this->coord_y; }

	// Modifiers 
	void set_new_coords(const int table[3][3]);
};

#endif