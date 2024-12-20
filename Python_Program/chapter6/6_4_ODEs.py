def euler_single(fs, x0, y0s, h):
  return [y0s[i] + fs[i](x0, y0s)*h for i in range(len(y0s))]

def runge_kutta_single(f, x0, y0s, h):
  n = len(y0s)
  k1s = [h*fs[i](x0, y0s)         for i in range(n)]
  yts = [y0s[i] + 0.5*k1s[i]  for i in range(n)]
  k2s = [h*fs[i](x0 + 0.5*h, yts) for i in range(n)]
  yts = [y0s[i] + 0.5*k2s[i]  for i in range(n)]
  k3s = [h*fs[i](x0 + 0.5*h, yts) for i in range(n)]
  yts = [y0s[i] + k3s[i]      for i in range(n)]
  k4s = [h*fs[i](x0 + h, yts)     for i in range(n)]

  return [y0s[i] + (k1s[i] + 2*k2s[i] + 2*k3s[i] + k4s[i])/6 for i in range(n)]
    
def sys_ode(fs, x0, y0s, h, x, method=runge_kutta_single):
  for i in range(int((x-x0)/h)):
    y0s = method(fs, x0, y0s, h) 
    x0 += h
  return y0s

if __name__ == '__main__':
  fs = [
    lambda x, ys : ys[1],
    lambda x, ys : 2*ys[1] - 3*ys[0]
  ]
  ys = sys_ode(fs, 0, [4, 6], 0.5, 2, euler_single)
  print(ys)