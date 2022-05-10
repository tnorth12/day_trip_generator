import random

def destination(destination_list):    
    print("Would you like to visit?")
    random.choice(destination_list)    
    city = random.choice(destination_list) 
    print(city)                                       #how do I keep from generating same rando city? I now see I can delete from lists since I named the variable.    
    user_input =  input("Do you like this location?: ")
    if user_input == "yes":
        print(f"Great selection in choosing {city}!")
        return destination_list        
    elif user_input != "yes":
        print("No worries, we have other exciting locations. How about?")
        random.choice(destination_list)
        city = random.choice(destination_list)
        print(city)
        user_input = input("Do you like this location?: ")
    if user_input == "yes":
        print(f"This will be an exciting trip! Now that you've selected {city} let's move on to how you'd like to travel.""")
        return destination_list
    elif user_input != "yes":
        print("""No worries, I've got just the place! Let's make it""")
        random.choice(destination_list)
        city = random.choice(destination_list)
        print(city)
        return destination_list






destination(destination_list=["Los Angeles", "Seattle", "Portland", "Boise", "St Paul", "Chicago"])
