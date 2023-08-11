# Here it is a small basic projects on dice simulator as who will get to the 50 points first : 

# RULES : 
# 1) Maximum 4 players and minimum 1 player so that you will be playing against computer
# 2) First to 50 wins 
# 3) If you get 1, next player gets it 

import random # This generates random numbers from given lists :

def main():
    return("Welcome to Who get to 50 first || Lets play this game!")

def players():
    int(input("Enter how many players are playing (1-4) : "))
    if input > 4:
        print("Maximum only 4 players can play this game.")
    elif input <=4:
        print("Well done with your first step.")
        print("Players : ", input)
        if input == 1:
            print("Alright, You will be playing against computer. All the best!")
        else:
            print("You will be playing against each other")

if __name__ == "__main__":
    main()