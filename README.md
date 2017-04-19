### Introduction to NumPy arrays

Python lists are very flexible, but they are slow for big calculations.

NumPy arrays can store purely numerical data in much less space, and are much simpler and faster for calculations.

We can calculate the mean with a NumPy array instead of a list:

	import numpy as np

	fluxes = np.array([23.3, 42.1, 2.0, -3.2, 55.6])

	m = np.mean(fluxes)

	print(m)


NumPy has a great range of numerical functions. For example, to calculate the size of an array, and the standard deviation:

	import numpy as np

	fluxes = np.array([23.3, 42.1, 2.0, -3.2, 55.6])

	print(np.size(fluxes)) # length of array

	print(np.std(fluxes))  # standard deviation


### Reading strings from CSV files

Tables are often stored in comma-separated values (CSV) format. You can use Python's built-in string functions to read a CSV file into a list and process it.

The following examples read this data.csv file:
data.csv

8.84,17.22,13.22,3.84

3.99,11.73,19.66,1.27

16.14,18.72,7.43,11.09

Our file has several rows and columns. We want to store each row in a list and the whole file as a list of these rows.

The program loops over each line in the file, splitting the row into a list of values, and appending each row to data:

	data = []

	for line in open('data.csv'):

  	data.append(line.strip().split(','))

​	print(data)

The strip method removes whitespace (including the newline) from the ends of line. The split method creates a list of strings using the ',' character as the separator between items. 

### Reading numbers from CSV files

Now we can store the data in lists, we need to convert each item from a string to a float. We could do this using nested for loops:

	data = []

	for line in open('data.csv'):

  		row = []

 		 for col in line.strip().split(','):

   			 row.append(float(col))

  		 data.append(row)

​	print(data)

NumPy has a simpler asarray function to do this conversion:

	import numpy as np

​	data = []

	for line in open('data.csv'):

  		data.append(line.strip().split(','))

​
	data = np.asarray(data, float)

	print(data)

Most NumPy functions operate on the whole array at once rather than individual items. 