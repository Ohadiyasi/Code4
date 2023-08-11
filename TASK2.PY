import random

def fillList(n):
    numbers = random.sample(range(1, n+1), n)
    return numbers

n = int(input("Enter the number of elements in the list: "))
result = fillList(n)
print("The list without repeats:", result)
