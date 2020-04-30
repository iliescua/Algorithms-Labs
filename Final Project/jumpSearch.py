import math

def jump(lst, val, size):
    #Determines the step size for how many elements to jump over 
    step = math.sqrt(size)
    #Keeps track of the block we are on
    track = 0

    #Searching to see which block of size sqrt(size) would contain the value
    while lst[int(step)] < val:
        track = int(step)
        step += step
        #Reaching the end of list without finding the value
        if track >= size:
            return -1

    #If step is > size we are checking the previous blocl for the value
    while lst[int(track)] < val:
        track+=1
        #If we checked whole block unsuccessfully
        if track > val:
            return -1
    
    #If value is found in the list return it
    if lst[int(track)] == val:
        return track
    else:
        return -1