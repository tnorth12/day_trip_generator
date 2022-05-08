


import random



def dtp():
    print("""
    
    Welcome to the Day Trip Planner! Let's start with choosing an exciting destination!
    
    """)

def destination(destination_list):
    print("Would you like to visit?")
    print(random.choice(destination_list))                 #how do I keep from generating same rando city?
    user_input =  input("Do you like this location?: ")
    if user_input == "yes":
        print("Great selection!")
    elif user_input != "yes":
        print("No worries, we have other exciting locations. How about?")
        print(random.choice(destination_list))
        user_input = input("Do you like this location?: ")
    if user_input == "yes":
        print("This will be an exciting trip, let's move on to how you'd like to travel.")
        return(random.choice(destination_list))
    elif user_input != "yes":
        print("No worries, I've got just the place!")
        print(random.choice(destination_list))
        return(random.choice(destination_list))
        
        

def transportation(transpo_list):
    print(random.choice(transpo_list))
    transpo_input = input("Would you like to use this mode of transportation?: ")
    if transpo_input == "yes":
        print("Great selection!")
    elif transpo_input != "yes":
        print("No worries, how about?")
        print(random.choice(transpo_list))
        transpo_input = input("Will this work?: ")
    if transpo_input == "yes":
        print("This will be an exciting trip, let's now choose a restaruant!.")
        return(random.choice(transpo_list))
    elif transpo_input != "yes":
        print("No worries, this should fit your needs")
        print(random.choice(transpo_list))
        return(random.choice(transpo_list))

    
        
       



dtp()

destination(destination_list=["Los Angeles", "Seattle", "Portland"])

transportation(transpo_list=["Commuter Train", "Vehicle", "Public Bus"])

