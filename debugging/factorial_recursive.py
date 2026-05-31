#!/usr/bin/python3
import sys

# Function Description:
# Calculates the factorial of a non-negative integer using recursion.
#
# Parameters:
# n (int): The number for which the factorial is calculated.
#
# Returns:
# int: The factorial of n.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
