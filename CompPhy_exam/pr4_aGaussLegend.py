import numpy as np
#  Gauss-Legendre quadrature
# here the approximation for for root of legendre function is used and weight from derivative formula
#x1, w1 = np.loadtxt('rootGL(0,1.00).txt',unpack=True)
 
def gauss_legendre(f, a, b, n,*args):
    x1, w1 = np.polynomial.legendre.leggauss(n)  #x is the point and w is the weight list of the function
    x = (b-a)*x1/2 + (a+b)/2     # Roots of Legendre polynomial
    w = (b-a)/2*w1     # Weights for each root
    
    sum = 0     
    for i in range(n):
        sum += w[i] * f(x[i],*args)   # Weighted value of integrand at root
    return sum

def gauss_legendre_2d(f, a, b, c, d, Nx, Ny,*args):
    x1, w1 = np.polynomial.legendre.leggauss(Ny)  #x is the point and w is the weight list of the function
    yp = (d-c)/2*x1 + (d+c)/2
    wp = (d-c)/2*w1
    I = 0
    for i in range(Ny):
        I += wp[i]*gauss_legendre(f,a,b,Nx,yp[i],*args)
    return I

def gauss_legendre_3d(f,a,b,c,d,e,g,Nx,Ny,Nz):
    x1, w1 = np.polynomial.legendre.leggauss(Nz)  #x is the point and w is the weight list of the function
    yp = (g-e)/2*x1 + (e+g)/2
    wp = (g-e)/2*w1
    I = 0
    for i in range(Nz):
        I += wp[i]*gauss_legendre_2d(f,a,b,c,d,Nx,Ny,yp[i])
    return I

def f(r1,r2,th):
    fn= (r1**2 * r2**2 * np.sin(th) * np.exp( -2*(r1 + r2) ) )/( np.sqrt(r1**2 + r2**2 - 2*r1*r2*np.cos(th)))
    return fn

nt=149
intg_prev= 8*np.pi**2 * gauss_legendre_3d(f,0,10,0,10,0,np.pi,nt,nt,nt)
print(intg_prev)
for n in range(nt+1,200):

    intg = 8*np.pi**2 * gauss_legendre_3d(f,0,10,0,10,0,np.pi,n,n,n)
    diff = abs(intg-intg_prev)
    print('At n = {}, the difference between two values is {}'.format(n,diff))
    if diff<=0.00001:
        print('The number of mesh grid needed = {}\nThe intigral value = {}'.format(n,intg))
        break
    print('running...')
    intg_prev=intg
