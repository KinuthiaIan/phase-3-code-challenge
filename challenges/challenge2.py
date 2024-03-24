'''
write a function, which takes three integers a, b, and c as arguments, 
and returns True if exactly two of of the three integers are positive numbers (greater than zero), and False - otherwise.
'''

# Defining the function


def exactly_two_positive(a, b, c):
    # Initializing the number of positive integers to zero
    positive_int_count = 0

    # With every condition met below, add 1 to the count of positive integers
    if a > 0:
        positive_int_count += 1
    if b > 0:
        positive_int_count += 1
    if c > 0:
        positive_int_count += 1

        # Check if exactly two of the integers are positive and return true or false
    return positive_int_count == 2


    # Calling the function with examples
print(exactly_two_positive(1, 2, 3))  # False
print(exactly_two_positive(2, 4, -3))  # True
print(exactly_two_positive(-4, 6, 8))  # True
print(exactly_two_positive(4, -6, 9))  # True
print(exactly_two_positive(-4, 6, 0))  # False
print(exactly_two_positive(4, 6, 10))  # False
print(exactly_two_positive(-14, -3, -4))  # False
