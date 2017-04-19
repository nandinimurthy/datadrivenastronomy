import numpy as np

# Function to calculate mean and median without using statistics module
# Input: CSV file
# Output: Mean and Median of data stored in CSV file
def calc_stats(file):
  data = []
for line in open(file, 'r'):
  data.append(line.strip().split(','))

data = np.asarray(data, float)
total = 0
values = []
row = []
count = 0
for i in data:
  total += sum(i)
count = count + len(i)
for j in i:
  values.append(j)

mean = round(total/count, 1)
values = sorted(values)
index = int(count/2)
if count % 2 is 0:
  median = round((values[index] + values[index - 1])/2, 1)
else: 
  median = round(values[index], 1)
return mean, median


# Main function to test the above function with sample input stored in data.csv
if __name__ == '__main__':
  # Run your `calc_stats` function with examples:
mean,median = calc_stats('data.csv')
print(mean, median)