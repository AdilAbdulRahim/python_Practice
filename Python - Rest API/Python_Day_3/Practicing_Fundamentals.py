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

# def find_largest(number):
#     largest = 0 #Improvement: largest = list[0] so that it can take in negative values
#     for num in number:
#         if num > largest:
#             largest = num
#     return largest
    

# def main():
#     number = [50,10,3,20,5]
#     largest = find_largest(number)
#     print(f"The largest number in the list is: {largest}")

# main()

# def contains_number(numbers, target_number):
#     for number in numbers:
#         if number == target_number:
#             return True
#     return False
    
        
# def main():
#     numbers = []
#     for i in range (5):
#         number = int(input("Enter 5 numbers to be on your list: "))
#         numbers.append(number)
#     target_number = int(input("what number would you like to check to see if it is on the list: "))
#     match = contains_number(numbers, target_number)
#     print(match)

# main()

# def count_occurrences (numbers, target_number):
#     count = 0
#     for number in numbers:
#         if number == target_number:
#             count += 1
#     return count
        
# def main():
#     numbers = []
#     for i in range(5):
#         number = int(input(f"Enter {i+1} numbers to be on your list: "))
#         numbers.append(number)
#     target_number = int(input("What number would you like to count: "))
#     count = count_occurrences(numbers, target_number)
#     print(f"The number appears {count} times.")

# main()

# def remove_duplicates(numbers):
#     no_dupe = []
#     for num in numbers:
#         if num not in  no_dupe:
#             no_dupe.append(num)
#     return no_dupe

# def main():
#     numbers = [1,1,2,2,2,3,4,5,5,6]
#     test = remove_duplicates(numbers)
#     print(f"Here is the list without duplicates: {test}")

# main()

# def find_smallest(numbers):
#     smallest = numbers[0]
#     for num in numbers:
#         if num < smallest:
#             smallest = num
#     return smallest

# def main():
#     numbers = [0,-4,2,3,-10]
#     test = find_smallest(numbers)
#     print(f"The smallest value in the list is: {test}")

# main()

# def count_vowels(sentence):
#     vowels = 0
#     for letter in sentence:
#         if letter.lower() in ('a', 'e', 'i', 'o', 'u'):
#             vowels  += 1
#     return vowels

# def main():
#     sentence = input("Enter a sentence: ")
#     test = count_vowels(sentence)
#     print(f"There are {test} vowel(s) in the sentence")

# main()

# def reverse_string(sentence):
#     reversed_text = ""
#     for letter in range(len(sentence) -1, -1, -1):
#         reversed_text += sentence[letter]
#     return reversed_text

# def main():
#     sentence = input("Enter a sentence to reverse: ")
#     test = reverse_string(sentence)
#     print(f"Your string reversed is as follows: {test}")

# main()