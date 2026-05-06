import time

from food import Food
from snake import Snake
from scoreboard import Scoreboard
from turtle import Turtle, Screen

class GameController:
    def __init__(self, snake : Snake, food : Food, scoreboard : Scoreboard):
        self.snake = snake
        self.food = food
        self.scoreboard = scoreboard
        self.isGameOn = True
        self.screen = Screen()
        self.screen.setup(width=700, height=600)
        self.screen.bgcolor("#1B2A4A")
        self.screen.title("Snake Game")
        self.screen.tracer(0)

    def setup_bindings(self):
        self.screen.listen()
        self.screen.onkeypress(self.snake.up, "Up")
        self.screen.onkeypress(self.snake.down, "Down")
        self.screen.onkeypress(self.snake.left, "Left")
        self.screen.onkeypress(self.snake.right, "Right")

    def run_game_loop(self):
        self.setup_bindings()
        self.snake.create_starting_snake()
        self.food.refresh()

        while self.isGameOn:
            self.screen.update()
            time.sleep(0.1)
            self.snake.move()
            self.check_wall_collision()
            self.check_food_collision()
            self.check_self_collision()
        self.scoreboard.game_over()
        self.screen.exitonclick()


    def check_food_collision(self):
        if self.snake.head.distance(self.food) < 15:
            self.food.refresh()
            self.snake.grow()
            self.scoreboard.increase_score()


    def check_wall_collision(self):
        x = self.snake.head.xcor()
        y = self.snake.head.ycor()
        if x > 350 or x < -350 or y > 300 or y < -300:
            self.isGameOn = False

    def check_self_collision(self):
        if not self.snake.has_started:
            return
        for segment in self.snake.segments[1:]:
            if self.snake.segments[0].distance(segment) < 10:
                self.end_game()

    def end_game(self):
        self.isGameOn = False
        self.scoreboard.game_over()
