from turtle import *
import snake
import food
import time
import scoreboard

def exit():
    print(1)
    global game_is_on
    game_is_on = False

FONT = ("arial", 20, "bold")
game_is_on = True

#GUI background settings
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snake_game")
screen.tracer(0)

#creating object
snake1 = snake.Snake()
snake1.create_snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()



#movement
screen.listen()
screen.onkey(key="Up",fun= snake1.move_up)
screen.onkey(key="Right",fun= snake1.move_right)
screen.onkey(key="Left",fun= snake1.move_left)
screen.onkey(key="Down",fun= snake1.move_down)
screen.onkey(key="r",fun= snake1.reset)
screen.onkey(key="q",fun=exit)


while game_is_on:
    time.sleep(0.1)  # speed of snake
    snake1.snake_movement()
    screen.update()

    if snake1.snake_body[0].distance(food) < 15:
        food.refresh()
        scoreboard.score += 1
        scoreboard.update()
        snake1.extend()
        print("nom nom")

#detects collison with wall
    if snake1.snake_body[0].xcor() > 280 or snake1.snake_body[0].xcor() < -280 or snake1.snake_body[0].ycor() < -280 or snake1.snake_body[0].ycor() > 280 :
        if scoreboard.high_score < scoreboard.score:
            scoreboard.high_score = scoreboard.score
        scoreboard.update()
        scoreboard.game_over()
        snake1.snake_body[0].goto(x=1000,y=1000)
        #game_is_on = False

#detect tail collision
    for body in snake1.snake_body[1:len(snake1.snake_body)]:
        if snake1.snake_body[0].distance(body) < 10:
            if scoreboard.high_score < scoreboard.score:
                scoreboard.high_score = scoreboard.score
            scoreboard.update()
            scoreboard.game_over()
            snake1.snake_body[0].goto(x=1000, y=1000)
            break

    if snake.reset :
            scoreboard.score = 0
            scoreboard.update()
            snake.reset = False



#screen.mainloop()