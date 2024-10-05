def bubblesort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-i-1):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swapped = True

        if not swapped:
            return arr    

    return arr

# print(bubblesort([1,2,3,5]))


def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key  

    return arr

# print(insertionsort([2,4,3,1]))  


def reverseinsertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key  

    return arr

# print(reverseinsertionsort([2,4,3,1]))  


def selectionsort(arr):
    for i in range(len(arr)):
        mini = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[mini]:
                mini = j

        arr[mini], arr[i] = arr[i], arr[mini]       

    return arr

# print(selectionsort([3,2,2,1]))    




def merge(arr, low, mid, high):
    left = low
    right = mid + 1
    temp = []
    
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:  # if arr[left] >= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    while left <= mid:
        temp.append(arr[left])
        left += 1
    
    while right <= high:
        temp.append(arr[right])
        right += 1
    
    for i in range(len(temp)):
        arr[low + i] = temp[i]

def mergesort(arr, low, high):
    if low == high: return 
    mid = (low + high) // 2
    mergesort(arr, low, mid)
    mergesort(arr, mid + 1, high)
    merge(arr, low, mid, high)


# arr = [1, 3, 2, 5]
# mergesort(arr, 0, len(arr) - 1)
# print(arr)  


def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot and  i <= high:
            i += 1
        while arr[j] > pivot and j >= low  :
            j -= 1   

        if i<j:
            arr[j], arr[i] = arr[i], arr[j]

    arr[low], arr[j] = arr[j], arr[low]        

    return j

def quickSort(arr, low, high):
    if low == high: return
    pindex = partition(arr, low, high)
    quickSort(arr, low, pindex-1)
    quickSort(arr, pindex+1, high)

# arr = [3,4,1,2]
# quicksort(arr, 0 , len(arr)-1)
# print(arr)