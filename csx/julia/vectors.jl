# Create a vector of integers 
x = [1, 2, 3, 4, 5]

# Create a vector of floats
y = [1.0, 2.0, 3.0, 4.0, 5.0]

# Type of vector x
println("Type of vector x: ", typeof(x))

# Type of vector y
println("Type of vector y: ", typeof(y))

# Length of vector x
println("Length of vector x: ", length(x))

# Length of vector y
println("Length of vector y: ", length(y))

# Accessing elements of vector x
println("First element of vector x: ", x[1])
println("Second element of vector x: ", x[2])
println("Last element of vector x: ", x[end])

# Changing an element in vector x
x[1] = 10
println("Modified vector x: ", x)

# Adding two vectors
z = x .+ y

println("Sum of vectors x and y: ", z)

# Appending an element to vector x
push!(x, 6)
println("Vector x after appending 6: ", x)

# Removing the last element from vector x
pop!(x)
println("Vector x after removing the last element: ", x)

# Inserting an element at a specific position in vector x
insert!(x, 2, 20)
println("Vector x after inserting 20 at position 2: ", x)

# Iterating elements of vector x
for element in x
    println("Element: ", element)
end

# Iterating with index
for (index, element) in enumerate(x)
    println("Element at index $index: ", element)
end

# Summing elements of vector x
sum_x = sum(x)
println("Sum of elements in vector x: ", sum_x)

# Finding the maximum element in vector x
max_x = maximum(x)
println("Maximum element in vector x: ", max_x)

# Finding the minimum element in vector x
min_x = minimum(x)
println("Minimum element in vector x: ", min_x)

# Finding the minimum and maximum elements in vector x at the same time
min_x, max_x = extrema(x)
println("Minimum element in vector x: ", min_x)
println("Maximum element in vector x: ", max_x)

