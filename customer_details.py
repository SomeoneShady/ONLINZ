# I have made a blank list that will act as a catalyst for data that will be extracted from the user later on
customer_details = {}

# I shall now make a series of inputs that provides me with te information I need in order to remember the user if they appear again
print("Before we send you the receipt, we're going ask you a few more questions:")
name = "Bob"
last_name = input("What is your last name?")
address = input("What is your address?")
phone_number = input("What is your telephone number?")
customer_details["First Name"], customer_details["Last Name"], customer_details["Address"], customer_details["Phone Number"], = name, last_name, address, phone_number

# I will now print out the list, allowing the user to confirm if this data is correct
print(customer_details)
