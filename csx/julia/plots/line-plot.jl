using Plots 

t = 1:30

x = rand(30)

plot(
    t, 
    x, 
    seriestype = :line, 
    title = "Line Plot", 
    label = "Line Plot", 
    xlabel = "X-axis", 
    ylabel = "Y-axis", 
    legend = :topleft, 
    grid = :on, 
    size = (800, 600), 
    color = :red)