

import random




def dtp():
    print("""
    
    Welcome to the Day Trip Planner! Let's start with choosing an exciting destination!
    
    """)

def destination(destination_list):    
    print("Would you like to visit?")
    random.choice(destination_list)    
    destination = random.choice(destination_list) 
    print(destination)                                       #how do I keep from generating same rando city? I now see I can delete from lists since I named the variable.    
    user_input =  input("Do you like this location?: ")
    if user_input == "yes":
        print(f"Great selection in choosing {destination}!")
        return destination                    
    elif user_input != "yes":
        print("No worries, we have other exciting locations. How about?")
        random.choice(destination_list)
        destination = random.choice(destination_list)
        print(destination)
        user_input = input("Do you like this location?: ")
    if user_input == "yes":
        print(f"This will be an exciting trip! Now that you've selected {destination} let's move on to how you'd like to travel.""")
        return destination        
    elif user_input != "yes":
        print("""No worries, I've got just the place! Let's make it""")
        random.choice(destination_list)
        destination = random.choice(destination_list)
        print(destination)
        return destination
        
        

        
                

def transportation(transpo_list):
    random.choice(transpo_list)
    transportation = random.choice(transpo_list)
    print(f"""How about using {transportation} for travel?""")
    transpo_input = input("Will this work for transportation?: ")
    if transpo_input == "yes":
        print("Great selection!")
        return transportation
    elif transpo_input != "yes":
        random.choice(transpo_list)
        transportation = random.choice(transpo_list)
        print(f"No worries, how about {transportation}")
        transpo_input = input("Will this work?: ")
    if transpo_input == "yes":
        print("""This will be an exciting trip, let's now choose a restaruant!""")
        return transportation
    elif transpo_input != "yes":
        random.choice(transpo_list)
        transportation = random.choice(transpo_list)
        print(f"""No worries, a {transportation} should fit your needs. Now we'll pick a restaurant.""")
        return transportation
    


def restaurant(food_list):
    random.choice(food_list)
    restaurant = random.choice(food_list)
    print(f"""How about {restaurant}... """)
    sel_input = input("Does this sound like a good restaurant option?: ")
    if sel_input == "yes":
        print("Great choice!")
        return restaurant
    elif sel_input != "yes":
        print("""No worries, here's another option.""")
        random.choice(food_list)
        restaurant = random.choice(food_list)
        print(restaurant)
        sel_input = input("""
Will this work?""")
    if sel_input == "yes":
        print("""
We just need to get your itinerary.""")
        return restaurant
    elif sel_input != "yes":
        print("No worries! I've got just the thing and we'll get your itinerary.")
        random.choice(food_list)
        restaurant = random.choice(food_list)
        print(restaurant)
        return restaurant
        
     
def itinerary():
    print(f"You have chosen {destination} for your destination, and you will travel by {transportation}. Finally, you'll eat at {restaurant}... a great restaraunt!")
    





dtp()


destination(destination_list=["Los Angeles", "Seattle", "Portland", "Boise", "St Paul", "Chicago"])
destination = ""                                                                                    #I tried everythng to capture the return variables


transportation(transpo_list=["Commuter Train", "Car", "Public Bus", "Uber", "Taxi", "Limo"])
transportation = ""


restaurant(food_list=["TGIF", "Local Favorite", "Red Robin", "Famous Burger Joint", "Steak House"])
restaurant = ""

itinerary()







