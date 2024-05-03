using Plots

t = 1:17

x = [1, 1, 2, 3, 4, 4, 4, 5, 5, 6, 7, 7, 7, 7, 8, 9, 10]
y = [10, 9, 9, 8, 8, 8, 7, 6, 5, 5, 5, 4, 4, 3, 2, 1, 1]
z = rand(1:10, 17)

plot(
    t,
    x,
    seriestype=:line,
    title="Line Plot",
    label="x",
    legend=:top,
    grid=:on,
    size=(800, 600),
    color=:red)

plot!(
    t,
    y,
    seriestype=:line,
    title="Line Plot",
    label="y",
    legend=:top,
    grid=:on,
    size=(800, 600),
    color=:blue)

plot!(
    t,
    z,
    seriestype=:line,
    title="Line Plot",
    label="z",
    xlabel="time",
    ylabel="x, y, and z",
    legend=:top,
    grid=:on,
    size=(800, 600),
    color=:green)