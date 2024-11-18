from gauss import *

def least_square(x, y, order, sys_lin_method=gaussian_elimination):
 
  sx  = [sum(x[j]**i        for j in range(len(x))) for i in range(order*2+1)]
  sxy = [sum(x[j]**i * y[j] for j in range(len(x))) for i in range(order+1)]
  m = []
  for i in range(order+1):
    a = sx[i:(i+order+1)]
    a.append(sxy[i])
    m.append(a)
  return sys_lin_method(m)

if __name__ == '__main__':
  x = [0, 0.5, 1, 1.5, 2, 2.5]  # data from http://web.iitd.ac.in/~pmvs/courses/mel705/curvefitting.pdf
  y = [0.0674, -0.9156, 1.6253, 3.0377, 3.3535, 7.9409]
  print(least_square(x, y, 2))
  
