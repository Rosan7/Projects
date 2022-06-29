# **Quiz Trivia**

- Table of Content
  - About the Project
    - main.py
    - question_model.py
    - data.py
    - quizbrain.py
  - Built With
  - Prerequisites
  - Installation


## About The Project
### main.py
    1. This is the main file of the project 
    2. This initializes a question_bank object which consists of question and its answer 
    3. The player gets to know the score and the correct answer after every question
### question_model.py
    This file contains a Question class . 
    Functional requirements:
    1. __init__ : This method initiates the structure and variables of each question in the question bank. 
### data.py
    - This file contains data of all the questions in the question bank
### quizbrain.py
    This file contains the QuizBrain class
    Functional requirements:
    1. __init__ : This method initiates the question number and user_score.
    2. still_has_questions : This method checks whether there are questions to continue the game.
    3. next_question : This method figures out the next question in the question_bank and accepts the answer of user
    4. check_answer : This method checks the answer of user with the original answer and updates score . 
## Built with
    - Pycharm editor
## Prequisites
    - Pycharm Editor or Python intepreter
    - To create data.py file of your own 
       - Open https://opentdb.com/ and move to API in taskbar
       - Create the no of questions and choices and GENERATE API URL
       - The data would be in form of JSON format 
       - Convert the info into lists of questions in dictionary format.
    
## Installation
    1. Clone the repo
        - git clone https://github.com/Rosan7/Projects.git 
    
    
    
    
    
    
