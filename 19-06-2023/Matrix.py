# Prog1
# get 1 matrix as input . display diagonal elements, non-diagonal , upper, lower diagonal elements
row = int(input("Enter no.of rows :"))
col = int(input("Enter no.of cols :"))
print("Enter", row*col," matrix elements :")
matrix = []
for i in range(row):
    row = []
    for j in range(col):
        ele = int(input())
        row.append(ele)
    matrix.append(row)

#Display the Matrix
print("The Matrix is :-")
for row in matrix:
    for ele in row:
        print(ele, end=' ')
    print()
    
#Diagonal  Matrix
print("The Doagonal Matrix is :-")
for i in range (len(matrix)):
    for j in range (len(matrix[0])):
        if(i==j):
            print(matrix[i][j], end=' ')
        else:
            print(' ',end=' ')
    print()

#Upper Triangle  Matrix
print("The Upper Triangle Matrix is :-")
for i in range (len(matrix)):
    for j in range (len(matrix[0])):
        if(i<=j):
            print(matrix[i][j], end=' ')
        else:
            print(' ',end=' ')
    print()

#Lower Triangle  Matrix
print("The Lower Triangle Matrix is :-")
for i in range (len(matrix)):
    for j in range (len(matrix[0])):
        if(i>=j):
            print(matrix[i][j], end=' ')
        else:
            print(end=' ')
    print()

#Transpose  Matrix
print("The Transposed Matrix is :-")
for i in range (len(matrix)):
    for j in range (len(matrix[0])):
        print(matrix[j][i], end=' ')
    print()