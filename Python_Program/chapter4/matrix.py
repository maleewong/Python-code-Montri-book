def column(m, c):
  return [m[i][c] for i in range(len(m))]

def row(m, r):
  return m[r][:]
   
def height(m):
  return len(m)
  
def width(m):
  return len(m[0])

def print_matrix(m):
  for i in range(len(m)):
      print(m[i])  
