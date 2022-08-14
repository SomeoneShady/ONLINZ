# I shall create a function that ensures the user submits a valid answer instead of leaving it blank (in this case a name)
def anti_blank(question):
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
name = anti_blank("Greetings! What is your name?")
print("{}? What a wonderful name!".format(name))
