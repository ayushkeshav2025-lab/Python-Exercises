from math import gcd  # built-in gcd function

# Function to calculate LCM of two numbers
def lcm(x, y):
    return (x * y) // gcd(x, y)

# Function to calculate LCM of a list of numbers
def lcm_of_list(numbers):
    result = numbers[0]
    for num in numbers[1:]:   # iterate from the second element onward
        result = lcm(result, num)
    return result

# Take multiple inputs from user
nums = list(map(int, input("Enter numbers separated by space: ").split()))

print("LCM of", nums, "is", lcm_of_list(nums))