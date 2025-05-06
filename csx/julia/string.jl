# String definition 

s = "Hello, World!"

# Upper and lower case
s_upper = uppercase(s)
s_lower = lowercase(s)
println("Uppercase is $s_upper")  # Output: HELLO, WORLD!
println("Lowercase is $s_lower")  # Output: hello, world!

# String concatenation
s2 = " How are you?"
s3 = s * s2
println(s3)  # Output: Hello, World! How are you?


# String interpolation
name = "Ali"
age = 25
greeting = "Hello, my name is $name and I am $age years old."
println(greeting)  # Output: Hello, my name is Ali and I am 25 years old.


# String length
s_length = length(s)
println("Length of string: $s_length")  # Output: Length of string: 13

# String indexing
first_char = s[1]
println("First character: $first_char")  # Output: First character: H

# String slicing
s_slice = s[1:5]
println("Slice of string: $s_slice")  # Output: Slice of string: Hello

# startswith and endswith
s_start = startswith(s, "Hello")
s_end = endswith(s, "World!")
println("Starts with 'Hello': $s_start")  # Output: Starts with 'Hello': true
println("Ends with 'World!': $s_end")  # Output: Ends with 'World!': false

# String replacement
s_replaced = replace(s, "World" => "Julia")
println("Replaced string: $s_replaced")  # Output: Replaced string: Hello, Julia!


# String splitting
s_split = split(s, ", ")
println("Split string: $s_split")  # Output: Split string: ["Hello", "World!"]

# findall
s_find = findall('o', s)
println("Indices of 'o': $s_find")  # Output: Indices of 'o': [5, 8]

# findfirst
s_find_first = findfirst('o', s)
println("First index of 'o': $s_find_first")  # Output: First index of 'o': 5

# Iterating over characters
for c in s
    println(c)
end
# Output:
# H
# e
# l
# l
# o
# ,
#
# W
# o
# r
# l
# d
