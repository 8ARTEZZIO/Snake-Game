from random import randint
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
COLOR = 'pink'
SHAPE = 'square'
SPEED = 'slowest'

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head_turned = False
        self.detection_level = 25

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(SHAPE)
            new_segment.speed(SPEED)
            new_segment.color(COLOR)
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].setheading(self.head.heading())
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.head_turned = False

    def add_segment(self):
        new_segment = Turtle(SHAPE)
        new_segment.speed(SPEED)
        new_segment.color(COLOR)
        new_segment.penup()
        if self.segments:
            last_seg_position = self.segments[-1].pos()
            new_segment.goto(last_seg_position)
        self.segments.append(new_segment)

    def hit(self):
        st_condition = (
                min(list(map(lambda x: int(x.distance(self.head)), self.segments[2:]))) < 3
        )
        nd_condition = self.head.xcor() <= -300
        rd_condition = self.head.xcor() >= 300
        th_4condition = self.head.ycor() <= -300
        th_5condition = self.head.ycor() >= 300
        return (st_condition or nd_condition or rd_condition or th_4condition or th_5condition)       

    def up(self):
        if not self.head_turned and self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.head_turned = True
    def down(self):
        if not self.head_turned and self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.head_turned = True
    def left(self):
        if not self.head_turned and self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.head_turned = True
    def right(self):
        if not self.head_turned and self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.head_turned = True

    def detect_wall(self):
        # decide a direction dependently on DISTANCE FROM THE WALL
        x = self.head.xcor()
        y = self.head.ycor()
        direction = self.head.heading()
        # I qt
        if (x >= 0 and y >= 0 and direction == 90 and self.head.ycor() >= 275):
            self.left()
            return 'left'
        elif (x >= 0 and y >= 0 and direction == 0 and self.head.xcor() >= 275):
            self.down()
            return 'down'
        # II qt
        if (x >= 0 and y < 0 and direction == 0 and self.head.xcor() >= 275):
            self.up()
            return 'up'
        elif (x >= 0 and y < 0 and direction == 270 and self.head.ycor() <= -275):
            self.left()
            return 'left'
        # III qt
        if (x < 0 and y < 0 and direction == 270 and self.head.ycor() <= -275):
            self.right()
            return 'right'
        elif (x < 0 and y < 0 and direction == 180 and self.head.xcor() <= -275):
            self.up()
            return 'up'
        # IV qt
        if (x < 0 and y >= 0 and direction == 90 and self.head.ycor() >= 275):
            self.right()
            return 'right'
        elif (x < 0 and y >= 0 and direction == 180 and self.head.xcor() <= -275):
            self.down()
            return 'down'

    def detect_food(self, food_x, food_y, snake_x, snake_y):
        direction = self.head.heading()
        if abs(food_x - snake_x) < 3:
            if food_y >= snake_y:
                if direction == 0:
                    self.up()
                    return 'up'
                elif direction == 180:
                    self.up()
                    return 'up'
            elif food_y < snake_y:
                if direction == 0:
                    self.down()
                    return 'down'
                elif direction == 180:
                    self.down()
                    return 'down'
        if abs(food_y - snake_y) < 3:
            if food_x >= snake_x:
                if direction == 90:
                    self.right()
                    return 'right'
                elif direction == 270:
                    self.right()
                    return 'right'
            elif food_x < snake_x:
                if direction == 90:
                    self.left()
                    return 'left'
                elif direction == 270:
                    self.left()
                    return 'left'

    def detect_tail(self, moves=list):
        data1 = moves[-6:]
        data = moves[-4:]
        data0 = moves[-3:]
        if min(list(map(lambda x: int(x.distance(self.head)), self.segments[2:]))) <= self.detection_level:
            # right, left, up, down -> left
            if data0 == ['left', 'up', 'down']:
                self.left()

            # left, up, right, down -> right
            if data0 == ['up', 'right', 'down']:
                self.right()

            # down, right, up, left -> up
            if data0 == ['right', 'up', 'left']:
                self.up()

            # down, left, up, right -> up
            if data0 == ['left', 'up', 'right']:
                self.up()

            # up, right, down, left -> down
            if data0 == ['right', 'down', 'left']:
                self.down()

            # up, left, down, right -> down
            if data0 == ['left', 'down', 'right']:
                self.down()

            # left, down, right, up -> right
            if data0 == ['down', 'right', 'up']:
                self.right()

            # right, down, left, up -> left
            if data0 == ['down', 'left', 'up']:
                self.left()

            # right, left, up, down -> left
            if data == ['right', 'left', 'up', 'down']:
                self.left()
                # print('left')

            # left, up, right, down -> right
            if data == ['left', 'up', 'right', 'down']:
                self.right()
                # print('right')

            # down, right, up, left -> up
            if data == ['down', 'right', 'up', 'left']:
                self.up()
                # print('up')

            # down, left, up, right -> up
            if data == ['down', 'left', 'up', 'right']:
                self.up()
                # print('up')

            # up, right, down, left -> down
            if data == ['up', 'right', 'down', 'left']:
                self.down()
                # print('down')

            # up, left, down, right -> down
            if data == ['up', 'left', 'down', 'right']:
                self.down()
                # print('down')

            # left, down, right, up -> right
            if data == ['left', 'down', 'right', 'up']:
                self.right()
                # print('right')

            # right, down, left, up -> left
            if data == ['right', 'down', 'left', 'up']:
                self.left()
                # print('left')

            if data == ['right', 'up', 'left', 'down']:
                self.left()

            if data1 == ['left', 'down', 'right', 'down','right','up']:
                self.right()

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)  # Move segments off-screen
        self.segments.clear()
        self.create_snake()  # Recreate the snake in the initial state
        self.head = self.segments[0]
        self.head_turned = False
