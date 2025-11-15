from IPython.display import Image
import sys
print(sys.version)
# load numpy
import numpy as np

# load csv into an array named co2data
# This will create a variable named co2data. Notice that we don't need to declare it first.
# Notice that we use the delimiter keyword to specify that values are separated by commas.
co2data=np.genfromtxt('co2py.csv',delimiter=',')

# the first column of the data is country names, not numbers, so they all show up as NaN (not a number)
# let's delete column 0 (the first column)
# the first row is the year for the emissions data (1990-2014), so let's strip that out as well
# the first index is the row number, and the second index is the column number
# "1:"" means to select rows/columns 1 (that's the second row/column) to the end
co2data=co2data[1:,1:]

countries=np.genfromtxt('co2py.csv',delimiter=',',usecols=0,dtype=str)

countries=countries[1:]

print(co2data)

print(co2data[40])

print(co2data[40,4])

np.shape(co2data)


# # Hands-On Exercise 1
# 1. Load the data set and store it in arrays
# 2. Print line number 100 (i.e., the 101st country).
# 3. Which country's data are you viewing?
# 4. Is it complete? If not, what's missing? Which years?
# load numpy
import numpy as np

# load the data
co2data=np.genfromtxt('co2py.csv',delimiter=',')

# finish cleaning it
co2data=co2data[1:,1:]

# as before, store the country names in a separate array
countries=np.genfromtxt('co2py.csv',delimiter=',',usecols=0,dtype=str)
countries=countries[1:]

# print line 100
print(co2data[100])
# which country is in line 100? use the countries array
print(countries[100])

#First, create an empty dictionary that we can fill
co2_dict=dict()

for i in range(len(countries)): 
    co2_dict[countries[i]]=co2data[i]

# Let's find the data for Afghanistan. Now, I don't need to know the line number, and I can do everything in one line:
print(co2_dict['Afghanistan'])
print(type(co2data))
print(type(co2_dict))


# # Hands-On Exercise 2
# 1. Use a for loop to print out the name of each country in the list, followed by its emissions data from 1990 (the first year in the data set).
# Here's one solution, using just the original arrays
# 1990 is the first entry in each row, so it's element 0 in the second dimension

for i in range(len(countries)): # go through all countries, using range to go from 0 to len(countries)
    print(countries[i]) # print country name
    print(co2data[i,0]) # print the 1990 data

# create the dictionary
co2_dict=dict()

# populate the dictionary
for i in range(len(countries)): # go through all countries, using range to go from 0 to len(countries)
    co2_dict[countries[i]]=co2data[i]

for i in co2_dict: # go through all dict entries
    print(i) # print country name
    print(co2_dict[i][0]) # we can't use a comma here, since the two dimensions are referring to different things
    # this first [i] is the element of the dictionary, which is an array
    # the second [0] means element 0 of that array
    # print the 1990 data, still element 0 of the array for each country

# load pyplot from Matplotlib. It's usually abbreviated as plt. 
import matplotlib.pyplot as plt

# Here's the simplest possible plot - US carbon emissions, 1990-2014
# we're only giving the y-axis here, with the x-axis implied
# plt.plot(co2_dict['United States'])

# It would be nice if the x-axis were accurate with the year number
# now, we're going to use range with start, stop, and step size arguments
# plt.plot(range(1990,2015,1),co2_dict['United States'])

# Let's label the axes as well
# plt.xlabel('Year')
# plt.ylabel('CO2 emissions (kg per PPP $ of GDP)')

# Let's plot three countries on the same axes
# I can specify the color & shape of the markers after the data
# plt.plot(range(1990,2015,1),co2_dict['United States']) # the default is to plot a line
# plt.plot(range(1990,2015,1),co2_dict['Afghanistan'],'o') # o means to plot circles
# plt.plot(range(1990,2015,1),co2_dict['China'],'r') # 'r' means to plot in red

# Let's label the axes as well
# plt.xlabel('Year')
# plt.ylabel('CO2 emissions (kg per PPP $ of GDP)')

# and include a legend, with the labels in the order in which we generated the plots
# plt.legend(['US','Afghanistan','China'])

# Again, let's plot three countries on the same axes
# I can specify the color & shape of the markers after the data
plt.plot(range(1990,2015,1),co2_dict['United States']) # the default is to plot a line
plt.plot(range(1990,2015,1),co2_dict['Afghanistan'],'o') # o means to plot circles
plt.plot(range(1990,2015,1),co2_dict['China'],'r') # 'r' means to plot in red

# Let's label the axes as well
plt.xlabel('Year')
plt.ylabel('CO2 emissions (kg per PPP $ of GDP)')

# and include a legend, with the labels in the order in which we generated the plots
plt.legend(['US','Afghanistan','China'])
plt.savefig("3countries.pdf",format='pdf') # to save to file - filename and format

# # Hands-On Exercise 3
# 1. Plot the data for Ukraine for all years as red stars.
# 2. Plot the data for Japan for all years as a green line on the same plot. 
# 3. Label your axes and add a legend. 

# load pyplot from Matplotlib. It's usually abbreviated as plt. 
import matplotlib.pyplot as plt

# make a range for the x-axis, from 1990 through 2014
plt.plot(range(1990,2015,1),co2_dict['Ukraine'],'r*') # r for red, * for stars
plt.plot(range(1990,2015,1),co2_dict['Japan'],'g') # g for green; lines are the default shape

# Let's label the axes as well
plt.xlabel('Year') # label x-axis
plt.ylabel('CO2 emissions (kg per PPP $ of GDP)') # label y-axis

# and include a legend, with the labels in the order in which we generated the plots
plt.legend(['Ukraine','Japan'])

co2_dict['United States']/co2_dict['China']
# performs an elementwise division between 2 arrays of the same size and returns an array

# First, find the mean for 2014 using numpy's mean function
np.mean(co2data[:,-1])

np.mean(co2_dict['United States'])

np.nanmean(co2data[:,-1])

mean2014=np.nanmean(co2data[:,-1])
below_average=np.array([],dtype=str)
above_average=np.array([],dtype=str)
unknown=np.array([],dtype=str)

# go through all of the countries -- the number of them is the length of the countries array
for i in co2_dict:
    individual2014=co2_dict[i][-1] # find the 2014 data for that country
    if individual2014<=mean2014:
        below_average=np.append(below_average,i) # add to below_average array
    elif individual2014>mean2014:
        above_average=np.append(above_average,i) # add to above_average array
    else: # unknown 'nan' entries
        unknown=np.append(unknown,i)
    
print("Below average:",below_average)
print("Above average:",above_average)
print("No 2014 data:",unknown)

# ## File Output in NumPy
# a function of an array is "tofile"
# we specify the destination file name and the separator between elements of the array
# '\n' is a newline character, to put each element on its own line
below_average.tofile("below_average.out",sep='\n')

# Let's look at that file with the Linux cat command. We can access the command line in Jupyter with %. 
##get_ipython().run_line_magic('cat', 'below_average.out')

# # Hands-On Exercise 4
# 1. Figure out which countries had lower emissions per GDP in 2014 than they did in 2013. 
# 2. Print out these countries to the screen.
# 3. Save your results to a file named "reducers.dat". 

# create an array to store the countries that reduced
reducers=np.array([],dtype=str)

#go through all countries
for i in co2_dict:
    # see if 2014 (last column, -1) is less than 2013 (second-to-last column, -2)
    if co2_dict[i][-1]<co2_dict[i][-2]:
        # if so, store in the array
        reducers=np.append(reducers,i)

print(reducers)

reducers.tofile("reducers.dat",sep='\n') # store in a file named reducers.dat
# with each element separated by a newline character (\n)