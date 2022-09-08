def isPowerOfTwo(n):
    if (n == 0):
        return False
    while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
             
    return True

def change_values(int1, int2, int3, int4):
    
    if (int2 % 2 != 0):
        temp = int1
        int1 = int2 
        int2 = temp
    if isPowerOfTwo(int3) == True:
        temp = int4
        int4 = int3
        int3 = temp
    if (int1 + int2 + int3) == int4:
        int4 = int1

    return int1, int2, int3, int4

def main():

    input1 = int(input())
    input2 = int(input())
    input3 = int(input())
    input4 = int(input())

    num1, num2, num3, num4 = change_values(input1,input2, input3, input4)

    print(str(num1) + ' ' + str(num2) + ' ' + str(num3) + ' ' + str(num4))

main()
    
        


