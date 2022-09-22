from pandas import *
 
# reading CSV file
data = read_csv("world_population.csv")
 
# converting column data to list
set = data['1980 Population'].tolist()
 
# printed list data to test accuracy
# print('1980 Population:', set)

# finding the highest population of the list
print(max(set))

# returns 982372466, which is China