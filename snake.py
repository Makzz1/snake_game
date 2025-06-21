
import turtle
import time
import food


reset = False
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
POSITION = ((0,0),(-20,0),(-40,0))

class Snake:
    def __init__(self):
        self.snake_length = 2
        self.snake_body = []


    def create_snake(self):
        for i in (POSITION):
            self.add_segment(i)


    def add_segment(self,position):
        tim = turtle.Turtle()
        tim.shape("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.snake_body.append(tim)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())
        self.snake_length += 1

    def snake_movement(self):
            for i in range(self.snake_length):
                self.snake_body[self.snake_length - i].goto(self.snake_body[self.snake_length-(i+1)].xcor(),self.snake_body[self.snake_length-(i+1)].ycor())
            self.snake_body[0].forward(20)

    def move_up(self):

        if self.snake_body[0].heading() != DOWN :
            self.snake_body[0].setheading(UP)

    def move_down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def move_right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

    def move_left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def reset(self):
        self.snake_body[0].goto(-1000,1000)
        self.snake_length = 2
        self.snake_body[0].goto(0,0)
        global reset
        reset = True







