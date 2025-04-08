def tower_of_hanoi(n,a,b,c):
    if n==1:
        print("Move disk 1 from rod  ",a,"to rod ",c)
        return
    tower_of_hanoi(n-1,a,c,b)
    print("Move disk ",n,"from rod ",a,"to rod ",c)
    tower_of_hanoi(n-1,b,a,c)

tower_of_hanoi(3,"A","B","C")