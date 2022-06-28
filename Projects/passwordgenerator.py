#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
options = [letters,symbols,numbers]
password = ""
while(nr_letters != 0 or nr_symbols!=0 or nr_numbers!=0):
  
  chosen_option = random.choice(options)
  character = random.choice(chosen_option)
  
  if(character in letters and nr_letters != 0):
    nr_letters -= 1
    password += character
  elif(character in numbers and nr_numbers != 0):
    nr_numbers -= 1
    password += character
  elif(character in symbols and nr_symbols != 0):
    nr_symbols -= 1
    password += character

print("Your password is " + password)
  
