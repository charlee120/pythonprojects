my_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def dev(n):
    if n%2==0:
        return True
    else:
        return False
    

list1=filter(dev,my_list)

print(list(list1))
