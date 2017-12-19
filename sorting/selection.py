'''
time complexity is O(n^2)
'''

def sort(arr):
    i = 0
    n = len(arr)
    for i in range(n-1):
        j = i+1
        while j < n:
            if arr[j] < arr[i]:
                arr[i],arr[j] = arr[j],arr[i]
            j += 1

if __name__ == '__main__':
    a = [6,5,7,9,8,4,3,1,2]
    sort(a)
    print(a)