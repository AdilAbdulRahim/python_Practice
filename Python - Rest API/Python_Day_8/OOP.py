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
       print(f"You have deposited ${amount}, you remaining balance is: ${self.balance}")
       self.balance += amount
       
    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            print(f"You have withdrawn ${amount}, you remaining balance is: ${self.balance}")
        elif amount > self.balance:
            print(f"You do not have enough funds to withdraw {amount}")
        else:
            print("Please enter a valid amount")

    def show_balance(self):
        print(f"Balance: ${self.balance}")

cx = BankAccount("Ben", 4000)


print("--------------------\n Welcome to The Bank\n--------------------")

while True:
   try:
      menu = int(input("""Would you like to:
1. Deposit
2. Withdraw
3. See Balance
4. Exit
Your input: """))
   
      if menu == 1:     
         while True:
            try:
               d_amount = int(input("How much would you like to deposit?\n$")) 
               if d_amount <= 0:
                  print("Please enter a valid amount.")
               else:
                  cx.deposit(d_amount)
                  break
            except ValueError:
               print("Please enter a valid amount.")
      elif menu == 2:
         while True:
            try:
               w_amount = int(input("How much would you like to withdraw?\n$"))
               if w_amount <= 0:
                  print(f"Please enter a valid amount.")
               else:
                  cx.withdraw(w_amount)
                  break
            except ValueError:
               print("Please enter a valid amount.")
      elif menu == 3:
         cx.show_balance()
      elif menu == 4:
         break
      else:
         print("Please enter a valid number.")
   except ValueError:
      print("Please select one of the listed options.")

   

    