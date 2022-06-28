print("Welcome to Treasure Islnd.")
print("Your mission is to find the treasure.");
instruc1 = input('You are at a cross road. Where do you to go? Type "left" or "right"')
if(instruc1 == "left"):
    instruc2 = input('You came at a lake. There is an island in the middle of the lake. Type "wait" or "swim"')
    if(instruc2 == "wait"):
        instruc3 = input('Which door? Type "Red" or "Blue" or "Yellow"')
        if(instruc3 == "Red"):
            print("Burned by fire . Game Over")
        elif(instruc3 == "Yellow"):
            print("You Win!")
        elif(instruc3 == "Blue"):
            print("Eaten by beasts . Game over")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game over")

    
