from random import randint

lower = int(input("Enter the lower boundary: "))
upper = int(input("Enter the upper boundary: "))

rand_num = randint(lower, upper)

print(rand_num, "is between ", lower, " and ", upper)