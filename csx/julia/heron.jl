# Heron's method for computing the square root of a number.
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots

function heronstep(initial, value)
    return 0.5 * (initial + value / initial) 
end

function heron(initial, value)
    x = initial
    while true
        y = heronstep(x, value)
        if y == x
            break
        end
        x = y
    end
    return x
end

result = heron(1.0, 25.0)
println("Square root of 25 is $result")

