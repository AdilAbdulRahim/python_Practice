# name = "Adil" #string
# age = 24 #int
# height = 177.8 #float
# country = "Canada" #string

# is_developer = input("Are you a developer? (y/N): ").lower() == "y"

# print(f"My name is {name}.")
# print(f"I am {age} years old.")
# print(f"I am {height}cm tall.")
# print(f"I currently live in {country}.")

# if is_developer:
#     print("I am a developer.")
# else:
#     print("I am not a developer.")

# if age <13:
#     print("You are a child.")
# elif age >= 13 and age <= 17: #Improvement 13 <= age <= 17
#     print("You are a teen.")
# else:
#     print("You are an adult.")


# for i in range (1,11): #Improvement for i in range (1,11):
#     if i % 2 ==0:
#         print(i)

# i = 0

# while i != 5: #safer i < 5:
#     i += 1
#     print(i)

# def greet(name):
#     print(f"Hello, {name}")

# def main():
#     name = input("What is your name? ")
#     greet(name)

# main()

# def is_even(number):
#     if number % 2 == 0:
#         print("Your number is even")
#     else:
#         print("Your number is odd")

# def main():
#     number = int(input("Pick any number: "))
#     is_even(number)

# main()

# #Improvement: handle print functions separately

# def is_even(number):
#     return number % 2 == 0

# def main():
#     number = int(input("Pick any number: "))

#     if is_even(number):
#         print("Your number is even")
#     else:
#         print("Your number is odd")

# main()


# def multiply(a,b):
#     return a * b

# def main():
#     a = int(input("Enter your first number: "))
#     b = int(input("Enter your second number: "))

#     result = multiply(a, b)
#     print(f"The product of your numbers is: {result}")

# main()

# numbers = [1, 2, 3, 4, 5]

# print(numbers)
# print(numbers[0])
# print(numbers[4]) #Improvement use -1 instead of 4

# numbers = [1, 2, 3, 4, 5]

# for i in numbers: #Improvement use better variables like for number in numbers
#     print(i)

# total = 0

# numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     total += number

# print (total)

# user = {
#     "name" : "Ben",
#     "age" : 22,
#     "country" : "Britain"
#     }

# print(user)
# print(user["name"]) #Improvement print(f"Name: {user['name']}")

# user = {
#     "name" : "Ben",
#     "age" : 22,
#     "country" : "Britain"
#     }

# user["age"] = 30
# user["job"] = "programmer"
# print(user)

# user = {
#     "name" : "Ben",
#     "age" : 22,
#     "address" : {
#         "country" : "Canada",
#         "city" : "Halifax"
#     }
# }
# # print(user)
# print(user["address"]["city"])

# with open("notes.txt", "w") as file:
#     file.write("Hello World")

# with open("notes.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("notes.txt", "a") as file:
#     note = input("Write something to contribute to the notes: \n")
#     file.write("\n")
#     file.write(note)

# with open("notes.txt", "r") as file:
#     updated_content = file.read()
#     print(updated_content)

# while True: 
#     number = input("Enter a number: ")

#     try: 
#         number = int(number)
#         print(f"Your number is: {number}")
#         break

#     except: #Improvement: Avoid bare except ex: except ValueError:...
#         print("Enter a valid number")

# sentence = input("Enter your favorite sentence: ")
# print(f"Uppercase: {sentence.upper()}")
# print(f"Lowercase: {sentence.lower()}")
# print(f"Length: {len(sentence)}")


# numbers = []
# for i in range (0,5):
#     number = int(input("Enter numbers to add to a list: "))
#     numbers.append(number)

# print(numbers)

# total = 0 

# for i in range(len(numbers)): #Improvement: for number in number
#     total += numbers[i] #Improvement: total += number

# print(f"The sum of all the numbers in the list is: {total}")

def find_largest(number):
    largest = 0 #Improvement: largest = list[0] so that it can take in negative values
    for num in number:
        if num > largest:
            largest = num
    return largest
    

def main():
    number = [50,10,3,20,5]
    largest = find_largest(number)
    print(f"The largest number in the list is: {largest}")

main()





