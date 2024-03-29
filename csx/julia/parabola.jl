function get_delta(a, b, c)
    return b^2 - 4*a*c
end

function get_number_of_roots(a, b, c)
    delta = get_delta(a, b, c)
    if delta > 0
        return 2
    elseif delta == 0
        return 1
    else
        return 0
    end
end

function get_roots(a, b, c)
    delta = get_delta(a, b, c)
    if delta > 0
        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)
        return x1, x2
    elseif delta == 0
        x1 = (-b - sqrt(delta)) / (2*a)
        return r
    else
        return nothing
    end
end

# example 
p1 = -1
p2 = 2
p3 = 10
println(get_number_of_roots(p1, p2, p3))
println(get_roots(p1, p2, p3))
