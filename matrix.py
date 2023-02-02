import numpy as np
r1 = int(input("Enter the number of row of first: "))
c1 = int(input("Enter the number of column of first: "))
entries1 = list(map(int,input("Enter the elements seperated by spaces: ").split()))
matrix1 = np.array(entries1).reshape(r1,c1)
print("Matrix1 :\n",matrix1)

r2 = int(input("\nEnter the number of row of sec: "))
c2 = int(input("Enter the number of column of sec: "))
entries2 = list(map(int,input("Enter the elements seperated by spaces: ").split()))
matrix2 = np.array(entries2).reshape(r2,c2)
print("Matrix2 :\n",matrix2)

if(c1 != r2):
    print("multiplication not possible")
else:
    result=np.dot(matrix1,matrix2)
    M=np.array(result).reshape(r1,c2)
    print("Result :\n",M)
