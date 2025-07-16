# Create a vector of integers 
x = [1, 2, 3, 4, 5, -6]

# Apply absolute value function to each element
abs_x = map(abs, x)
println("Absolute values: ", abs_x)

# Filter out negative values
filtered_x = filter(x -> x >= 0, x)
println("Filtered values (non-negative): ", filtered_x)

# Function that takes a function as an argument
function apply_func(f, x)
    return f(x)
end

# Apply a function to each element in the vector
applied_x = map(a -> apply_func(abs, a), x)
println("Applied function to each element: ", applied_x)

# Function returning a function
function make_multiplier(factor)
    return x -> x * factor
end

# Create a multiplier function
twice = make_multiplier(2)

# Apply the multiplier function to each element
result = twice(10)

println("Result of multiplying 10 by 2: ", result)
