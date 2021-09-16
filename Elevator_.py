import time 


# Defining the function of print pause

def print_pause(string):

    print(string)

    time.sleep(2)


# Defining the function of Intro

def intro():

    print_pause("You have just arrived at your new job!")

    print_pause("You are in the elevator.")

# First floor

def first_floor(items):
    print_pause("You push the button for the first floor.")     # If user enters 1 he'll go to lobby
        
    print_pause("After a few moments, you find yourself in the lobby.")

    if "ID Card" in items:
        
        print_pause(("The clerk greets you again, but you already have your ID Card."
        
                "So there isn't much here!"))
                
            
    else:
        
        items.append("ID Card")
        
        print_pause("The cleark greets you and gives you your ID Card")

    ride_elevator(items)
# The second floor

def second_floor(items):

    print_pause("You push the button for the second floor.")   # if he enters 2 he'll go to HR
            
    print_pause("After a few moments, you find yourself in the human resources department.")

    if "Handbook" in items:
            
        print_pause("There is nothing much to do here! you can go to other floor")
            
    elif "ID Card" not in items:
            
        print_pause("I can't give you handbook unless you have ID card! ")
            
    else:
            
        print_pause("The HR Greets you sees your ID Card and gives you the handbook")
            
        items.append("Handbook")

    ride_elevator(items)
            

# The third floor 

def third_floor(items):
    print_pause("You push the button for the third floor.")   # If he enter 3 he'll go to Third floor
        
    print_pause("After a few moments, you find yourself in the engineering department.")

    if "ID Card" not in items and "Handbook" not in items:
        
        print_pause("You can't get in you require a ID card and a handbook")


    elif "ID Card" in items and "Handbook" not in items:
                
        print_pause("You can get in but, you require a Handbook, you need to submit it to your head")
                

    elif "Handbook" in items and "ID Card" in items:
                
        print_pause("You can start working here as Vp of engeneering!") 
    ride_elevator(items)  




# The Actual code 

# Here the user will give where he wants to go!


        # The If else statements

def ride_elevator(items):

    floor = int(input("Where would you like to go \n"
        "1. Lobby \n"
        "2. Human Resource \n"
        "3. Engineering department\n"))

    if floor == 1:

        first_floor(items)
                    
    elif floor == 2:
                
        second_floor(items)
                
    elif floor == 3:
                
        third_floor(items)
            
    else:                                                        # If he enters someting beyond the range of 3

        print_pause("there are only 3 floors!")    
            
    print_pause("Where would you like to go next?")



def play_game():

    items = []

    intro()

    ride_elevator(items)    


play_game()




