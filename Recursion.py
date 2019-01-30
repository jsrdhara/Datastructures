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

#fibonacci Series

# Created by Jan Markus, edited by Martin

class Fibonacci:
    def fibo(self, x):
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            return self.fibo(x-1) + self.fibo(x-2)

f = Fibonacci()

for i in range(16):
    print(f.fibo(i))