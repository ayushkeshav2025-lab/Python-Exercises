num = int(input("enter the number"))
flag = False
if num>1:
    for i in range(2,num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print(num, "Given Number Is Not A Prime Number")
else:
    print(num, "Given Number Is  A Prime Number")