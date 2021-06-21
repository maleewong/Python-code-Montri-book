def euler_ivp(f, x0, y0, h, x):
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
  float : solution at x
  """
  for i in range(int(round((x-x0)/h))):
    y0 += f(x0, y0) * h
    x0 += h
  return y0

if __name__ == '__main__':
  f = lambda x, y : y - x  
  print(euler_ivp(f, 0, 0.5, 0.1, 1.0))
  
  
# author : worasait suwannik
# date   : jul 2015

