# minimax-tictactoe

This program allows the user to play the game of Tic Tac Toe with different types of opponents, and on a board with custom size. It utilizes the minimax algorithm with optional alpha-beta pruning to create an intelligent bot player. It also allows to carry out simulations of games between bots with different parameters.

User can launch the game by running the game.py file:  
`python3 .\game.py`  
By default the game is played between a human and a bot with minimax enabled.
User can customize the game by providing one or more of the optional parameters:  
- `--size` - define the size of the board and length of a streak required to win by providing values for rows, columns and streak
- `--opponent` - define type of opponent by chosing one of the options: minimax, random, human
- `--square` - define custom size of a single square on the board
- `--theme` - choose one of the color themes predefined in themes.json by providing it's name

Example of a game launching command with custom properties:  
`python3 .\game.py  --size 5 5 4 --opponent random --square 100 --theme alien`

### A demo game between a random bot (as X) and minimax bot (as O)
![minimax](https://user-images.githubusercontent.com/74139325/152865440-f198fd93-1e0b-43f7-bd36-26e884a8b41d.gif)

### Users can try out one of the included color themes, or easily add their own
![themes](https://user-images.githubusercontent.com/74139325/152865453-2e5877a8-905b-4747-a595-65133257c24e.png)
