# DeVillaCharlene_CS2_ActSet1.py
# Program to Store and Display Student Personal Information Using Dictionaries

# Step 2: Create empty dictionary
student = {}

# Step 3: Collect input from user
student["name"] = input("Enter your name: ")
student["age"] = input("Enter your age: ")
student["subject"] = input("Enter your favorite subject: ")

# Step 5: Print information in clear format
print("\nStudent Record:")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Favorite Subject: {student['subject']}")
