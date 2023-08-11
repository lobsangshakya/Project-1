import random

def dice_range():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Simulator || Roll the dice and enjoy")
    
    while True:
        input("Press any key to roll the dice : ")
        result = dice_range()
        print("You rolled : ", result)
        
        play_again = input("Do you want to roll again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thank you for using the Dice Simulator!")
            break
        else:
            print("Let's roll again!")

if __name__ == "__main__":
    main()
