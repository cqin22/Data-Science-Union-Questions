from pandas import *

i = 0
newDensity = []

# reading CSV file
data = read_csv("world_population.csv")
 
# converting column data to lists
country = data['Country'].tolist()
population = data['2022 Population'].tolist()
area = data['Area'].tolist()

# divides population and area into a density list
density = [p / a for p, a in zip(population, area)]

# creates a new list with only densities of countries that start with "A"
for ele in country:
    if ele[0] == 'A':
         newDensity.append(density[i])
    i += 1

# calculates average of newDensity
avg = sum(newDensity)/len(newDensity)

# returns 137.112 (rounded)
print(round(avg,3))