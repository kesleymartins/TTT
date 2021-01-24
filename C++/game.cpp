#include <iostream>

#include "game.h"

using namespace std;

Game::Game()
{
	this->game_loop = true;

	for (int i=0; i<3; ++i)
	{
		for (int j=0; j<3; ++j)
		{
			this->table[i][j] = 0;
		}
	}
}

void Game::show_table() const
{

	system("clear");

	for (int i=0; i<3; ++i)
	{
		for (int j=0; j<3; ++j)
		{
			if (table[i][j] > 0)
				cout << " X ";

			else if (table[i][j] < 0)
				cout << " O ";
			else
				cout << "   ";
			
			if (j != 2)
				cout << "|";
		}

		if (i != 2)
			cout << endl << "-----------";
		cout << endl;
	}
}

void Game::make_move(const int & who)
{
	if (who > 0) 
	{
		p1.set_new_coords(this->table);
		table[p1.get_x()][p1.get_y()] = who; 
	}
	else
	{
		p2.set_new_coords(this->table);
		table[p2.get_x()][p2.get_y()] = who;
	}

	end_game_verifier();
}

void Game::end_game_verifier()
{
	
	// Verify first diagonal
	int dig_01, dig_02, hor_sum, ver_sum;

	dig_01 = 0;
	dig_02 = 0;

	for (int i=0; i<3; ++i)
	{
		ver_sum = 0;
		hor_sum = 0;

		dig_01 += table[i][i];
		dig_02 += table[2-i][i];
		
		for (int j=0; j<3; j++)
		{
			hor_sum += table[i][j];
			ver_sum += table[j][i];
		}

		if (hor_sum == 3 || ver_sum == 3 || hor_sum == -3 || ver_sum == -3)
		{
			this->game_loop = false;
			break;
		}

	}

	if (dig_01 == 3 || dig_02 == 3 || dig_01 == -3 || dig_02 == -3)
		this->game_loop = false;
}