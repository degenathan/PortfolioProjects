import numpy as np
from numpy.linalg import inv

def normalize(x):
    fac = abs(x).max()
    x_n = x / x.max()
    return fac, x_n

def build_matrix():
    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))
    print("Enter the entries in a single line (separated by space): ")
    entries = list(map(float, input().split()))
    matrix = np.array(entries).reshape(R, C)
    print(matrix)
    return matrix

def power_method():
    
    #x = np.array([1, 1])
    #a = np.array([[0, 2], [2, 3]])
    
    print("x")
    x = build_matrix()
    print("A")
    a = build_matrix()
    n = int(input("what n value: "))
    
    for i in range(n+1):
        x = np.dot(a, x)
        lambda_1, x = normalize(x)
        
        print()
        print("Eigenvector:", x)
        print("current lambda:", lambda_1)
    
    print('Eigenvalue:', lambda_1)
    print('Eigenvector:', x)
    
def inverse_power():
    a = build_matrix()
    a_inv = inv(a)
    x = build_matrix()
    for i in range(4):
        x = np.dot(a_inv, x)
        lambda_1, x = normalize(x)
    
        print('Eigenvalue:', lambda_1)
        print('Eigenvector:', x)
        print()
#6 -2 2 2 0 4 5 -1 3 2 -6 -3 6 -2 -2 1 -4 -2 -4 -1 -6 4 3 -6 0


def __find_p(x):
    return np.argwhere(np.isclose(np.abs(x), np.linalg.norm(x, np.inf))).max()

def inverse_power_method():
    A = build_matrix()
    tolerance=1e-8
    max_iterations=1000
    
    n = A.shape[0]
    x = np.ones(n)
    I = np.eye(n)
    
    q = -4
    
    p = __find_p(x)
    
    error = 1
    
    x = build_matrix()
    print("initial x", x)
    
    for i in range(max_iterations):
        
        if error < tolerance:
            break
            
        y = np.linalg.solve(A - q * I, x)   
        print("y",y)
        μ = y[p]
        print("u",μ)
        p = __find_p(y)     
        error = np.linalg.norm(x - y / y[p],  np.inf)
        print("v", error)
        x = y / y[p]
        print(x)
        μ = 1. / μ + q 
        print()
    
    return (μ, x)

def svds():
    
    A = build_matrix()
    u,s,v = np.linalg.svd(A)
    print(u)
    print(s,"s")
    print(v)
    


def least():
    
    a = build_matrix()
    b = build_matrix()
    x, residuals, rank, s = np.linalg.lstsq(a,b,rcond='warn')
    print()
    print(x)
    d = np.matmul(a,x)
    e = np.subtract(d,b)
    print()
    print(e)
    print()
    mag = np.linalg.norm(e)
    print(mag)
   

    
#1 1 1 8 4 2 27 9 3 64 16 4 125 25 5
#2.5 0.5 -2.8 -5.3 -4.5
def qr():
    a = build_matrix()
    q, r = np.linalg.qr(a, mode = 'reduced')
    print(q)
# 1 -3 8 2 4 -7 0 2 1 1 3 -5 1 -1 -3
def main():
    
    print("Program Loaded")
    
main()
'''

alpha:=-4;x:=Matrix(5,1,[1,0,0,0,0]); 
Mtemp:=ReducedRowEchelonForm(Matrix(4,5,[A-alpha*IdentityMatrix(4,4),x])); 
ytemp:=SubMatrix(Mtemp,[1..4],[5..5]); mu:=ytemp(1): for i from 2 to n do if abs(ytemp(i))>abs(mu) then mu:=ytemp(i): end if: end do: mu; nu:= alpha+1/mu; x:=1/mu*ytemp;  for k from 1 to 5 do Mtemp:=ReducedRowEchelonForm(Matrix(4,5,[A- alpha*IdentityMatrix(4,4),x]));ytemp:=SubMatrix(Mtemp,[1..4],[5. .5]); mu:=ytemp(1): for i from 2 to n do if abs(ytemp(i))>abs(mu) then mu:=ytemp(i): end if: end do: mu; nu:=alpha+1/mu; x:=1/mu* ytemp; end do;

'''