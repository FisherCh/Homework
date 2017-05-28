# coding = utf-8

import hashlib
import base64
def week1_romantic():
    optionalList = ['我们在一起吧','我选择原谅你','别说话，吻我','多喝热水']
    wordEncoded = b'NDRiMWZmMmVjZTk5MTFjMWI1MDNkYTY0MzZlYTAzMTA=\n'
    wordDecodedBase64 = base64.decodestring(wordEncoded)
    print('Excepted md5 code:')
    print(wordDecodedBase64)
    print()
    for option in optionalList:
        wordEncodedMD5 = hashlib.new("md5",option.encode() ).hexdigest()
        # print(wordEncodedMD5)
        if wordEncodedMD5.encode()==wordDecodedBase64:
            print('The answer is: ',option)

from numpy import *
def week2_magic(n):
    if mod(n,2):
        # 奇数阶
        A = week2_oddMagic(n)
    elif mod( int(n/2) ,2 ):
        # 仅能被2整除，可拆分成四个奇数阶幻方
        a = int(n/2)
        A = zeros([n,n])
        A[:a,:a] = week2_oddMagic(a)
        A[a:,a:] = week2_oddMagic(a) + a**2
        A[:a,a:] = week2_oddMagic(a) + 2*a**2
        A[a:,:a] = week2_oddMagic(a) + 3*a**2
    else:
        # 仅能被4整除
        A = mat([i for i in range(1,n**2+1)]).reshape([n,n])
        J = mod( array([i for i in range(1,n+1)]) ,4 )>1.2
        for x in range(0,n):
            for y in range(0,n):
                if (J[x] == J[y]):
                    A[x,y] = n**2+1 - A[x,y]
    print(A)

def week2_oddMagic(n):
    # 罗伯特法求奇数阶幻方/楼梯法
    A = zeros([n,n])
    posX = 0
    posY = int(n/2)
    for val in range(1,n**2+1):
        if int(A[posX,posY]):
            posX = mod(posX+2,n)
            posY = mod(posY-1,n)
        # 赋值并更新位置
        A[posX,posY] = int(val)
        posX = mod(posX-1,n)
        posY = mod(posY+1,n)
    return A

def week3_Yanghui(i,j):
    # 返回i行j列的杨辉三角--递归
    if j>i+1:
        print('invalid query')
        return -1
    if i<2 or j==0 or j==i:
        return 1
    else:
        return week3_Yanghui(i-1,j-1) + week3_Yanghui(i-1,j)

def week3_generateYH_help(lastLayer,i,j):
    # 杨辉三角：根据上一层计算下一层
    if j==0 or j==i:
        return 1
    else:
        return lastLayer[j-1] + lastLayer[j]

def week3_generateYH(m):
    # 返回m层的杨辉三角
    Layer = [1]
    for x in range(1,m):
        print(Layer)
        Layer = [week3_generateYH_help(Layer,x,i) for i in range(x+1)]
    print(Layer)

def week4_Goldbach( num ):
    # 验证哥德巴赫猜想
    num = int(num)
    if mod(num,2)==0:
        for m in range(2,num):
            n = num - m
            if week4_isPrime(m) and week4_isPrime(n):
                print(m,' + ',n,' == ',num)
                return
    elif num>5:
        for m in range(2,num-4):
            for n in range(2,num-2-m):
                k = num-m-n
                if week4_isPrime(m) and week4_isPrime(n) and week4_isPrime(k):
                    print(m,' + ',n,' + ',k,' == ',num)
                    return
    print('Failed')
    return

def week4_isPrime( num ):
    # 判断是否质数
    num = int( num )
    if num>=1 and num<=3:
        return True
    if mod(num,2)==0:
        return False
    for x in range(2, int( sqrt(num) )+1 ):
        if mod(num,x)==0:
            return False
    return True

if __name__ == '__main__':
    # week1_romantic()
    # week2_magic(8)
    print( week3_Yanghui(3,2) )
    print( week3_generateYH(6) )
