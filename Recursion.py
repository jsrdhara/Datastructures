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