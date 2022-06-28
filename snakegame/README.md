#Snake Game (Readme.md)

There are four python files in this project:
              1) main.py
              2) snake.py
              3) food.py
              4) scoreboard.py
Each of the .py files has its own working . You can run the game using the main.py file along with all other files .
Below I have listed the functional requirements of this project:

main.py
    This is the main file of the project . Here objects of the classes used are declared and their functions are utilized .
    From the turtle module ,Screen class is used. The user defined classes used are Snake class , Scoreboard class and Food class.
    The screen is assigned the width of 600 px * 800 px .
    The snake of this game is created using three turtle objects lined together in the x axis. The movement of the snake is controlled 
    using the onkey method of turtle module . The turtle responds to four arrow keys of keyboard. The snake increases in size upon colliding 
    with the food . The game continues until the snake does not collide with any of the walls or collide with its tail . 
snake.py
    This file contains a Snake class . 
    Functional requirements:
    1) __init__ and create_snake: This function helps to initialize a snake of three turtle segments placed along x axis.
    2) add_segment : This function helps to initialize turtle object , its attributes , postion in the screen
    3) extend : This adds a segment everytime the snake collides with food
    4) move : This method helps the snake move throughout the screen
    5)right,left,up,down : This methods are used to control the movement of the snake
food.py
    This file contains a Food class:
    Functional requirements:
    1)__init__ : This creates a turtle object food and inherits the constructor of Turtle class
    2)refresh : This method randomly generates food at random positions
scoreboard.py
    This file contains the Scoreboard class
    Functional requirements:
    1)__init__ : This method initializes the current user score . It also initializes the scoreboard where the score updates .
    2)update_scoreboard: This method updates the scoreboard after every event
    3)increase_score : This method increases the score of the player everytime the snake collides with the food
    4)game_over : This method ends the game when the snake collides with wall or with itself.
    
   
    
    
    
    
    
