#include "game.h"

int main()
{

	int who = 1;

	Game game;

	while (game.get_game_loop())
	{
		game.show_table();
		game.make_move(who);

		if (who > 0)
			who -= 2;
		else
			who += 2;
	}

	game.show_table();

	return 0;
}