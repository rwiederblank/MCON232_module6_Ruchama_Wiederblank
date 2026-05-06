from food import Food
from snake import Snake
from scoreboard import Scoreboard
from game_controller import GameController


snake = Snake()
scoreboard = Scoreboard()
food = Food()
game_controller = GameController(snake, food, scoreboard)
game_controller.run_game_loop()