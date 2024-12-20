from matrix import height

def gaussian_elimination(m):
  # forward elimination
  n = height(m)
  for i in range(n):
    for j in range(i+1, n):
      m[j] = [m[j][k] - m[i][k]*m[j][i]/m[i][i] for k in range(n+1)]

  if m[n-1][n-1] == 0: raise ValueError('No unique solution')

  # backward substitution
  x = [0] * n
  for i in range(n-1, -1, -1):  # for i in reversed(range(n)):
    s = sum(m[i][j] * x[j] for j in range(i, n))
    x[i] = (m[i][n] - s) / m[i][i]
  return x

if __name__ == '__main__':
  m = [[2,1,2,1,3], [4,-2,-4,6,2], [6,2,3,-1,-3], [4,3,3,3,8]]
  print(gaussian_elimination(m))   # [-1.0, 1.0, 1.0, 2.0]
  
