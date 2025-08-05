#This is the insertion sort algorithm
def insertion_sort(array):
    n = len(array)
    for i in range(1,n):
        key = array[i]
        j = i-1
        while j>=0 and key < array[j]:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key
    return array    

array=[1,4,6,3,8]
result= insertion_sort(array)
print("sorted array: ",result)            
        