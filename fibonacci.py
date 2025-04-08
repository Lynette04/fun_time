def fib(n):
    if n==0 or n==1:
        return n
    else: 
        return fib(n-1)+ fib(n-2) #since we are getting the next fibonacci number, we add the previous two numbers.
    
print(fib(5))

'''fib(5)=fib(4)+fib(3)
   fib(4)=fib(3)+fib(2)
   fib(3)=fib(2)+fib(1)
   fib(2)=fib(1)+fib(0)'''
    
