def runge_kutta(f, x0, y0, h, x):
  for i in range(int(round((x-x0)/h))):
    k1 = h*f(x0,         y0)
    k2 = h*f(x0 + 0.5*h, y0 + 0.5*k1)
    k3 = h*f(x0 + 0.5*h, y0 + 0.5*k2)
    k4 = h*f(x0 +     h, y0 +     k3)
    
    y0 += (k1 + 2*k2 + 2*k3 + k4)/6
    x0 += h
    
  return y0
  
if __name__ == '__main__':
  f = lambda x, y : -2*x**3 + 12*x**2 - 20*x + 10
  print(runge_kutta(f, 0, 1, 0.5, 4))




