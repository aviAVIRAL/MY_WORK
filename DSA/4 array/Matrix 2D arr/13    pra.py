

def f(matrix):
    n = len(matrix)
    
    temp = [[0] * n for _ in range(n)]
    
    
    for i in range(n):
        for j in range(n):
            temp[j][n - i - 1] = matrix[i][j]
    return temp


if __name__ == "__main__":
    mat = [[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]]
    k = f(mat)   
    for i in range(len(k)):
        for j in range(len(k[0])):
            print(k[i][j], end=" ")
        print()


print("...........................")
print("...........................")


t = [ [0]*4 for _ in range(3)]
print(t)

print()


print(4*4)  
print([1]*4 )

print( "1" * 4)
print( )
print( )
print( )
print( )



arr = [ 1,2  ,3]

print(*arr)


str = "123"
print(*str)


print()

if __name__ == "__main__":
    mat = [[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]]
    k = f(mat)   
    for i in range(len(k)):
        for j in range(len(k[0])):
            print(k[i][j], end=" ")
        print()

print()

if __name__ == "__main__":
    mat = [[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]]
    k = f(mat)   
    for i in range(len(k)):
        for j in range(len(k[0])):
            print(k[i][j], end = " ")
        # print()   # 7 4 1 8 5 2 9 6 3

print( )
print( )

if __name__ == "__main__":
    mat = [[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]]
    k = f(mat)   
    for row in mat:
        for elem in row:
            print(elem, end=" ")
        print()


print( )
print( )