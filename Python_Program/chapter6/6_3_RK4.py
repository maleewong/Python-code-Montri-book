def runge_kutta(f, x0, y0, h, x):
  """
  Parameters
  ----------
  f  : function
  x0 : float :  initial value
  y0 : float :  initial value
  h  : float :  step size
  x  : float 
      
  Returns
  -------  
  float : f at x
  """
  for i in range(int(round((x-x0)/h))):
    k1 = f(x0,         y0)
    k2 = f(x0 + 0.5*h, y0 + 0.5*k1*h)
    k3 = f(x0 + 0.5*h, y0 + 0.5*k2*h)
    k4 = f(x0 +     h, y0 +     k3*h)
    
    y0 += (k1 + 2*k2 + 2*k3 + k4)*h/6
    x0 += h
    
  return y0
  
if __name__ == '__main__':
  f = lambda x, y : -2*x**3 + 12*x**2 - 20*x + 10
  print(runge_kutta(f, 0, 1, 0.5, 4))

# author : worasait suwannik
# date   : jul 2015



