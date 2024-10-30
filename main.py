import time
from _datetime import datetime
from turtle import Turtle
from snake import Snake
from food import Food
from dashboard import Dashboard
from game_window import Window

def update_move_history(moves, new_move):
    if not moves or moves[-1] != new_move:
        moves.append(new_move)
    return moves[-6:]

def reset_game(snake, food, dashboard, moves):
    """Resets the snake, food, and dashboard but retains moves history and score."""
    snake.reset()  # Implement a reset method in the Snake class to reset its state
    food.generate_food()  # Generate new food position
    dashboard.reset_display()  # Reset the display if necessary
    moves.clear()  # Clear the moves list

def main():
    # Initialize all the classes once
    moves = []
    scores = []
    window = Window()
    snake = Snake()
    food = Food()
    dashboard = Dashboard()

    # Listen to keys from the keyboard
    window.window_keys(snake)

    # Game loop that allows resetting
    while True:
        game_is_on = True
        while game_is_on:
            window.screen.update()
            dashboard.score_display()
            time.sleep(0.01)

            snake.move()
            snake.detect_tail(moves)

            x1 = snake.detect_wall()
            if x1 is not None:
                update_move_history(moves, x1)

            x2 = snake.detect_food(food.xcor(), food.ycor(), snake.head.xcor(), snake.head.ycor())
            if x2 is not None:
                update_move_history(moves, x2)

            # Condition when snake's head touches its own tail or hits a wall
            if snake.hit():
                # with open('scores.txt', 'a') as data:
                #     d = str(f'\nlvl:{snake.detection_level:.2f};score:{dashboard.score}')
                #     data.write(d)
                # print(f'{moves[-6:]}, detection_lvl={snake.detection_level}, score={dashboard.score}')
                dashboard.save_score()
                game_is_on = False

            # Condition when snake's head touches the food
            if snake.head.distance(food) < 15:
                dashboard.score += 1
                food.generate_food()
                dashboard.score_display()
                snake.add_segment()

        # Reset the game state but keep relevant data
        reset_game(snake, food, dashboard, moves)

if __name__ == '__main__':
    main()
