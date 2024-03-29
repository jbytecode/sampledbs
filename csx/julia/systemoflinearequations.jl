# x + 2y + z = 14
# 2x + 3y + 2z = 24
# 3x + 4y + 2z = 29

A = Float64[1 2 1; 2 3 2; 3 4 2]
b = Float64[14, 24, 29]

result = A\b
result2 = inv(A'A)*A'b

println(result)
println(result2)

# Output: [1.0, 4.0, 5.0]