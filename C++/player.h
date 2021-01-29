#ifndef PLAYER_H
#define PLAYER_H

class Player
{
private:
	int coord_x, coord_y;

	const int get_input(const char & c);

public:

	// Acessor
	inline const int & get_x() { return this->coord_x; }
	inline const int & get_y() { return this->coord_y; }

	// Modifiers 
	void set_new_coords(const int table[3][3]);
};

#endif