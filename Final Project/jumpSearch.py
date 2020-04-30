import math

def jump(lst, val):
    size = len(lst)
    #Determines the step size for how many elements to jump over 
    step = math.sqrt(size)
    #Keeps track of the block we are on
    track = 0

    #Searching to see which block of size sqrt(size) would contain the value
    while (lst[int(step)] < val and int(step) < size):
        track = step
        step += step
        #Reaching the end of list without finding the value
        if track >= size:
            return -1

    #If step is > size we are checking the previous block for the value
    while lst[int(track)] < val:
        track+=1
        #If we find the value in the block
        if lst[int(track)] == val:
            return track
    
    #Returns -1 if value is not found in the list
    return -1
