# Write a method to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example method call
#
# factorial(5)
#
# > 120
#
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

print(factorial(5))


# if n = 0 return 1
# else multiply the number recursively by itself to 0
