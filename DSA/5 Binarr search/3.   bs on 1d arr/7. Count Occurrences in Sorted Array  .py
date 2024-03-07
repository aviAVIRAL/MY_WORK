# Count Occurrences in Sorted Array
# Problem Statement: You are given a sorted array containing N integers and a number X, you have to find the occurrences of X in the given array.

# Examples
# Example 1:
# Input: N = 7,  X = 3 , array[] = {2, 2 , 3 , 3 , 3 , 3 , 4}
# Output: 4
# Explanation: 3 is occurring 4 times in 
# the given array so it is our answer.

# Example 2:
# Input: N = 8,  X = 2 , array[] = {1, 1, 2, 2, 2, 2, 2, 3}
# Output: 5
# # Explanation: 2 is occurring 5 times in the given array so it is our answer.

# brute  tc n  

def count(arr,n,x) :
    cnt = 0
    for i in range(n):
        if arr[i] == x:
            cnt += 1
    return cnt
if __name__ == "__main__":
    arr = [2, 4, 6, 8, 8, 8, 11, 13]
    n = 8
    x = 8
    ans = count(arr, n, x)
    print("The number of occurrences is:", ans)


# optimal   O(2*logN)  
    # first occ - last occ + 1 
    
