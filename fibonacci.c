#include <stdio.h>
int fib(int a){
    if(a==0)
    return 0;
    if(a==1||a==2)
    return 1;
    else
    return (fib(a-1)+fib(a-2));
}

int main(){
    int n;
    printf("Enter a postion of a number in the fibonacci sequence: ");
    scanf("%d",&n);

    printf("The number in position %d is %d",n,fib(n));
    return 0;
}