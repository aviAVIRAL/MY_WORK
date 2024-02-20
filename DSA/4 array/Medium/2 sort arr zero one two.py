
# Sort an array of 0s, 1s and 2s
# Problem Statement: Given an array consisting of only 0s, 1s, and 2s. Write a program to in-place sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)

# Examples
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Input: nums = [2,0,1]
# Output: [0,1,2]

# Input: nums = [0]
# Output: [0]



# brute  :     tc  o(nlogn)     sc 0(n)  # using merge sort  

# better 1  :  tc o( 4n )   sc = o(n)   


def f (arr ):
    n = len(arr)
    temp = []

    for i in range ( n):
        if  arr[i] == 0 :
            temp.append(arr[i])
    for x in arr : 
        if x == 1 : 
            temp.append(x)
    for x in arr : 
        if x == 2 : 
            temp.append(x)

    j = 0 
    for i in range(len(temp)): 
        arr[j] = temp[i]
        j += 1 

    return arr 

if __name__=="__main__":
    arr= [2,0,1,0,1,2]
    print(f(arr))



# better 2   tc = 0(2n)   sc = 0(1)
    
def sortArray(arr):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0

    for num in arr:
        if num == 0:
            cnt0 += 1
        elif num == 1:
            cnt1 += 1
        else:
            cnt2 += 1

    for i in range(cnt0):
        arr[i] = 0

    for i in range(cnt0, cnt0 + cnt1):
        arr[i] = 1

    for i in range(cnt0 + cnt1, len(arr)):
        arr[i] = 2

    return arr

if __name__ == "__main__": 
    n = 6
    arr = [0, 2, 1, 2, 0, 1]
    k = sortArray(arr)
    for X in k:
        print(X, end=" ")
    print()


#  optimal  tc 0(n)   sc 0(1)
    
    # dench french algo 

def sortArray(arr):
    n = len(arr)

    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

n = 6
arr = [0, 2, 1, 2, 0, 1]
sortArray(arr)
print("After sorting:")
for num in arr:
    print(num, end=" ")
print()
   

