def box_dimensions(width, length, height):
    width = float(input("How wide is the box in centimetres?"))
    length = float(input("How long is the box in centimetres?"))
    height = float(input("How tall is the box in centimetres?"))
    return width * length * height


name = "Bob"

# I Have created a loop that stops the user from adding invalid inputs into the code, which would create unexpected outputs.
correct_dimensions = True
while True:
    print("Alright {}, I'm going to ask you some quick questions, please answer them truthfully:".format(name))
    correct_width = box_dimensions("width")
    correct_length = box_dimensions("length")
    correct_height = box_dimensions("height")

    # Check inputs and provide a print statement depending on said inputs.
    if correct_width <= "4" or correct_width >= "100":
        print("Those are invalid dimensions, please get a different box.")
    elif correct_length <= "4" or correct_length >= "100":
        print("Those are invalid dimensions, please get a different box.")
    elif correct_height == "3" or correct_height >= "100":
        print("Those are invalid dimensions, please get a different box.")
    else:
        total_volume = box_dimensions('width', 'length', 'height')
        print("The total volume of the box is {} cm^3.".format(total_volume))
        correct_dimensions = False
