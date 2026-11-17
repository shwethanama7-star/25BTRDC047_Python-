# import random

# number = random.randint(1, 10)

# guess = int(input("Guess a number between 1 and 10: "))

# if guess == number:
#     print("Correct! You guessed the number.")
# else:
#     print("Wrong! The number was", number)

# n = int(input("Enter a number: "))

# if n < 2:
#     print(n, "is not a prime number")
# else:
#     prime = True

#     for i in range(2, n):
#         if n % i == 0:
#             prime = False
#             break

#     if prime:
#         print(n, "is a prime number")
#     else:
#         print(n, "is not a prime number")

# n = int(input("Enter a number: "))

# factorial = 1

# for i in range(1, n + 1):
#     factorial = factorial * i

# print("Factorial:", factorial)

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# n = int(input("Enter number of terms: "))

# for i in range(n):
#     print(fibonacci(i), end=" ")