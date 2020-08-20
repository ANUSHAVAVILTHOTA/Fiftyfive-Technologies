m=int(input())
n=int(input())
matrix=[[int(input()) for x in range(m)]for y in range(n)]
# print(matrix)
def changeRowCoulmn(matrix,m,n,x,y):
    for j in range(n):
        if matrix[x][j]:
            matrix[x][j]=-1
    for i in range(m):
        if matrix[i][y]:
            matrix[i][y]=-1
for i in range(0,m):
    for j in range(0,n):
        if(matrix[i][j]==0):
            changeRowCoulmn(matrix,m,n,i,j)

    #matrix transfer -1 to 0
for i in range(m):
    for j in range(n):
        if matrix[i][j]==-1:
            matrix[i][j]=0
for row in matrix:
    print(row)

    
