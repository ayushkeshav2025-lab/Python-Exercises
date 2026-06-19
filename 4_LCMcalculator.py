def lcm (x,y):
    if x>y:
        z=x
    else:
        z=y
        while True:
            if (z%x==0) and (z%y==0):
                lcm = z
                break
            z+=1
        return lcm
#taking inputs from users for lcm
num1 = int(input ("enter the first numeber"))
num2 = int(input("enter the secondd number"))
print("The Lcm of ", num1 ,"And", num2 ,"is", lcm(num1,num2))