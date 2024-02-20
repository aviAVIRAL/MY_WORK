# Count Maximum Consecutive One’s in the array
# Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

# Examples:

# Example 1:

# Input: prices = {1, 1, 0, 1, 1, 1}

# Output: 3

# Explanation: There are two consecutive 1’s and three consecutive 1’s in the array out of which maximum is 3.

# Input: prices = {1, 0, 1, 1, 0, 1} 

# Output: 2

# Explanation: There are two consecutive 1's in the array.





# optimum  tc = o(n)   sc =  o(1)

def findMaxConsecutiveOnes( arr):
    count = 0
    maxi  = 0 

    for i in range ( len(arr)):
        if arr[i] == 1:
            count +=1
            # maxi  = max(count,maxi )
        else:
            count = 0
            
        maxi  = max(count,maxi )

    return maxi 


if __name__=="__main__":
    arr = [1,0,1,1,0,1,1,1] 
    print(findMaxConsecutiveOnes(arr))



