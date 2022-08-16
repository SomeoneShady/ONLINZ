def box_dimensions(width, length, height):
    width = float(input("How wide is the box in centimetres?"))
    length = float(input("How long is the box in centimetres?"))
    height = float(input("How tall is the box in centimetres?"))
    return width * length * height


name = "Bob"
print("Alright {}, I'm going to ask you some quick questions, please answer them truthfully:".format(name))

total_volume = box_dimensions('width', 'length', 'height')
print("The total volume of the box is {}cm cubed.".format(total_volume))
