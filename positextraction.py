N=9
n1="110000000"
n3="000000011"
es=3
z=n1[0]
#<-------0----------->
def OR(a, b):
    if a == '1' or b =='1':
        return '1'
    else:
        return '0'
for i in range(1,N):
    z= OR(z,n1[i])
if z=='0':
    print("zero representation")
#<----------infinity--------->
z1='1'
if n1[0]=='1' :
    z1=n1[1]
    for i in range(2,N):
        z1= OR(z1,n1[i])

    if z1=='0':
        print("infinity representation")

def flip(c):
    return '1' if (c == '0') else '0'

#-----twos complement


def TwosComplement(bin):

    n = len(bin)
    ones = ""
    twos = ""

    for i in range(n):
        ones += flip(bin[i])


    ones = list(ones.strip(""))
    twos = list(ones)
    for i in range(n - 1, -1, -1):

        if (ones[i] == '1'):
            twos[i] = '0'
        else:
            twos[i] = '1'
            break





    return twos
if z1!='0' and z!='0':
    if n1[0]=='1':
        n2=TwosComplement(n1[1:N])
    else:
        n2=n1[1:N]


    #------regime----


    k=n2[0]
    for i in range(1,N-1):
        if n2[i]!=k :


            break
    print("regime bits are--",end="")
    r=i

    for i in range(0,r+1):
        print(n2[i],end="")
    print("\n")
    #---exponent----
    print("exponent are--",end="")
    e=0
    for i in range(r+1,N-1):

        print(n2[i],end="")
        e=e+1
        if e==es :
            break
    print("\n")
    #---fraction---
    r=i
    print("fraction are--",end ="")
    for k in range(r+1,N-1):
        print(n2[k],end="")

print("\n")
#-2nd
z=n3[0]
#<-------0----------->
def OR(a, b):
    if a == '1' or b =='1':
        return '1'
    else:
        return '0'
for i in range(1,N):
    z= OR(z,n3[i])
if z=='0':
    print("zero representation")
#<----------infinity--------->
z1='1'
if n3[0]=='1' :
    z1=n3[1]
    for i in range(2,N):
        z1= OR(z1,n3[i])

    if z1=='0':
        print("infinity representation")

def flip(c):
    return '1' if (c == '0') else '0'

#-----twos complement


def TwosComplement(bin):

    n = len(bin)
    ones = ""
    twos = ""

    for i in range(n):
        ones += flip(bin[i])


    ones = list(ones.strip(""))
    twos = list(ones)
    for i in range(n - 1, -1, -1):

        if (ones[i] == '1'):
            twos[i] = '0'
        else:
            twos[i] = '1'
            break

    i -= 1

    if (i == -1):
        twos.insert(0, '1')

    return twos
if z1!='0' and z!='0':
    if n3[0]=='1':
        n2=TwosComplement(n3[1:N])
    else:
        n2=n3[1:N]


    #------regime----


    k=n2[0]
    for i in range(1,N-1):
        if n2[i]!=k :


            break
    print("regime bits are--",end="")
    r=i

    for i in range(0,r+1):
        print(n2[i],end="")
    print("\n")
    #---exponent----
    print("exponent are--",end="")
    e=0
    for i in range(r+1,N-1):

        print(n2[i],end="")
        e=e+1
        if e==es :
            break
    print("\n")
    #---fraction---
    r=i
    print("fraction are--",end ="")
    for k in range(r+1,N-1):
        print(n2[k],end="")

