def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def substract(a, b):
    print "Substract %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Dividing %d / %d" % (a, b)
    return a / b

print "Lets do some math with just functions!"

age = add(30, 5)
height = substract(184, 2)
weight = multiply(90, 2)
iq = divide(300,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#A puzzle for extra credit, type it in anyway
print "Here is a puzzle:"

what = add(age,substract)
