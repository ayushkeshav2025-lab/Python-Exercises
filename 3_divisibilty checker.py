# Divisibility and Multiples Checker

# Taking input from the user
number = int(input("Enter a number: "))

# Checking divisibility by 7 and multiple of 5
if number % 7 == 0 and number % 5 == 0:
    print(f"{number} is divisible by 7 and a multiple of 5.")
elif number % 7 == 0:
    print(f"{number} is divisible by 7 but not a multiple of 5.")
elif number % 5 == 0:
    print(f"{number} is a multiple of 5 but not divisible by 7.")
else:
    print(f"{number} is neither divisible by 7 nor a multiple of 5.")
