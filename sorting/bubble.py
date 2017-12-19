'''
Best: O(n)
Average: O(n^2)
worst: O(n^2)
'''


def sort(arr):
    n = len(arr)
    for k in range(n):
        swap = False
        for j in range(n-1):
            if arr[k] < arr[j]:
                arr[j],arr[k] = arr[k],arr[j]
                swap = True
        if not swap:
            break

if __name__ == '__main__':
   a = [6,8,9,7,5,4,3,1,2]
   sort(a)
   print(a)