@info "Loading Flux"
using Flux


X = Float32[
    0.0 0 1 1; 
    0.0 1 0 1
    ]
y = Float32[0.0 1 1 0]

model = Chain(
    Dense(2, 3, Flux.sigmoid),
    Dense(3, 1, Flux.sigmoid)
)

loss_fn(x, y) = Flux.mse(model(x), y)

opt = Flux.ADAM(0.1)

N = 5000
for i in 1:N
    Flux.train!(loss_fn, Flux.params(model), [(X, y)], opt)
end 

println(model(X))
