# I have made a function that stores three questions the user has to answer, then stores the user input for later use
def box_dimensions():
    width = float(input("How wide is the box in centimetres?"))
    length = float(input("How long is the box in centimetres?"))
    height = float(input("How tall is the box in centimetres?"))
    volume = width * length * height
    return width, length, height, volume

# I have set temporary values that will be changed once all code files have been combined
name = "Bob"
volume_cost = 0

# I have created a loop that stops the user from adding invalid inputs into the code, which would create unexpected outputs
dimensions_repeat = True
while dimensions_repeat == True:
    try:
        print("Alright {}, I'm going to ask you some quick questions, please answer them truthfully:".format(name))
        correct_width, correct_length, correct_height, total_volume = box_dimensions()

        # Check inputs and provide a print statement depending on said inputs.
        if correct_width <= 4.0 or correct_width >= 100.0:
            print("Those are invalid dimensions, please get a different box.")
        elif correct_length <= 4.0 or correct_length >= 100.0:
            print("Those are invalid dimensions, please get a different box.")
        elif correct_height == 3.0 or correct_height >= 100.0:
            print("Those are invalid dimensions, please get a different box.")
        else:
            print("The total volume of the box is {} cm^3.".format(total_volume))
            dimensions_repeat = False
    except ValueError:
        print("Sorry, we only allow numbers. Please try again.")

# With the data provided by the user, I shall now calculate the base rate and charge the user.
base_rate = total_volume
if base_rate <= 6000.0:
    print("This return will cost you $8.00")
    volume_cost += 8.00
elif base_rate > 6000.0 and base_rate < 10000.0:
    print("This return will cost you $12.00")
    volume_cost += 12.00
else:
    print("This return will cost you $15.00")
    volume_cost += 15.00

print("Thank you for your time, you will now be charged ${}, we hope to see you again!".format(volume_cost))
