#  find equilibrium index in an arr 
  
  # Example 1:
    # Input: nums = [2,3,-1,8,4]
    # Output: 3
    # Explanation: The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
    # The sum of the numbers after index 3 is: 4 = 4

    # Example 2:
    # Input: nums = [1,-1,4]
    # Output: 2
    # Explanation: The sum of the numbers before index 2 is: 1 + -1 = 0
    # The sum of the numbers after index 2 is: 0


# m1 

def f(nums):
    n = len(nums)

    for i in range(n):
        left_sum = sum(nums[:i])
        right_sum = sum(nums[i + 1:])

        if left_sum == right_sum:
            return i


if __name__=="__main__":

    arr = [1, - 1,  4]
    print(f( arr))

print()

if __name__=="__main__":

    arr = [2, 3, -1, 8, 4]
    print(f( arr))
    
# m 2 

def f(arr):
    n = len(arr)

    for i in range( n):

        s1= 0 
        for j in range( 0 , i ): 
            s1 = s1 + arr[j]
        
        
        s2= 0 
        for k in range( i+1 , n ): 
            s2 = s2 + arr[k] 

        if s1 == s2 :
            return i 
        

if __name__=="__main__":

    arr = [1, - 1,  4]
    print(f( arr))

print()

if __name__=="__main__":

    arr = [2, 3, -1, 8, 4]
    print(f( arr))




        
