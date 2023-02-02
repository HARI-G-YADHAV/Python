import numpy as np

r = int(input("Enter the order of square matrix: "))
print("Enter the entries seperated by spaces: ")
entries = list(map(int,input().split()))
matrix = np.array(entries).reshape(r,r)

det = np.linalg.det(matrix)
u,v = np.linalg.eig(matrix)

print("matrix : ",matrix)
print("Determinant = ",det)
print("Eigenvalues = ",u)
print("Eigen vector = ",v)
