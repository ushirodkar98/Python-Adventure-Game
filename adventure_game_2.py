# Importing modules
import time
import random

# Defining a empty list

items = []
charecters = ["Farie","Dragon","Troll","Pirate","Gorgon"]    
actors = random.choice(charecters)
            

# Defining Print Pause Function


def print_pause(string):
    print(string)
    time.sleep(2)

# defining introduction


def intro():
        print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
        print_pause(f"Rumor has it that a {actors} is somewhere around here, and has been terrifying the nearby village.")    
        print_pause("In front of you is a house.")
        print_pause("To your right is a dark cave.")
        print_pause("In your hand you hold your trusty (but not very effective) dagger.")

# def first option


def first_option():
    print_pause("You approach the door of the house")
    print_pause(f"You are about to knock when the door opens and out steps a {actors} ")
    print_pause(f"Eep! This is the {actors}'s'house! ")
    print_pause(f"The {actors} attacked you! ")

# def second option


def second_option():   
    if "sword" in items:    
        print_pause("You peer cautiously into the cave.")  
        print_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now.")    
        print_pause("You walk back out to the field.")
    else:   
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!") 
        print_pause("You discard your silly old dagger and take the sword with you.")  
        print_pause("You walk back out to the field.")  
        items.append("sword")

# Action options fight or run


def action_option():
    
    if "sword" in items:
        print_pause(f"As the {actors} moves to attack, you unsheath your new sword.")   
        print_pause("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")   
        print_pause(f"But the {actors} takes one look at your shiny new toy and runs away!")   
        print_pause(f"You have rid the town of the {actors}. You are victorious!")               
    elif "sword" not in items:
        print_pause("You tried your best")
        print_pause(f"But your dragger was no match in front of {actors} ")    
        print_pause("You're defeated")
    
        
        

# Acttion option 2 run away


def action_option_2():
    print_pause("You run back into the field. Luckily, you don't seem to have been followed.")

# action 


def action():
    options = input("Press 1 to fight or 2 to run away \n")
    if options == "1":                   
        action_option()
        play_again_option()            
    elif options == "2":                    
        action_option_2()
        play_option()
    else:
        print_pause("There are only 2 options 1,2")
        return action()

# play again option


def play_again_option():
    while True:
        answer = input("Would you like to play again!\n"
                        "Please enter 'yes' or 'no' \n").lower()    
        if "yes" in answer:              
            print_pause("Great we'll restart!")
            global actors
            actors = random.choice(charecters)
            adventure_game()
            break          
        elif 'no' in answer:          
            print_pause("Thanks for playing with us!")
            break
    
# def play option


def play_option():

    
        option = input("Enter 1 to knock the door of the house\n"
                       "Enter 2 to peer in to the cave\n"
                       "What would you like to do?\n"
                       "Please enter 1 or 2\n")
        if option == "1":                            
            first_option()
            action()
        elif option == "2":
            second_option()
            play_option()
        else:
            print_pause("There are only 2 options")
            play_option()

# Adventure Game


def adventure_game():
    intro()
    play_option()


adventure_game()
