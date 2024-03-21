class TransportationTable:
    def __init__(self, costs, supply, demand):
        self.costs = costs 
        self.supply = supply
        self.demand = demand 

    def isbalanced(self):
        return sum(self.supply) == sum(self.demand)
    
    def numsupply(self):
        return len(self.supply)
    
    def numdemand(self):
        return len(self.demand)
    

    

t = TransportationTable([[2, 3, 6], [4, 5, 1]], [20, 30], [10, 15, 25])
print("Balanced: {}, Num supply: {}, Num demand: {}".format(t.isbalanced(), t.numsupply(), t.numdemand()))
