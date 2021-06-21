import numpy as np
import matplotlib.pyplot as plt

def Runge_Kutta(f, t0, y0s, dt):
  n = len(y0s)
  k1s = [fs[i](t0, y0s)          for i in range(n)]
  yts = [y0s[i] + 0.5*dt*k1s[i]  for i in range(n)]
  k2s = [fs[i](t0 + 0.5*dt, yts) for i in range(n)]
  yts = [y0s[i] + 0.5*dt*k2s[i]  for i in range(n)]
  k3s = [fs[i](t0 + 0.5*dt, yts) for i in range(n)]
  yts = [y0s[i] + dt*k3s[i]      for i in range(n)]
  k4s = [fs[i](t0 + dt, yts)     for i in range(n)]
  return [y0s[i] + (k1s[i] + 2*k2s[i] + 2*k3s[i] + k4s[i])*dt/6 for i in range(n)]

def sys_ode(fs, t0, y0s, dt, tn):
  t=[]
  y1s=[]
  y2s=[]
  for i in range(int((tn-t0)/dt)):
    y0s = Runge_Kutta(fs, t0, y0s, dt)
    y1s.append(y0s[0])
    y2s.append(y0s[1])
    t.append(t0)
    t0 = t0 + dt
  return y1s, y2s

if __name__ == '__main__':
  fs = [
    lambda t, ys : 0.5*ys[0] - 0.02*ys[0]*ys[1],
    lambda t, ys : 0.004*ys[0]*ys[1] - 0.4*ys[1]
  ]
  
  y1, y2 = sys_ode(fs, 0, [20, 40], 0.01, 50)
  plt.plot(y1,y2)
  plt.xlabel("prey")
  plt.ylabel("predator")
  plt.savefig('predator-circle.eps', format='eps') 
  plt.show()
 
  
