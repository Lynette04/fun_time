#This is the binary serach algorithm
def binary_search(array,target):
    left=0
    right=len(array)-1

    while left<=right:
        mid=(left+right)//2
        if array[mid]==target:
            return mid
        elif array[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
array=[2,3,4,5,6]
target=4
result= binary_search(array,target)
if result!=-1:
    print(f"Element is at index {result}")  
else:
    print(f"Element does not exist")          