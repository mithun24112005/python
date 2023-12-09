# to add two matrices
def matrix(m,n):
    o=[]
    for i in range(m):
        row=[]
        for j in range(n):
            inp=int(input(f"enter O[{i}][{j}] "))
            row.append(inp)
        o.append(row)
    return o

def sum(A,B):
    output=[]
    for i in range(len(A)): #num of rows
        row=[]
        for j in range(len(A[0])): #num of colls
            row.append(A[i][j] + B[i][j])
        output.append(row)
    return output


#for m x n matrix
m=int(input("enter the value of m rows: ")) #rows
n=int(input("enter the value of n colls: ")) #collomn
print("enter matrix A")
A=matrix(m,n)
print(A)
print("enter matrix B")
B=matrix(m,n)
print(B)
print(sum(A,B))



