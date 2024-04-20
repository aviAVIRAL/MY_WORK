


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

print("see ans eer ")

def ff(matrix):
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
    k = ff(mat)   
    for row in k:    # its working fine 
        for elem in row:
            print(elem, end=" ")
        print()

print()


def fun(matrix):
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
    k = fun(mat) 
    print(k)  
    # for i in range(len(k)):
    #     for j in range(len(k[0])):
    #         print(k[i][j], end=" ")
    #     print()

print()
#trcik to unpack 

def fu(matrix):
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
    k = fu(mat) 
    print(*k)  

print()
#trcik to unpack 

def fu(matrix):
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
    print(*fu(mat)) 


if __name__ == "__main__":
    mat = [[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]]
    k = fu(mat) 
    for row in k:
        print(*row)

print("see ans eer ")

def function(matrix):
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
    k = function(mat)   
    for row in k:    # its working fine 
        print(*row)
    print()
        

        # for elem in row:
        #     print(elem, end=" ")
        # print()


# ......        ........
print("............concept.............")


arr = [ 1, 2, 3 , 4]

for i in range(len(arr)):
    print(arr[i], end = "//")
# print() cut it

































