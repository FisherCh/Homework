# coding = utf-8


def week1_romantic():
    import hashlib
    import base64
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
        A = week2_oddMagic(n)
    elif mod( int(n/2) ,2 ):
        a = int(n/2)
        A = zeros([n,n])
        A[:a,:a] = week2_oddMagic(a)
        A[a:,a:] = week2_oddMagic(a) + a**2
        A[:a,a:] = week2_oddMagic(a) + 2*a**2
        A[a:,:a] = week2_oddMagic(a) + 3*a**2
    else:
        A = mat([i for i in range(1,n**2+1)]).reshape([n,n])
        J = mod( array([i for i in range(1,n+1)]) ,4 )>1.2
        for x in range(0,n):
            for y in range(0,n):
                if (J[x] == J[y]):
                    A[x,y] = n**2+1 - A[x,y]
    print(A)

def week2_oddMagic(n):
	# 罗伯特法求奇数阶幻方
    A = zeros([n,n])
    posX = 0
    posY = int(n/2)
        
    for val in range(1,n**2+1):
        # print(posX,', ',posY)
        if int(A[posX,posY]):
            posX = mod(posX+2,n)
            posY = mod(posY-1,n)
        A[posX,posY] = int(val)
        posX = mod(posX-1,n)
        posY = mod(posY+1,n)
    return A

if __name__ == '__main__':
	# week1_romantic()
    week2_magic(8)
