
# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print("Amount deposited successfully!")
#         else:
#             print("Invalid amount!")

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Invalid amount!")
#         elif amount > self.__balance:
#             print("Insufficient balance!")
#         else:
#             self.__balance -= amount
#             print("Withdrawal successful!")

#     def check_balance(self):
#         print("Current Balance:", self.__balance)


# account = BankAccount("Shwetha", 5000)

# print("Account Holder:", account.name)

# account.deposit(2000)
# account.withdraw(1000)
# account.check_balance()

# account.withdraw(10000)
# account.deposit(-500)


# class Book:
#     def __init__(self, title):
#         self.title = title
#         self.available = True

#     def issue_book(self):
#         if self.available:
#             self.available = False
#             print(self.title, "issued successfully!")
#         else:
#             print(self.title, "is not available!")

#     def return_book(self):
#         if not self.available:
#             self.available = True
#             print(self.title, "returned successfully!")
#         else:
#             print(self.title, "was not issued!")

#     def display(self):
#         if self.available:
#             print(self.title, "- Available")
#         else:
#             print(self.title, "- Not Available")


# class Library(Book):
#     def __init__(self, title):
#         super().__init__(title)


# book1 = Library("Python Programming")

# book1.display()
# book1.issue_book()
# book1.display()
# book1.return_book()
# book1.display()



import random

rolls = int(input("Enter number of rolls: "))

frequency = [0] * 6

for i in range(rolls):
    dice = random.randint(1, 6)
    print("Roll", i + 1, ":", dice)
    frequency[dice - 1] += 1

print("\nFrequency of each number:")

for i in range(6):
    print(i + 1, "appeared", frequency[i], "times")

