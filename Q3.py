from pandas import *

longest = 0
length = 0
longestCap = ""

# reading CSV file
data = read_csv("world_population.csv")
 
# converting column data to list
capital = data['Capital'].tolist()

# finds the longest element length in the Captial column
for ele in capital:
    length = len(ele)
    if length > longest:
        longest = length
        longestCap = ele

# returns Bandar Seri Begawan
print(longestCap)
