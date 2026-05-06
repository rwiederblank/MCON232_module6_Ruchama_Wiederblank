from turtle import Turtle, Screen
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()


    def refresh(self):
        rand_x, rand_y = self.random_position()
        self.goto(rand_x, rand_y)



    def random_position(self):
        rand_x = random.randint(-300, 300)
        rand_y = random.randint(-280,280)
        return rand_x, rand_y
