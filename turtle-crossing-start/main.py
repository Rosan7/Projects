import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
racing_car = CarManager()
score = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Capstone project")
player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    racing_car.create_cars()
    racing_car.move_cars()

    # Detect collison with car
    for car in racing_car.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
    if player.is_at_finish():
        player.go_to_start()
        racing_car.level_up()
        score.incr_level()


screen.exitonclick()
