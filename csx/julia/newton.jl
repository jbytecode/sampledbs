using ForwardDiff
using LinearAlgebra

function newton(f, start, eps = 0.00001)
    x = start 
    while true 
        @info "Current x: $x"
        newx = x - ForwardDiff.hessian(f, x)^(-1) * ForwardDiff.gradient(f, x)
        if sum(abs.(newx - x)) < eps
            return newx
        end
        x = newx
    end
end

function f(x)
    return x[1]^2 + x[2]^2 - 2*x[1] - 4*x[2] + 5
end

start = [10.0, -15.0]
result = newton(f, start)
println("Minimum found at: ", result)