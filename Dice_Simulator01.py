import random # This generates random numbers from given lists :
import time # This generates a time/seconds to work with : 

def dice_range(): # Genrating of the number between 1-6 : 
    return random.randint(1, 6)

def dice_animation(): # This is the animation function where I have created for rolling...
    for _ in range(5): # For loop
        print("Rolling...", end="\r") # end="\r (carriage return), it helps to move the cursor back to beginning line and overwrite it : 
        time.sleep(0.3)
        print("Rolling. ", end="\r")
        time.sleep(0.3)
        print("Rolling...", end="\r")
        time.sleep(0.3)
    print("Rolling...") # Prints the statement of rolling... : 

def main(): # This is the main function :
    print("Welcome to the Dice Simulator || Roll the dice and enjoy")
    
    while True: 
        input("Press any key to roll the dice : ") # This is the input section where you press any key and the number will be generated :
        dice_animation() # Calling animations 
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
