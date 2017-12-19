
'''
Time Complexity: theta(nlogn)
space Complexity: theta(nlogn)
not an in-place algo. so requires extra space

'''



def mergeSort(array):
    l = len(array)
    if l < 2:
        return 
    m = round(l/2)
    L = array[:m]
    R = array[m:]
    mergeSort(L)
    mergeSort(R)
    merge(L,R,array)



def merge(L,R,A):
    lL,lR = len(L),len(R)
    i = j = k = 0
    
    while i < lL and j < lR:

        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]  
            j += 1
        k += 1
    
    while i < lL:
        A[k] = L[i]
        i += 1
        k += 1

    while j< lR:
        A[k] = R[j]
        j += 1
        k += 1



if __name__ == '__main__':
    import random
    a = list(range(50000))
    random.shuffle(a)
    mergeSort(a)
    print(a)