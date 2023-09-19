# # 1. brute force   tc = o(n*n) ~> n^2    sc = o(1) 

# def missing_value(arr):

#     for i in range( len(arr)+1):   # n = len(arr)
#         flag = 0
#         for j in range(len(arr)):  
#             if arr[j] == i :
#                 flag = 1
#                 break
#         if flag == 0 :
#             break
#     return i 
  

# arr =[0, 1, 2, 3,     5 ,6 ]
# ans = missing_value(arr )
# print (ans)

# # 2. better solution 

# # using Hashing 

# def missingNumber(a, N):
#     hash = [0] * (N + 1)  # hash array

#     # storing the frequencies:
#     for i in range(N - 1):
#         hash[a[i]] += 1

#     # checking the frequencies for numbers 1 to N:
#     for i in range(1, N + 1):
#         if hash[i] == 0:
#             return i

# #  Example usage:
# arr = [1, 2, 3, 5]

# N = 5
# ans = missingNumber(arr, N)
# print(ans)



# def missingNumber(arr):
#     hash = [0] * (len(arr) + 1)  # Initialize a list to store frequencies

#     # Count the frequencies of numbers in 'arr'
#     for i in range(len(arr)):
#         hash[arr[i]] += 1

#     # Check for the missing number in the range 1 to len(arr)
#     for i in range(1, len(arr) + 1):
#         if hash[i] == 0:
#             return i

# # Example usage:
# arr = [1, 2, 3, 5]
# ans = missingNumber(arr)
# print(ans)



# //////////////////
# # chat Gpt:-
# def missing_value_(arr):
#     for i in range(len(arr) + 1):
#         if i not in arr:
#             return i
#     return -1  # Return -1 if no missing value is found

# arr = [0, 1, 2, 3, 5, 6]
# ans = missing_value_(arr)
# print(ans)
# //////////////////



def mssing(arr):
    
    hash = [0] * ( len(arr) + 1 )
    
    for i in range (len(arr) - 1 ):
        hash[ arr[i] ] += 1 

    for i in range(1, len(arr) + 1):
        if hash[i] == 0:
            return i
        
arr =[1,2,3,5]
ans =mssing(arr)
print(ans)
print()
arr =[1,2,1,3,5]
ans =mssing(arr)
print(ans)







