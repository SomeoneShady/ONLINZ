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


# Greet the user and ask for their name
name = blank_name("Greetings! What is your name?").title()
print("{}? What a lovely name!".format(name))
