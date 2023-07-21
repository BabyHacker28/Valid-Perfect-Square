def sqrtNum(num):
    k = num//2
    for i in range(1,k+1):
        if i*i == num:
            return True
        elif(i*i > num):
            return False

num = int(input())
print(sqrtNum(num))
