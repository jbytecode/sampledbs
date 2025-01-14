# This program calculates the square root of a number using the Heron method.
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots

def heronstep(initial, x):
    return 0.5 * (initial + x / initial)

def heron(initial, x):
    while True:
        newinitial = heronstep(initial, x)
        if newinitial == initial:
            return newinitial
        initial = newinitial

# Find the square root of 25
print("The square root of 25 is", heron(1, 25))