# Create a dictionary object 
d = Dict()

# Add some elements 
d["a"] = 1
d["pi"] = 3.14
d["e"] = 2.71828

# Print the contents of the dictionary
println(d)

# Create with elements 
d2 = Dict("a" => 1, "pi" => 3.14, "e" => 2.71828)

# Print the contents of the second dictionary
println(d2)

# Loop the dictionary with its keys and values 
for (key, value) in d2
    println("Key: $key, Value: $value")
end

# Change the value
d2["a"] = -1

# Print again 
for (key, value) in d2 
	println("Key: $key, Value: $value")
end 
