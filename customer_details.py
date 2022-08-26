customer_details = {}


print("Before we send you the receipt, we're going ask you a few more questions:")
name = "Bob"
last_name = input("What is your last name?")
address = input("What is your address?")
phone_number = input("What is your telephone number?")
customer_details["First Name"], customer_details["Last Name"], customer_details["Address"], customer_details["Phone Number"], = name, last_name, address, phone_number

print(customer_details)
