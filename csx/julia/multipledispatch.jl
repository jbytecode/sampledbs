struct Point2D
    x::Float64
    y::Float64
end

function Base.:+(a::Point2D, b::Point2D)::Point2D
    return Point2D(a.x + b.x, a.y + b.y)
end

function Base.:-(a::Point2D, b::Point2D)::Point2D
    return Point2D(a.x - b.x, a.y - b.y)
end

function Base.:*(a::Point2D, b::Point2D)::Float64
    return a.x * b.x + a.y * b.y
end

p1 = Point2D(1, 2)
p2 = Point2D(3, 4)

println(p1 + p2)
println(p1 - p2)
println(p1 * p2)

# Output:
# Point2D(4.0, 6.0)
# Point2D(-2.0, -2.0)
# 11.0