#factorial

n=int(input("Enter a Factorial of the Number: "))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i

print(n,"!","=",factorial,sep="")    