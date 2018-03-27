# Write a method called `p_times` that takes a `statement` and
# a `num` as inputs, and outputs the `statement` some `num` of times
# to the console.
#
# Example method call:
#
# p_times('Hello there', 1)
#
# > Hello there
#
# p_times('Hello there', 3)
#
# > Hello there
# > Hello there
# > Hello there

# print sting on same line n number of times
def p_times(string, num):
    print((string + " ") * num)

p_times('Hello', 4)


# print string on individual line n number of times
def p_times(string, num):
    for i in range(num):
        print (string)

p_times('help me', 5)
