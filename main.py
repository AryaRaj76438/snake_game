import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor()>280 or snake.head.ycor() <-280:
        scoreboard.reset()
        snake.reset()
        # scoreboard.game_over()
        # game_is_on = False

    # Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            # snake.reset()


    # for segment in snake.segments[1:]:
    #     if snake.head.distance(segment) < 10:
    #         scoreboard.game_over()
    #         game_is_on = False


    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         scoreboard.game_over()
    #         game_is_on = False
    # If head collides with any segment in the tail:
        # trigger game_over


screen.exitonclick()




# screen = Screen()
# screen.setup(width=600,height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)
#
# starting_position = [(0,0), (-20,0), (-40,0)]
# segments = []
#
# for position in starting_position:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)
#
# # screen.update()
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     # for seg in segments:
#     #     seg.forward(20)
#     for seg_num in range(len(segments)-1,0,-1):
#         new_x = segments[seg_num-1].xcor()
#         new_y = segments[seg_num-1].ycor()
#         segments[seg_num].goto(new_x,new_y)
#     segments[0].forward(20)