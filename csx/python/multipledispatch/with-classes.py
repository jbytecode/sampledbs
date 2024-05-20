import multipledispatch

# Originally the term "multiple dispatch" comes from Julia programming language.
# In Julia, you can define multiple methods with the same name, but different signatures.
# In Python, you can use the multipledispatch library to achieve the same effect.

# In this example we will define a function add that can take two integers, two Vector2d objects, 
# or an integer and a Vector2d object.

class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector2d({self.x}, {self.y})"
    

@multipledispatch.dispatch(int, int)
def add(x, y):
    return x + y


@multipledispatch.dispatch(Vector2d, Vector2d)
def add(v1, v2):
    return Vector2d(v1.x + v2.x, v1.y + v2.y)

@multipledispatch.dispatch(Vector2d, int)
def add(v, i):
    return Vector2d(v.x + i, v.y + i)

@multipledispatch.dispatch(int, Vector2d)
def add(i, v):
    return Vector2d(i + v.x, i + v.y)

v1 = Vector2d(1, 2)
v2 = Vector2d(3, 4)

print(add(v1, v2)) # Vector2d(4, 6)

print(add(v1, 1)) # Vector2d(2, 3)

print(add(1, v1)) # Vector2d(2, 3)

print(add(5, 4))

