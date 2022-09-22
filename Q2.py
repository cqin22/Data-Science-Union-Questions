from pandas import *
 
total = 0

# reading CSV file
data = read_csv("world_population.csv")
 
# converting column data to list
set = data['1980 Population'].tolist()

# sums all elements in list
for ele in range(0, len(set)):
    total = total + set[ele]

# returns 4442400371
print(total)

