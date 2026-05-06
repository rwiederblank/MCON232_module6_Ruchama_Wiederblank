from turtle import Turtle
import random
class Snake:
    def __init__(self):
        self.segments  = []
        self.colors = [
            "#FF6B6B", "#FF9F43", "#FECA57", "#48DBFB", "#FF9FF3",
            "#54A0FF", "#1DD1A1", "#00D2D3", "#5F27CD", "#C56CF0",
            "#FF4757", "#2ED573", "#FFA502", "#3742FA", "#70A1FF"
        ]
        self.create_starting_snake()
        self.has_started = False
        self.head = self.segments[0]


    def create_starting_snake(self):

        start_positions = [(0,0), (-20,0), (-40, 0)]
        for pos in start_positions:
            segment = Turtle()
            segment.shape("square")
            segment.color(random.choice(self.colors))
            segment.penup()
            segment.goto(pos)
            self.segments.append(segment)

    def move(self):
        if not self.has_started:
            return
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x, y)

        self.head.forward(20)

    def grow(self):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color(random.choice(self.colors))
        new_segment.penup()
        new_segment.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(new_segment)

    def reset(self):
        self.segments = []
        self.create_starting_snake()

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
            self.has_started = True

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
            self.has_started = True

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
            self.has_started = True


    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
            self.has_started = True





