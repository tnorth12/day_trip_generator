


import random



def dtp():
    print("""
    
    Welcome to the Day Trip Planner! Let's start with choosing an exciting destination!
    
    """)

def destination(destination_list):    
    print("Would you like to visit?")
    random.choice(destination_list)    
    city = random.choice(destination_list) 
    print(city)                                       #how do I keep from generating same rando city? I now see I can delete from lists since I named the variable.    
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
        print("""No worries, I've got just the place! Let's make it""")
        random.choice(destination_list)
        city = random.choice(destination_list)
        print(city)
        
                

def transportation(transpo_list):
    random.choice(transpo_list)
    transpo = random.choice(transpo_list)
    print(f"""How about using {transpo} for travel?""")

    transpo_input = input("Will this work for transportation?: ")
    if transpo_input == "yes":
        print("Great selection!")
    elif transpo_input != "yes":
        random.choice(transpo_list)
        transpo = random.choice(transpo_list)
        print(f"No worries, how about {transpo}")
        transpo_input = input("Will this work?: ")
    if transpo_input == "yes":
        print("""
        
This will be an exciting trip, let's now choose a restaruant!
        
        """)
    elif transpo_input != "yes":
        random.choice(transpo_list)
        transpo = random.choice(transpo_list)
        print(f"""No worries, a {transpo} should fit your needs. Now we'll pick a restaurant.""")
    


def restaurant(food_list):
    random.choice(food_list)
    selection = random.choice(food_list)
    print(f""" 
How about {selection}... """)
    sel_input = input("Does this sound like a good restaurant option?: ")
    if sel_input == "yes":
        print("Great choice!")
    elif sel_input != "yes":
        print("""
No worries, here's another option.""")
        random.choice(food_list)
        selection = random.choice(food_list)
        print(selection)
        sel_input = input(""""
Will this work?""")
    if sel_input == "yes":
        print("""
We just need to get your itinerary.""")
    elif sel_input != "yes":
        print("No worries! I've got just the thing and we'll get your itinerary.")
        random.choice(food_list)
        selection = random.choice(food_list)
        print(selection)
        return(random.choice(food_list))   
     



dtp()

destination()
destination(destination_list=["Los Angeles", "Seattle", "Portland", "Boise", "St Paul", "Chicago"])

transportation(transpo_list=["Commuter Train", "Car", "Public Bus", "Uber", "Taxi", "Limo"])

restaurant(food_list=["TGIF", "Local Favorite", "Red Robin", "Famous Burger Joint", "Steak House"])