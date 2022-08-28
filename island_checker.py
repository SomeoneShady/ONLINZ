# I have created a list that stores each avaliable choice for the user later on
islands = ["North Island (Te Ika a Maui),", "South Island (Te Wai Pounamu)", "Stewart Island (Rakiura)"]

# I have created a function that tells the user what options they can choose from using the list above
def chosen_island():
    print("""Which island are you sending this product from?
          1: The North Island (Te Ika a Muai)
          2: The South Island (Te Wai Pounamu)
          3: The Stewart Island (Rakiura)
           4: None of these""")
    return""

print("Alright, now for the final step:")

# I have set the total cost to 8 so it functions with the next code, but this will change when combined with the other files
total_cost = 8.0

# I have created a while loop that changes the total cost based on the chosen island from the list above
valid_island = True
while valid_island == True:
    island = input(chosen_island())
    try:
        if island == "1":
            print("You have chosen The North Island, no additional charges will be applied.")
            valid_island = False
        elif island == "2":
            print("You have chosen The South Island, additional charges will now be applied.")
            total_cost *= 1.5
            valid_island = False
        elif island == "3":
            print("You have chosen The Stewart Island, additional charges will now be applied.")
            total_cost *= 2
            valid_island = False
        elif island == "4":
            new_island = input("Oh? You don't live on any of these islands? Please add which Island you live on then.")
            islands.append(new_island)
            print(islands, """
            Is this correct? We won't add any additional charges as we need to calculate
            the shipping fees for that location, I guess it's your lucky break!""")
            valid_island = False
        else:
            print("I'm sorry that wasn't an option, please try again.")

    except ValueError:
        print("I'm sorry that wasn't an option, please try again.")

# I have made one final print statement that shows the user how much they need to pay after modifications
print("The total amount you will have to pay is: ${}".format(total_cost))
