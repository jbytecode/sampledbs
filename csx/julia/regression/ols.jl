using GLM, Plots

n = 30

x = randn(n)
y = 2 * x .+ 3 .+ randn(n)
X = hcat(ones(n), x)  # Add a column of ones for the intercept

result = lm(X, y)

println(result)

println("Coefficients: ", coef(result))
println("Intercept: ", coef(result)[1])
println("Slope: ", coef(result)[2])
println("R-squared: ", r2(result))
println("Adjusted R-squared: ", adjr2(result))
println("F-statistic: ", deviance(result))

@info "F-Test"
ftestresult = ftest(result)
println("p-value: ", ftestresult.pval)

@info "Residuals"
println(residuals(result))

@info "Fitted values"
println(fitted(result))