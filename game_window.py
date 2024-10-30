from turtle import Screen

COLOR = 'green'
WIDTH = 600
HEIGHT = 600
TITLE = 'Snake'
TRACER = 0
KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT = 'Up', 'Down', 'Left', 'Right'

class Window:
    def __init__(self):
        self.screen = Screen()
        self.window_initialize()

    def window_initialize(self):
        self.screen.setup(WIDTH, HEIGHT)
        self.screen.bgcolor(COLOR)
        self.screen.title(TITLE)
        self.screen.tracer(TRACER)

    def window_keys(self, snake):
        self.screen.listen()
        self.screen.onkey(snake.up, KEY_UP)
        self.screen.onkey(snake.down, KEY_DOWN)
        self.screen.onkey(snake.left, KEY_LEFT)
        self.screen.onkey(snake.right, KEY_RIGHT)