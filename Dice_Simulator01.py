import random # This generates random numbers from given lists :

def dice_range(): # Genrating of the number between 1-6 : 
    return random.randint(1, 6)

def main(): # This is the main function :
    print("Welcome to the Dice Simulator || Roll the dice and enjoy")
    
    while True: 
        input("Press any key to roll the dice : ") # This is the input section where you press any key and the number will be generated :
        result = dice_range() # Calls the function from dice_range to generate numbers : 
        print("You rolled : ", result) # Printing of the results : 
        
        play_continue = input("Do you want to roll again? (yes/no): ") # Here, it tells whethere you want to continue to roll or not :
        if play_continue.lower() != "yes": # If the user enters "yes", It continues the game : 
            print("Thank you for using the Dice Simulator!")
            print("Hoping to see you again!")
            break
        else:
            print("Let's roll again!")

if __name__ == "__main__": 
    main()
