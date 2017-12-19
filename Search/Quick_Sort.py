
def quicksort(array,start,end):
    if start < end:
        pindex = partition(array,start,end)
        quicksort(array,start,pindex-1)
        quicksort(array,pindex+1,end)

def partition(array,start,end):
    pivot = array[end]
    pindex = start
    for i in range(start,end):
        if array[i] <= pivot:
            array[i],array[pindex] = array[pindex],array[i]
            pindex += 1
    array[pindex],array[end] = array[end],array[pindex]
    return pindex
    

if __name__ == '__main__':
    a = [5,7,6,4,8,9,3,1,2]
    quicksort(a,0,len(a)-1)    
    print(a)