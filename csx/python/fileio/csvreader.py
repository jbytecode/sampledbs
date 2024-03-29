myfile = open('data.csv', 'r')

all_lines = myfile.readlines()


for line in all_lines:
    name, age, country = line.strip().split(';')
    print(f'{name} is {age} years old and lives in {country}')

myfile.close()
