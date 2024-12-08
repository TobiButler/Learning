"""

"""
import random
from copy import deepcopy

########## Iterative Implementation ############
def mergesort(unsorted:list) -> list: 
    # copy list provided to avoid overwriting
    unsorted = deepcopy(unsorted)

    # get length of list for max indexing
    list_len = len(unsorted)

    # merge sub-lists in sets of 2, 4, 8, 16,...
    i = 1
    while i < len(unsorted):
        for n in range(0, len(unsorted), i*2):
            r_start = min(n+i, list_len)
            r_end = min(n+(i*2), list_len)

            # merge the two sorted lists into one sorted list
            sorted = merge(unsorted, n, r_start, r_end)

            # insert sorted list back into original list
            unsorted[n:n+(i*2)] = sorted
        i = i*2
    return unsorted # now sorted


# merge two already sorted lists together
def merge(unsorted:list, l_start, r_start, r_end):
    # create a new list to hold the results
    sorted = []

    # loop through the two lists until one of them is empty
    l = l_start
    r = r_start
    # print(l_start, r_start, r_end)
    while (l < r_start) and (r < r_end):
        # compare values in the two lists and add the smallest to the new list
        if unsorted[l] <= unsorted[r]: 
            sorted.append(unsorted[l])
            l = l + 1 # update index
        else: 
            sorted.append(unsorted[r])
            r = r + 1 # update index

    if l < r_start: sorted.extend(unsorted[l:r_start])
    elif r < r_end: sorted.extend(unsorted[r:r_end])

    return sorted




######### Recursive Implementation ###########
def mergesort_r(unsorted:list) -> list: pass



def helper_r(): pass



###### function for testing the mergesort algorithms ########
def main():
    k = random.choice(range(1,20)) # determine length of list to sort

    ######## iterative method ##########
    # create random list of integers
    random_list = random.choices(range(0,100),k=k)
    print("Unsorted list: " + str(random_list))

    # sort the list
    sorted_list = mergesort(random_list)
    print("Sorted list: " + str(sorted_list))

    # ######## recursive method ##########
    # # create random list of integers
    # random_list = random.choices(range(0,100),k=k)
    # print("Unsorted list: " + str(random_list))

    # # sort the list
    # sorted_list = mergesort_r(random_list)
    # print("Sorted list: " + str(sorted_list))



if __name__ == "__main__":
    main()