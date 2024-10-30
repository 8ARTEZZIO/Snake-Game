import time
from turtle import Turtle

POSITION_1 = 0, 270
COLOR = 'white'

class Dashboard:
    def __init__(self):
        self.text = Turtle()
        self.score = 0
        self.score_initialize()
        self.score_display()

    def score_initialize(self):
        self.text.penup()
        self.text.goto(POSITION_1)
        self.text.color(COLOR)
        self.text.hideturtle()

    def score_display(self):
        hgh = self.get_highscore()
        self.text.clear()
        self.text.penup()
        self.text.goto(POSITION_1)
        self.text.color(COLOR)
        self.text.hideturtle()
        self.text.write(f'SCORE: {self.score}  HIGHSCORE: {hgh}', align='center', font=("Arial", 15))

    def save_score(self):
        high = self.get_highscore()
        if self.score > high:
            high = self.score
            with open('C:\\Users\\grt0\\Desktop\\highscore.txt', 'w') as data:
                content = f'{high}'
                data.write(content)
        self.score = 0

    def get_highscore(self):
        with open('C:\\Users\\grt0\\Desktop\\highscore.txt') as data:
            return int(data.read())

    def display_game_over(self):
        self.text.goto(0, 0)
        self.text.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def reset_display(self):
        self.text.clear()
        self.score = 0  # Reset score to 0
        self.text.goto(0, 270)  # Reset position for displaying the score
        self.score_display()