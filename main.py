num1=int(input("Enter a number:"))
s=0.0
for i in range(1,num1+1):
    a=float(i**i)/i
    s=s+a
print("The sum of series is :",s)