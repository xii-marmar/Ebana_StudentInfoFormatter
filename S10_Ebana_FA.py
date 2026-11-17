# Required Inputs
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
section = input("Enter your section: ")
favorite_subject = input("Enter your favorite subject: ")

# Combine first and last name
full_name = first_name + " " + last_name

# Basic Output (unformatted)
print("\n--- Student Information ---")
print("Full Name:", full_name)
print("Full Name (Uppercase):", full_name)
print("Section:", section)
print("Favorite Subject:", favorite_subject)
print("Character Count:", len(full_name))