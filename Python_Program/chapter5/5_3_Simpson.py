def simpson(f, a, b, n):
  h = (b - a) / n
  sum1 = sum(f(a + (2*i + 2)*h) for i in range(0, int(n/2) - 1))
  sum2 = sum(f(a + (2*i + 1)*h) for i in range(0, int(n/2)))
  return (f(a) + 2*sum1 + 4*sum2 + f(b)) * h / 3

if __name__ == '__main__':
  from math import cos, pi
  f = lambda x : cos(x)
  a = 0
  b = pi / 2
  n = 20
  print(simpson(f, a, b, n))


