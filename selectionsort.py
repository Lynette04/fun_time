def selection_sort(array):
    n=len(array)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if array[j]<array[min_index]:
                min_index=j
        array[i],array[min_index]=array[min_index],array[i]

array=[4,5,7,6,8]
selection_sort(array)
print("sorted array: ",array)                