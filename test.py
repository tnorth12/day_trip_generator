import random


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
        






restaurant(food_list=["TGIF", "Local Favorite", "Red Robin"])