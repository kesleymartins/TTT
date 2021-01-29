#ifndef GAME_H
#define GAME_H

#include "player.h"

class Game
{
private:
	int table[3][3];
	bool game_loop;

	Player p1, p2;

	void end_game_verifier();

public:
	// Constructor and Destructor
	Game();

	// Acessors
	inline const bool & get_game_loop() { return this->game_loop; }

	// Modifiers

	// Functions
	void show_table() const;
	void make_move(const int & who);

};

#endif