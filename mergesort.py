def merge_sort(array):
    if len(array)>1: #if there are many elements in the array, divide the array into two parts the left array and the right array
        left_arr=array[:len(array)//2]     #side before the middle
        right_arr=array[len(array)//2:]    #side after the middle
    #recursion to carry out the merge sort on each array
        merge_sort(left_arr)    
        merge_sort(right_arr)
    # we use i,j,k to mean the indices of the elements in the left and right arrays and the index of the merged array
        i=0
        j=0
        k=0
    
        while i< len(left_arr) and j < len(right_arr):  #as the indices i and j are smaller than the size of the different arrays
            if left_arr[i] < right_arr[j]:  #if the element at index i of the left array is smaller than the element at index j of the right array
                array[k]=left_arr[i] #store the element of index i at index k of the merged array
                i+=1  #move to the next index and compare

            else:
                array[k]=right_arr[j]  #store the element of index j of the right array at index k of the merged array
                j+=1  #move to the next index and compare
        k+=1 # move to the next index of merged array
    
        while i<len(left_arr): #to cater for missing elements in the left array without considering the right array
            array[k]=left_arr[i]
            i+=1
            k+=1
    
        while j<len(right_arr): #to cater for the missing elements in the right array without considering the left array
            array[k]=right_arr[j]
            j+=1
            k+=1

array=[3,6,5,8,4,2,1]
merge_sort(array)
print(array)                    