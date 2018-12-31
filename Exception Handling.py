import math

def kap():

    kap.a = int(input('please give a number: '))

    try:
        print(math.sqrt(kap.a))

    except:

        print('you have given an incorrect format of number')
        print('given an absolute number')
        print(math.sqrt(abs(kap.a)))

kap()

def excep():

    if kap.a <0:

        raise RuntimeError('you cant use a negative number')
    else:

        print(math.cos(kap.a))

excep()