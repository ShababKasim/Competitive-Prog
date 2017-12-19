

def search(arr,e):
    l,r = 0,len(arr)-1
    while l<=r:
        m = round((l+r)/2)
        if arr[m] == e:
            return m
        if arr[m] <= arr[r]:
            if e > arr[m] and e <= arr[r]:
                l = m + 1
            else:
                r = m - 1
        else:
            if arr[l] <= e and e > arr[m]:
                r = m - 1
            else:
                l = m + 1
    return -1


if __name__ == '__main__':
    a = [6,7,8,9,1,2,3,4,5]
    e = int(input('Enter element to search..>'))
    res = search(a,e)
    print('Element {} is at index {}'.format(e,res))