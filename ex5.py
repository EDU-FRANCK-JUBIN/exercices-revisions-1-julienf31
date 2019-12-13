from pyDatalog import pyDatalog

pyDatalog.create_terms('X')
pyDatalog.create_terms('blue, yellow, red, green, purple')
pyDatalog.create_terms('isBehind, isAbove, first')


first(X) <= isBehind(X) == False


# V not first
# V isBehind B
# R isAbove P
# Y and R not following


# B P Y G R