import turtle
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
score=Scoreboard()
game_is_on=True


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
while game_is_on:
    screen.update()
    ball.move()

    if ball.ycor()>290 or ball.ycor()<-290:
        ball.bounce_y()
    #detect when ball hits paddle
    if ball.distance(r_paddle)<50 and ball.xcor() < 350 or ball.distance(l_paddle)<50 and ball.xcor() < -340:
        ball.bounce_x()
    #detech when right paddle misses
    if ball.xcor()>380:
        ball.reset_pos()
        score.l_score()
    if ball.xcor()<-380:
        ball.reset_pos()
        score.r_score()


screen.exitonclick()






