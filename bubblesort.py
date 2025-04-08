def bubble_sort(array):
    n=len(array)
    for i in range(n):
        for j in range(0,n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array

array=[1,7,6,5,4,2]
result= bubble_sort(array)
print("sorted array: ",result)             