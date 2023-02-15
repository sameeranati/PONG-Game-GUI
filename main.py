from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# speed=["fastest","fast","normal","slow","slowest"]
screen = Screen()
screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PongGame")
rpaddle=Paddle((350,0))
lpaddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()
screen=Screen() 
screen.listen()

screen.onkey(rpaddle.go_up, "Up")
screen.onkey(rpaddle.go_down, "Down")

screen.onkey(lpaddle.go_up, "w")
screen.onkey(lpaddle.go_down, "s")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    # ball.move_ball()
    # ball.speed(speed[-1])
    if ball.ycor()>=280 or ball.ycor()<-280:
      ball.bounce_y()
    if ball.distance(rpaddle)<50 and ball.xcor()>320 or ball.distance(lpaddle)<50 and ball.xcor()<-320:
      ball.bounce_x()
    if ball.xcor()>380:
      ball.home()
      ball.bounce_x()
      scoreboard.l_point()
      for s in speed:
        ball.speed[i]
        i+=1
    if ball.xcor()<-380:
      ball.home()
      ball.bounce_x()
      scoreboard.r_point()
      for s in speed:
        ball.speed[i]
        i+=1
    
  
    
screen.exitonclick()
  