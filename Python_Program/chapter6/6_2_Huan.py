def huen(f, x0, y0, h, x):   # Modified Euler Method 
  for i in range(int(round((x-x0)/h))):
    k1 = f(x0, y0)
    k2 = f(x0 + h, y0 + k1*h)
    
    y0 += (0.5*k1 + 0.5*k2)*h
    x0 += h
  return y0
  
def midpoint(f, x0, y0, h, x):
  for i in range(int(round((x-x0)/h))):
    k1 = f(x0, y0)
    k2 = f(x0 + 0.5*h, y0 + 0.5*k1*h)
    
    y0 += k2*h
    x0 += h
  return y0
  
if __name__ == '__main__':
  f = lambda x, y : y - x
  print(huen(f, 0, 0.5, 0.1, 1))  
