from turtle import Turtle

starting_position = [(0, 0), (-20, 0), (-40, -0)]
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.my_snake = []
        self.create_snake()
        self.head = self.my_snake[0]

    def create_snake(self):
        for position in starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.my_snake.append(new_segment)

    def extend(self):
        self.add_segment(self.my_snake[-1].position())

    def move_my_snake(self):
        for segment in range(len(self.my_snake) - 1, 0, -1):
            new_x = self.my_snake[segment - 1].xcor()
            new_y = self.my_snake[segment - 1].ycor()
            self.my_snake[segment].goto(new_x, new_y)
        self.head.forward(move_distance)

    def reset(self):
        for segments in self.my_snake:
            segments.goto(1000,1000)
        self.my_snake.clear()
        self.create_snake()
        self.head = self.my_snake[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
