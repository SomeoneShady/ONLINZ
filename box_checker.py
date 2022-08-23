def box_dimensions():
    width = float(input("How wide is the box in centimetres?"))
    length = float(input("How long is the box in centimetres?"))
    height = float(input("How tall is the box in centimetres?"))
    volume = width * length * height
    return width, length, height, volume


name = "Bob"

# I Have created a loop that stops the user from adding invalid inputs into the code, which would create unexpected outputs.
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
