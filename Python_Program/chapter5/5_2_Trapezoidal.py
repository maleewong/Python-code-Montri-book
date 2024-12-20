def trapezoidal(f, a, b, n):
  h = (b - a) / n
  s = sum(f(a + i*h) for i in range(1, n))
  return (f(a) + 2*s + f(b)) * h / 2

if __name__ == '__main__':
  from math import cos, pi
  f = lambda x : cos(x)
  a = 0
  b = pi / 2
  n = 20
  print(trapezoidal(f, a, b, n))

