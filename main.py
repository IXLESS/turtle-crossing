import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkey(player.move_up, "Up")

game_is_on = True
i = 0
number = 10
speed = 5
cars = []
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() > 285:
        for car in cars:
            car.hideturtle()
        if number == 1:
            pass
        else:
            number -= 1
        cars.clear()
        score.next_level()
        player.reset()
        speed += 5
    for car in cars:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False 
            break
    if i % number == 0:
        new_car = CarManager()
        cars.append(new_car)

    for car in cars:
        car.move(speed)
    i +=1
    
screen.exitonclick()
