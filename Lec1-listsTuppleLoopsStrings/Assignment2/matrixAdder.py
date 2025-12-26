"""The Matrix Adder: Create two 2x2 matrices (lists of lists): matrix_A = [[1, 2], [3, 4]] matrix_B = [[5, 6], [7, 8]] Write a program using nested loops to add these two matrices together. The result should be a new matrix where each element is the sum of the corresponding elements from A and B.
Target Output: [[6, 8], [10, 12]]
"""
matrix_A = [[1, 2], [3, 4]]
matrix_B = [[5, 6], [7, 8]]

sum = [[0,0],[0,0]]
for i in range(0,2):
    for j in range(0,2):
        sum[i][j] = matrix_A[i][j] + matrix_B[i][j]

print(sum)