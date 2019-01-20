# finding factorial

#Iteration

def iterative_factorial(n):

    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact

print(iterative_factorial(5))

#Recursion

def recursive_factorial(n):

    if n<0:
        return -1
    if n<2:
        return 1
    return n*recursive_factorial(n-1)

print(recursive_factorial(5))

#addition
#Recursion
def add(mylist):

    if len(mylist)==1:
        return mylist[0]

    return mylist[0]+add(mylist[1:])

print(add([1,2,3]))

#Iterative method

def add(mylist):
    sum=0
    for i in mylist:
        sum=sum+i
    return sum

print(add([1,2,3]))

#fibonacci iterative

def iterative_fibonacci(num):

    a,b = 0,1
    out_list=[]
    for _ in range(1,num):
        a,b=b,a+b
        out_list.append(b)
    return out_list
print(iterative_fibonacci(5))

#fibonacci recursive

def recursive_fibonacci(num):

    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return recursive_fibonacci(num-1)+recursive_fibonacci(num-2)

for i in range(5):
    print(recursive_factorial(i))



