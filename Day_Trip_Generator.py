


import random



def dtp():
    print("""
    
    Welcome to the Day Trip Planner! Let's start with choosing an exciting destination!
    
    """)

def destination(destination_list):    
    print("Would you like to visit?")
    random.choice(destination_list)    
    city = random.choice(destination_list) 
    print(city)                                       #how do I keep from generating same rando city?    
    user_input =  input("Do you like this location?: ")
    if user_input == "yes":
        print(f"Great selection in choosing {city}!")        
    elif user_input != "yes":
        print("No worries, we have other exciting locations. How about?")
        random.choice(destination_list)
        city = random.choice(destination_list)
        print(city)
        user_input = input("Do you like this location?: ")
    if user_input == "yes":
        print(f"This will be an exciting trip! Now that you've selected {city} let's move on to how you'd like to travel.""")
    elif user_input != "yes":
        print("No worries, I've got just the place!")
        random.choice(destination_list)
        city = random.choice(destination_list)
        print(city)
        
                

def transportation(transpo_list):
    random.choice(transpo_list)
    transpo = random.choice(transpo_list)
    print(transpo)
    transpo_input = input("Would you like to use this mode of transportation?: ")
    if transpo_input == "yes":
        print("Great selection!")
    elif transpo_input != "yes":
        print("No worries, how about?")
        random.choice(transpo_list)
        transpo = random.choice(transpo_list)
        print(transpo)
        transpo_input = input("Will this work?: ")
    if transpo_input == "yes":
        print("This will be an exciting trip, let's now choose a restaruant!")
    elif transpo_input != "yes":
        print("No worries, this should fit your needs.")
        random.choice(transpo_list)
        transpo = random.choice(transpo_list)
        print(transpo)



def restaurant(food_list):
    random.choice(food_list)
    selection = random.choice(food_list)
    print(selection)
    sel_input = input("Does this sound like a good restaurant option?: ")
    if sel_input == "yes":
        print("Great choice!")
    elif sel_input != "yes":
        print("No worries, how about?")
        random.choice(food_list)
        selection = random.choice(food_list)
        print(selection)
        sel_input = input("Will this work?: ")
    if sel_input == "yes":
        print("Great! Almost finished.")
        
    elif sel_input != "yes":
        print("No worries! I've got just the thing.")
        random.choice(food_list)
        selection = random.choice(food_list)
        print(selection)
        return(random.choice(food_list))
    
        
def itinerary(travel_list):
    print(travel_list) 

dtp()

destination(destination_list=["Los Angeles", "Seattle", "Portland"])


transportation(transpo_list=["Commuter Train", "Vehicle", "Public Bus"])

restaurant(food_list=["TGIF", "Local Favorite", "Red Robin"])

itinerary(travel_list=["city", "transpo", "selection"])