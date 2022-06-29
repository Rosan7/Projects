# **Snake Game**

- Table of Content
  - About the Project
    - main.py
    - snake.py
    - food.py
    - scoreboard,py
  - Built With
  - Prerequisites
  - Installation


## About The Project
### main.py
    1. This is the main file of the project
    2. The screen is set to be 600px * 800px
    3. The snake is created in snake.py file
    4. The snake is controlled using four arrow keys of the keyboard
### snake.py
    This file contains a Snake class . 
    Functional requirements:
    1. __init__ and create_snake: This function helps to initialize a snake of three turtle segments placed along x axis.
    2. add_segment : This function helps to initialize turtle object , its attributes , postion in the screen
    3. extend : This adds a segment everytime the snake collides with food
    4. move : This method helps the snake move throughout the screen
    5. right,left,up,down : This methods are used to control the movement of the snake
### food.py
    This file contains a Food class:
    Functional requirements:
    1. __init__ : This creates a turtle object food and inherits the constructor of Turtle class
    2. refresh : This method randomly generates food at random positions
### scoreboard.py
    This file contains the Scoreboard class
    Functional requirements:
    1. __init__ : This method initializes the current user score . It also initializes the scoreboard where the                    score updates .
    2. update_scoreboard: This method updates the scoreboard after every event
    3. increase_score : This method increases the score of the player everytime the snake collides with the food
    4. game_over : This method ends the game when the snake collides with wall or with itself.
    
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
    
    
    
    
    
    
