my_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

rakesh=iter(my_list)

n=int(input("Enter a number:"))

if n == len(my_list):
    for i in range(n):
        print(next(rakesh))

else:
    print("invalid input")
