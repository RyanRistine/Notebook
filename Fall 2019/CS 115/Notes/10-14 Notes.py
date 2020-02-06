grid = [[1, 2 ,3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
def nicePrint(A):
  for row in range (len(A)):
      for col in range (len(A[row])):
        print(A[row][col], end = " ")
      print()

def columnPrint(A, j):
    for i in range (len(A)):
        print(A[i][j])

def columnSum(A, j):
    total = 0
    for i in range(len(A)):
        total += A[i][j]
    print(total)

columnSum(grid, 1)
columnPrint(grid, 1)
nicePrint(grid)
