#This is the linear search algorithm
def linear_search(array,target):
    for i in range (len(array)):
        if array[i]==target:
            return i
    return -1
    
array=[3,4,7,8,9]
target=8
result=linear_search(array,target)
if result!=-1:
    print(f"the index is {result}")
else:
    print("the element doesnt exist")    
    