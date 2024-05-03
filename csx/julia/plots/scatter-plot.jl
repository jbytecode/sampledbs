using Plots 

x = rand(30)
y = rand(30)

plot(
    x, 
    y, 
    seriestype = :scatter, 
    title = "Scatter Plot", 
    label = "Scatter Plot", 
    xlabel = "X-axis", 
    ylabel = "Y-axis", 
    legend = :topleft, 
    grid = :on, 
    size = (800, 600), 
    color = :red)