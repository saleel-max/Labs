import random
import math
import datetime

name = input("Your name: ")
print("Hi", name + "!", "Your lucky number is", random.randint(1, 10))

num = float(input("Enter a number: "))
print("Square root:", math.sqrt(num))

now = datetime.datetime.now()
print("Time:", now.strftime("%H:%M:%S"), "Date:", now.strftime("%Y-%m-%d"))
