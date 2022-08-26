customer_details = {}


print("Before we send you the receipt, we're going ask you a few more questions:")
name = "Bob"
last_name = input("What is your last name?")
address = input("What is your address?")
phone_number = input("What is your telephone number?")
customer_details["First Name"] = name
customer_details["Last Name"] = last_name
customer_details["Address"] = address
customer_details["Phone Number"] = phone_number
print(customer_details)
