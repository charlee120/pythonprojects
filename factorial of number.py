num1=int(input("Enter a number:"))
fact=1
if(num1!=0):
    for i in range (1,num1+1):
        fact=fact*i
print("The factroial of of",num1,"is",fact)
