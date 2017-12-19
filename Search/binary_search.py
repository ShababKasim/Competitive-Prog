'''
Time complexity: O(logn)
Space complexity: O(n)
Worst case time complexity: O(n)
'''

def search(arr,ele):
    
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = int((l + (r-l)/2))
        if arr[m] == ele:
            return m
        elif arr[m] < ele:
            l = m + 1
        else:
            r = m - 1
    return -1



if __name__ == '__main__':
    arr = [5,2,4,6,8,5,7,9,6,4,2]
    arr.sort()
    arr = list(set(arr))
    ele = int(input('Enter element to be searched..>'))
    index = search(arr,ele)
    if index != -1:
        print('Gotcha! element: {} at index: {}'.format(ele,index))
    else:
        print('Nopes bro! not here.')
