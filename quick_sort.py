#This is the famous quick sort algorithm
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot= array[len(array)//2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right= [x for x in array if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

array=[3,5,4,6,8,7]
result= quick_sort(array)
print("sorted array: ",result)

    