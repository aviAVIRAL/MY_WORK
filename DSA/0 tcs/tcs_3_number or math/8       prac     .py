
# error in code 
arr = [ 1, 9, 10,-30, 5, 1 ]
k = 10 

maxi = -1
temp =  [] 
n = len(arr)
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum += arr[j]
        if sum > maxi :
            maxi = max(maxi, sum )
            temp.append(arr[i:j+1])
print( maxi)
print(temp)
print()
# print()
# 20
# [[1], [1, 9], [1, 9, 10]]

# correct code 
arr = [1, 9, 10, -30, 5, 1]
k = 10

maxi = -1
subarr = []
n = len(arr)

for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += arr[j]
        if sum > maxi:
            maxi = sum
            subarr = arr[i:j+1]

print( maxi)
print(subarr)


# op 
# 20
# [1, 9, 10]
    

    