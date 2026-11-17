# 1. Required Inputs
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
section = input("Enter your section: ").strip()
favorite_subject = input("Enter your favorite subject: ").strip()

# 2. String Formatting
proper_full_name = f"{first_name} {last_name}".title()

upper_full_name = proper_full_name.upper()
upper_section = section.upper()

proper_subject = favorite_subject.title()

name_length = len(proper_full_name)

# 3. Required Output
print("\n--- Formatted Student Information ---")
print(f"Full Name (Proper Format): {proper_full_name}")
print(f"Full Name (Uppercase): {upper_full_name}")
print(f"Section: {upper_section}")
print(f"Favorite Subject: {proper_subject}")
print(f"Number of Characters in Full Name: {name_length}")
