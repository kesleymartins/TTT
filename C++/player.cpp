#include <iostream>
#include <iomanip>

#include "player.h"

using namespace std;

int Player::get_input(const char & c)
{
	int new_coord;
	
	cout << "Insira o valor de " << c << ": ";
	cin >> new_coord;

	while (!cin.good())
	{
		cout << "Entrada Invalida!" << endl;

		cin.clear();
		cin.ignore(INT64_MAX, '\n');
		
		cout << "Insira o valor de " << c << ": ";
		cin >> new_coord;
	}

	cin.clear();
	cin.ignore(INT64_MAX, '\n');

	return new_coord;

}

void Player::set_new_coords(const int table[3][3])
{

	do
	{
		do
		{
			this->coord_x = get_input('X');
		}
		while(this->coord_x < 1 || this->coord_x > 3);
		
		do
		{
			this->coord_y = get_input('Y');
		} 
		while(this->coord_y < 1 || this->coord_y > 3);

		this->coord_x--;
		this->coord_y--;
	}
	while(table[this->coord_x][this->coord_y] != 0);
}