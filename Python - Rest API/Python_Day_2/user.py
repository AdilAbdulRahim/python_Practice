def create_user(name, age, number):
    return {
        "name": name, 
        "age": age, 
        "number": number
    }

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
        print("Your favorite number is more than 100.")
    elif number < 100: 
        print("Your favorite number is less than 100.")
    else:
        print("Your favorite number is 100.")

    if number > 0: 
        print("Your number is positive.")
    elif number < 0: 
        print("Your number is negative.")
    else:
        print("Your numebr is zero.")