using Plots


x = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7]

histogram(
    x,
    title="Histogram",
    label="Histogram",
    xlabel="X-axis",
    ylabel="Y-axis",
    legend=:topright,
    grid=:on,
    size=(800, 600),
    color=:red)