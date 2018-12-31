class Fraction():
    
    def __init__(self,num,den):
        
        self.num=num
        self.den=den
        
    def show(self):
        
        print(self.num,"/",self.den)
        
    def __str__(self):
        
        return(str(self.num)+"/"+str(self.den))
        
    def __add__(self,otherfrac):
        
        newnum = self.num*otherfrac.den+otherfrac.num*self.den
        newden = self.den*otherfrac.den
        g = gcd(newnum,newden)
        return(Fraction(newnum//g,newden//g))
        
    def __eq__(self,other):
        
        newnum = self.num*other.den
        newden = self.den*other.num
        
        return(newden==newnum)
        
def gcd(a,b):
    
    if a==0:
        return(b)
    if b==0:
        return(a)
    if a==b:
        return(a)
    if a>b:
        return(gcd(a-b,b))
    else:
        return(gcd(a,b-a))
        
f1 = Fraction(1,2)
f2 = Fraction(1,2)
f3 = f1+f2
print(f3)
print(f1==f2)

N = 4


# Function to check matrix
# is diagonal matrix
# or not.
def isDiagonalMatrix(mat):
    for i in range(0, N):
        for j in range(0, N):

            if ((i != j) and (mat[i][j] != 0)):
                return False

    return True


# Driver function
mat = [[4, 0, 0, 0],
       [0, 7, 0, 0],
       [0, 0, 5, 0],
       [0, 0, 1, 0]]

if (isDiagonalMatrix(mat)):
    print("Yes")
else:
    print("No")
