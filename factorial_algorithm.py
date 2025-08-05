#This is the factorial algorithm in python
def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)

number=int(input("Enter a positive number: "))
if number<0:
    number=int(input("Enter a positive number: "))
    print("The factorial of ",number,"is ",factorial(number))
else:
    print("The factorial of ",number,"is ",factorial(number))