//This is a program to find the factorial of a number in C

#include <stdio.h>
int factorial(int a){
    if(a==0||a==1){
        return 1;
    }
    return a * factorial(a-1);
}
int main(){
    int n;
    printf("Enter a positive number of your choice: ");
    scanf("%d",&n);

    if (n<0){
        printf("Enter a positive number: ");
    }
    else{
        printf("%d is the factorial of %d",factorial(n),n);
    }
    return 0;
}