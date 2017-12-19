'''
as binary search takes O(logn) time to search and we know that 
the array is sorted we calculate the lowest and highest index and 
sumup for occurances in O(logn) time
'''

def search(arr,e,searchfirst=True):
    l = 0 
    r = len(arr)-1
    res = -1
    while l <= r:
        m = round((l + (r-l)/2))
        if arr[m] == e:
            res = m
            if searchfirst:
                r = m - 1
            else:
                l = m + 1
        elif arr[m] < e:
            l = m + 1
        else:
            r = m - 1
    return res 

if __name__ == '__main__':
    a = [1,1,1,1,1,1,5,5,5,5,5,5,5,5,5,5,5,5,6,7,9]
    e = 1

    l,r = search(a,e), search(a,e,False)
    print(l,r)
    if l == -1 or r == -1:
        print('Nopes, not found in array')
    else:
        res = r - l +1
        print("the number {} occurs {} times".format(5,res))