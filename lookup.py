
#reads file
file = 'rands.txt'
f = open(file, 'r')
dat = f.read()
dat=dat.split()
##convert string to int and sort the list
dat = [int(i) for i in dat]
dat.sort()

##import both functions from mySearches.py

from mySearches import bsearch, lsearch

# Main program
for i in [78700, 3333, 1118]:
    print("Search for number: ",i)
    x = bsearch(i,dat)
    print(x)
    y = lsearch(i,dat)
    print(y, '\n')
