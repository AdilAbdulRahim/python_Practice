from utils import get_integer
from user import create_user, check_age, check_number
from storage import add_user, get_all_users

def get_user_info():
    name = input("Enter your name: ")
    age = get_integer("Enter your age: ")
    number = get_integer("Enter your favorite number: ")
    return name, age, number

def view_data():
    try:
        users = get_all_users()
    except Exception:
        print("Error loading data.")
        return 
    
    if not users:
        print("No entries found.")
        return
    
    print("\n--- Saved Users ---")
    for i, user in enumerate(users, 1):
        print(f"{i}. Name:{user['name']} | Age: {user['age']} | Number: {user['number']}")

def main():
    while True:
        print("\n==== MENU ====")
        print("1. Add new entry")
        print("2. View all entries")
        print("3. Exit")

        choice = input("Choose an option ")

        if choice == "1":
            name, age, number = get_user_info()

            check_age(name, age)
            check_number(number)

            user = create_user(name, age, number)
            add_user(user)

        elif choice == "2":
            view_data()

        elif choice == "3":
            print("Goodbye!")
            break
        else: print("Invalid Option")

if __name__ == "__main__":
    main()