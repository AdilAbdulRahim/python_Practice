# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("Adil", 24)


# print(p1.name)
# print(p1.age)

# class Car:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year

#     def display_info(self):
#         print(f"Brand {self.brand}")
#         print(f"Year: {self.year}")

# c1 = Car("Toyota", 2012)

# c1.display_info()

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(self.balance)

cx = BankAccount("Ben", 4000)

cx.withdraw(400)
cx.show_balance()
cx.deposit(400)
cx.show_balance()
