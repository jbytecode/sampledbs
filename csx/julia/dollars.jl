mutable struct Person
    money::Int
end

function hasmoney(person::Person)
    return person.money > 0
end

npeople = 100
ntries = 1000000

people = [Person(100) for i in 1:npeople]

for iteration in 1:ntries 
    i = rand(1:npeople)
    j = rand(1:npeople)
    if hasmoney(people[i])
            people[i].money -= 1
            people[j].money += 1
    end
end

sort!(people, by=x->x.money, rev=true)

println(people)


