class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y
    
    def __str__(self):
        return "Point2D({},{})".format(self.x, self.y)
    

# Create two points
p1 = Point2D(1, 2)
p2 = Point2D(3, 4)

# Add the points
p3 = p1 + p2

# Subtract the points
p4 = p1 - p2

# Multiply the points
p5 = p1 * p2

# Print the results
print(p3)
print(p4)

    
