# **Ping Pong Game**

- Table of Content
  - About the Project
    - main.py
    - ball.py
    - paddle.py
    - scoreboard.py
  - Built With
  - Prerequisites
  - Installation


## About The Project
### main.py
    1. This is the main file of the project 
    2. The paddles lying on left and right side of the screen are created using turtle
    3. The attributes of the screen are set i.e color as Black dimensions 600px height and 800px width
    4. onkey() method makes the paddles respond to keyboard instructions like "w","s","Up","Down"
    5. The tracer is set to 0 so as to turn animations off and the screen updates itself after 0.1 seconds
    6. The game is played between two players and can evaluate their scores during the game.
### ball.py
    **Ball class**
    1. __init_ : The ball is set as a turtle object and the attributes are declared.
    2. move : This method makes the ball move randomly at a constant amount.
    3. bounce_y : This method works when the ball bounces off the top and bottom edge.
    4. bounce_x : This method works when the ball bounces off the paddle and varies in speed after every bounce.
### paddle.py
    **Paddle class**
    1.  __init__ : Creates paddles  with Turtle attributes 
    2. move : Moves the paddle by a constant distance
    3. up : Moves the paddle up 
    4. down : Moves the paddle down
### scoreboard.py
    **Scoreboard class**
    Functional requirements:
    1. __init__ : This method initiates the scorecard of both players at the start of game.
    2. update_scoreboard : This method assigns the positon of scoreboard and updates the scorecard.
    3. l_point : This method increases the score of the left player if the right player misses the ball.
    4. r_point : This method increases the score of the right player if the left player misses the ball.
## Built with
    - Pycharm editor
    - turtle module
       -Turtle class
       -Screen class
    - time
## Prequisites
    - Pycharm Editor or Python intepreter
    - pi module
    - turtle module
    - time module
## Installation
    1. Clone the repo
        - git clone https://github.com/Rosan7/Projects.git 
    
    
    
    
    
    
