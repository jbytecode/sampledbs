abstract type PDF end

const sqrt2pi = sqrt(2.0 * pi)

struct Normal <: PDF
    mu::Float64
    sigma::Float64
    lower::Float64
    upper::Float64
    f::Function
end 

function Normal(mu, sigma) 
    return Normal(
        mu, 
        sigma,
        mu - 5 * sigma,
        mu + 5 * sigma,
        x -> (1.0/(sigma * sqrt2pi)) * exp(-0.5 * ((x - mu)/sigma)^2)
    )
end 


function integrate(pdf::PDF, a::Float64, b::Float64, eps=1e-6)::Float64
    pdf.f.(a:eps:b) .* eps |> sum
end


function invcdf(pdf::PDF, p::Float64, eps=1e-5)::Float64
    start = pdf.lower
    finish = pdf.upper
    mid = (start + finish) / 2
    L = pdf.lower
    intg = integrate(pdf, L, mid, eps)
    while abs(intg - p) > eps
        if intg < p
            start = mid
        else
            finish = mid
        end
        mid = (start + finish) / 2
        intg = integrate(pdf, L, mid, eps)
    end
    return mid
end


println(invcdf(Normal(0.0, 1.0), 0.975, 0.00001))



