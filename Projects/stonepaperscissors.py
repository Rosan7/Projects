rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
#Write your code below this line 👇

your_point = 0
opponent_point = 0
while(your_point!=5 and opponent_point!=5):
  user_choice = int(input("What do you choose?Type 0 for Rock,1 for Paper or 2 for Scissors : "))
  choices = ["Rock","Paper","Scissors"]
  opponent_choice = random.choice(choices)
  player_choice = choices[user_choice]
  
  if(player_choice == "Rock"):
    if(opponent_choice == "Paper"):
      
      opponent_point += 1
      print(f"User point : {your_point}")
      print(f"opponent_point : {opponent_point}")
      
    elif(opponent_choice == "Scissors"):
      
      your_point += 1
      print(f"User point : {your_point}")
      print(f"opponent_point : {opponent_point}")
    else:
      print(f"User point : {your_point}")
      print(f"opponent_point : {opponent_point}")
      
  elif(player_choice == "Paper"):
    if(opponent_choice == "Scissors"):
      
      opponent_point += 1
      print(f"User point : {your_point}")
      print(f"opponent_point : {opponent_point}")
    elif(opponent_choice == "Stone"):
      
      your_point += 1
      print(f"User point : {your_point}")
      print(f"opponent_point : {opponent_point}")
    else:
      print(f"User point : {your_point}")
      print(f"opponent_point : {opponent_point}")
  else:
    if(opponent_choice == "Stone"):
     
      opponent_point += 1
      print(f"User point : {your_point}")
      print(f"opponent_point : {opponent_point}")
    elif(opponent_choice == "Paper"):
    
      your_point += 1
      print(f"User point : {your_point}")
      print(f"opponent_point : {opponent_point}")
    else:
      print(f"User point : {your_point}")
      print(f"opponent_point : {opponent_point}")
  
if(user_choice == 5):
  print("You wins")
else:
  print("Opponent wins")
