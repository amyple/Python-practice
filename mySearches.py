# Copyright © [November 2nd, 2017]['blsearch.py' in Unit 4's resource by Prof. Lars].
#  A program to do a binary search on a list of numbers
#
def bsearch(x, nums):
    item =0
    low = 0
    high = len(nums) -1
    c = 0

    while low <= high:                   # Still a range to search
        print("Step counter : ",c,item)
        mid = (low+high)//2              # this is the position of the middle number
        item = nums[mid]
        print("The Mid:",item)

        if x == item:        # got it, now return it!
            c = c + 1
            print("Binary Search took",c,"lookeups") ### Print out total lookups
            print("With bsearch, number found:", x)
            return mid
            
        elif x < item:       # x is in the lower half of the range
            high = mid -1    #    move the top marker down
            c = c + 1        #    up the step counter

        else:                # x is in the upper half
            low = mid + 1    #    move the bottom marker up
            c = c + 1        #    up the step counter
            
    print("With bsearch,number not found")
    print("Binary Search took",c,"lookups")
    return -1                # x is not found


####
# Function for a linear search

def lsearch(x, nums):
    c = 0
    for i in range(0,len(nums)):
        if x == nums[i]:
            c = c + 1
            print("Linear Search took",c,"lookups")
            print("With lsearch, number found:",x)
            return i       
        else:
            c = c + 1
            
    print("With lsearch,number not found")
    print("Linear Search took",c,"lookups")
    return -1

#####


