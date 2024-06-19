

# ..................................................

# trick to print according to quetion op 

# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# result = searchMatrix(matrix, 8)
# print("true" if result else "false")

# ........................................................

# Brute   tc 0 ( n * m ) in both code   

# solution bby avi 
def f(mat, x):

    for i in range(len(mat)):
        if x in mat[i]:
            return True 
    return False
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(f(matrix, 11))

# sol by striver
def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == target:
                return True
    return False

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = searchMatrix(matrix, 8)
print("true" if result else "false")

# better 
 

def binarySearch(nums, target):
    n = len(nums) # size of the array
    low, high = 0, n - 1

    # Perform the steps:
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False

def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        if matrix[i][0] <= target <= matrix[i][m - 1]:
            return binarySearch(matrix[i], target)
    return False

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = searchMatrix(matrix, 8)
print("true" if result else "false")

# optimal   tc  O ( log ( N x M ) ) 

def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    # apply binary search:
    low = 0
    high = n * m - 1
    while low <= high:
        mid = (low + high) // 2
        row = mid // m
        col = mid % m
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = searchMatrix(matrix, 8)
print("true" if result else "false")







