# lower triangle to set zero in matrix 15 jan 

# ip 

#  1 2 3 4
#  1 2 3 4
#  1 2 3 4
#  1 2 3 4

# op 

# 1 0 0 0   # math | observation
# 1 2 0 0
# 1 2 3 0
# 1 2 3 4
   
def f(mat):
    n = len(mat)
    m = len(mat[0])

    for i in range(n):
        for j in range(i + 1, m):
            mat[i][j] = 0  # math | observation  
    return mat

if __name__=="__main__":
    matrix = [ [1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
    k = f(matrix)
    for i in range(len(k)):
        for j in range(len(k[0])):
            print(k[i][j], end = " ")
        print()



# + 15 jan string + matrix  so plz scheck our selg 
