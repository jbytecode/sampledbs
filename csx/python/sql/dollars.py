# Description: Simulate the distribution of dollars among 100 people

# Import the random module for selecting random people
import random 

# Number of people and transactions
numpeople = 100
numtransactions = 100000

# 100 people with $100 each
people = [100.0 for i in range(numpeople)]

# Randomly give a dollar to another person
for iterations in range(numtransactions):
    # Randomly select two people
    j = random.randint(0, 99)
    i = random.randint(0, 99)

    # Give a dollar from i to j if i has at least a dollar
    if people[i] > 0:
        people[i] -= 1
        people[j] += 1

# Sort the people by the amount of money they have
people.sort()

# Print the richest and poorest people
print(people)

