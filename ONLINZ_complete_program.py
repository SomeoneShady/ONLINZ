# I have created a list that stores each available choice for the user later on
islands = ["North Island (Te Ika a Maui),", "South Island (Te Wai Pounamu)", "Stewart Island (Rakiura)"]

# I have also made a blank list that will act as a catalyst for data that will be extracted from the user later on
customer_details = {}

# I shall create a function that ensures the user submits a valid answer instead of leaving it blank or using numbers
def blank_name(question):
    valid = False

    while not valid:
        response = input(question)

        if response.isdigit():
            print("We cannot serve numbers, please gives us your real name.")
        else:
            while response != "":
                return response
            else:
                print("Haha, very funny. Please gives us your name, we cannot serve the air.")

# I have also made a function that stores three questions the user has to answer, then stores the user input for later use
def box_dimensions():
    width = float(input("How wide is the box in centimetres?"))
    length = float(input("How long is the box in centimetres?"))
    height = float(input("How tall is the box in centimetres?"))
    volume = width * length * height
    return width, length, height, volume

# I have created a function that tells the user what options they can choose from using the list above
def chosen_island():
    print("""Which island are you sending this product from?
          1: The North Island (Te Ika a Muai)
          2: The South Island (Te Wai Pounamu)
          3: The Stewart Island (Rakiura)
           4: None of these""")
    return""

# In order to begin the code, I shall greet the user
name = blank_name("Greetings! What is your name?").title()
print("{}? What a lovely name!".format(name))
print("""Please stand by as we prepare our automated- I mean dedicated employee for the refunding process:""")

# I have set the total cost to 0 as we do not have information yet, this value will change overtime
total_cost = 0

# I have created a loop that stops the user from adding invalid inputs into the code, which would create unexpected outputs
dimensions_repeat = True
while dimensions_repeat == True:
    try:
        print("Alright {}, I'm going to ask you some quick questions, please answer them truthfully:".format(name))
        correct_width, correct_length, correct_height, total_volume = box_dimensions()

        # Check inputs and provide a print statement depending on said inputs.
        if correct_width <= 4.0 or correct_width >= 100.0:
            print("Those are invalid dimensions, I shall now restart the questioning process:")
        elif correct_length <= 4.0 or correct_length >= 100.0:
            print("Those are invalid dimensions, I shall now restart the questioning process:")
        elif correct_height <= 4.0 or correct_height >= 100.0:
            print("Those are invalid dimensions, I shall now restart the questioning process:")
        else:
            print("The total volume of the box is {} cm^3.".format(total_volume))
            dimensions_repeat = False
    except ValueError:
        print("Sorry, we only allow numbers. Please try again.")


# With the data provided by the user, I shall now calculate the base rate and charge the user.
base_rate = total_volume
if base_rate <= 6000.0:
    print("This return will cost you $8.00 so far.")
    total_cost += 8.00
elif base_rate > 6000.0 and base_rate < 10000.0:
    print("This return will cost you $12.00 so far.")
    total_cost += 12.00
else:
    print("This return will cost you $15.00 so far.")
    total_cost += 15.00

print("Now for the next step:")

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
