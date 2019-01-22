def matrix_multiply(matrix1, matrix2):
  print_matrix(matrix1)
  print_matrix(matrix2)

  r1 = len(matrix1)
  c1 = len(matrix1[0])
  r2 = len(matrix2)
  c2 = len(matrix2[0])

  rv = [[0 for _ in range(c2)] for _ in range(r1)]

  for i in range(r1):
    for j in range(c2):
      sum = 0
      for k in range(c1):
        sum += matrix1[i][k] * matrix2[k][j]
      rv[i][j] = sum
  return rv

def print_matrix(matrix):
  print("\n")
  for i in range(len(matrix)):
    print(" ".join(str(x) for x in matrix[i]))
  print("\n")


tm1 = [[1,2],[3,4],[5,6],[7,8]]
tm2 = [[1,2,3],[4,5,6]]

print_matrix(matrix_multiply(tm1, tm2))
