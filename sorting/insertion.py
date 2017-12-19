

def sort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(i,-1,-1):
            if arr[i] > arr[j]:
                break
            else:
                arr[i],arr[j] = arr[j],arr[i]
            



if __name__ == '__main__':
    a = [6,5,7,9,8,4,3,1,2]
    sort(a)
    print(a)