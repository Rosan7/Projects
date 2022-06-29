# **Turtle Crossing**

- Table of Content
  - About the Project
    - main.py
    - player.py
    - car_manager.py
    - scoreboard,py
  - Built With
  - Prerequisites
  - Installation


## About The Project
### main.py
    1. This is the main file of the project
    2. The screen is set to be 600px * 600px
    3. The turtle is created in snake.py file
    4. The cars are created in car_manager.py
    5. The scoreboard is created in scoreboard.py
    6. The main objective of this game is to make the turtle dodge the moving cars and reach the destination
### player.py
    This file contains a Player class . 
    Functional requirements:
    1. __init__ : This function helps to initialize the player turtle and its attributes.
    2. go_up : This function makes the turtle to move forward
    3. go_to_start : This function redirects the turtle to its starting position after crossing every level 
    4. is_at_finish : This function checks whether the turtle has reached the finishing line
### car_manager.py
    This file contains a Car class:
    Functional requirements:
    1. __init__ : This creates random cars and initializes its speed
    2. create_cars : This method sets the attributes of the cars , its position .
    3. move_cars : This method makes all the listed cars in screen to move uniformly
    4. level_up : This method increases the speed of cars after every successful cross of the turtle
### scoreboard.py
    This file contains the Scoreboard class
    Functional requirements:
    1. __init__ : This method initializes the current user score . It also initializes the scoreboard where the                    score updates .
    2. update_scoreboard: This method updates the scoreboard after every event
    3. incr_level : This method is used to increase the level and update the score
    4. game_over : This method reacts when the turtle collides with any of the cars and the game ends .
## Built with
    - turtle
      - Turtle
      - Screen
    - time
    - random 
## Prequisites
    - Pycharm Editor or Python intepreter
    - pip module
    - turtle
    - time
    - random 
## Installation
    1. Clone the repo
        - git clone https://github.com/Rosan7/Projects.git 
    
    
    
    
    
    
