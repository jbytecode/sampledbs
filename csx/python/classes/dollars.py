# Agent based model of the dollar game
# All agents start with 100 dollars
# At each time step, a random agent gives one dollar to another random agent
# The model is run for 1000000 time steps
# The agents are then sorted in descending order of the amount of dollars they have
# The agent with the most dollars is the winner
 
import random 

class Person:
    def __init__(self, amount):
        self.amount = amount
    
    def getOne(self):
        self.amount += 1

    def giveOne(self):
        self.amount -= 1
    
    def hasDollars(self):
        return self.amount >= 1
    
    def __repr__(self):
        return f"Person has {self.amount} dollars"
    

npeople = 100
ntries = 1000000
people = [Person(100) for i in range(npeople)]

for i in range(ntries):
    p1 = random.choice(people)
    p2 = random.choice(people)
    if p1.hasDollars():
        p1.giveOne()
        p2.getOne()


people.sort(key=lambda x: x.amount, reverse=True)
print(people)
