import json
import os

def save_to_file(name, age, number):
    data = []

    if os.path.exists("user_data.json"):
        with open("user_data.json", "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    
    data.append({
        "name": name, 
        "age": age, 
        "number": number
    })

    with open ("user_data.json", "w") as file:
        json.dump(data, file, indent=4)

def view_data():
    if not os.path.exists("user_data.json"):
        print("No data found.")
        return
    with open("user_data.json", "r") as file:
        data = json.load(file)
    
    if not data:
        print("No entries found.")
        return
    
    print("\n--- Saved Users ---")
    for i, user in enumerate(data, 1):
        print(f"{i}. Name: {user['name']} | Age: {user['age']} | Number: {user['number']}")

def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_user_info():
    name = input("Enter your name: ")
    age = get_integer("Enter your age: ")
    number = get_integer("Enter a number: ")
    return name, age, number


def check_age(name, age):
    print(f"Hello {name}, you are {age} years old.")

    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")


def check_number(number):
    if number % 2 == 0:
        print("Your favorite number is even.")
    else:
        print("Your favorite number is odd.")

    if number > 100:
        print("Your favorite number is greater than 100.")
    elif number < 100:
        print("Your favorite number is less than 100.")
    else:
        print("Your favorite number is equal to 100.")

    if number > 0:
        print("Your favorite number is positive.")
    elif number < 0:
        print("Your favorite number is negative.")
    else:
        print("Your favorite number is zero.")


def main():
    while True:
        print("\n==== MENU ====")
        print("1. Add new entry")
        print("2. View all entries")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name, age, number = get_user_info()

            check_age(name, age)
            check_number(number)

            save_to_file(name, age, number) 

        elif choice == "2":
            view_data()

        elif choice == "3":
            print("Goodbye")
            break

        else:
            print("\n\nInvalid option")


main()

        

