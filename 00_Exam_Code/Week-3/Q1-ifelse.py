# Write a Python program to check whether a number entered by the user is
# positive, negative, or zero.

num = int(input("Enter a number: "))

if num > 0:
    print(f"{num} is a positive number.")
elif num < 0:
    print(f"{num} is a negative number.")
else:
    print(f"Given number is {num}.")