# **Coffee Maker**

- Table of Content
  - About the Project
    - main.py
    - menu.py
    - coffee_maker.py
    - money_machine.py
  - Built With
  - Prerequisites
  - Installation


## About The Project
### main.py
    1. This is the main file of the project 
    2. This takes in orders of the customer and tries to complete the order if the requirements are satisfied.
    3. The reports of items left are processed after every order
### menu.py
    - MenuItem class
    Functional requirements:
    1. __init__ : This method initiates the model of the item with the name of the item , cost and requirements.
    - Menu class
    Functional requirements:
    1. __init__ : Creates a menu with the help of MenuItem class inside menu list
    2. get_items : Returns all the names of available menu items
    3. find_drink : Searches the menu for a particular drink by name. Returns that item if it exists,otherwise returns None
### coffee_maker.py
    1.  __init__ : Creates a resources model with all the initially available ingredients.
    2. report : Prints a report of all resources.
    3. is_resource_sufficient : This method takes parameter as the drink name and returns whether ingredients are enough to         make the drink
    4. make_coffee : This method takes parameter as drink name and deducts the ingredients after drink is made
### money_machine.py
    This file contains the MoneyMachine class
    Functional requirements:
    1. __init__ : This method initiates the profit and money_recieved.
    2. report : This method prints the current profit.
    3. process_coins : Returns the total calculated from coins inserted
    4. make_payment : "Returns True when payment is accepted and gives a change , or False if insufficient
## Built with
    - Pycharm editor
## Prequisites
    - Pycharm Editor or Python intepreter
## Installation
    1. Clone the repo
        - git clone https://github.com/Rosan7/Projects.git 
    
    
    
    
    
    
