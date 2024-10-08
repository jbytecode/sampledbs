# Fibonacci Numbers as Determinants 

$$
F_5 = Det\begin{bmatrix}
1 & i & 0 & 0 & 0 \\
i & 1 & i & 0 & 0 \\
0 & i & 1 & i & 0 \\
0 & 0 & i & 1 & i \\
0 & 0 & 0 & i & 1 \\
\end{bmatrix}
$$

```julia
using LinearAlgebra

function f(n::Int)
    m = zeros(Complex, n, n)
    for i in 1:n
        for j in 1:n
            if i == j
                m[i, j] = 1
                if i-1 >0
                    m[i-1, j] = im
                end
                if i+1 < n
                    m[i+1, j] = im
                end
                if j-1 > 0
                    m[i, j-1] = im
                end
                if j+1 < n
                    m[i, j+1] = im
                end
            end
        end
    end
    return convert(Int64, det(m))
end

println(f(2))
println(f(3))
println(f(4))
println(f(5))
println(f(6))
println(f(7))
```


```bash
2
3
5
8
13
21
```