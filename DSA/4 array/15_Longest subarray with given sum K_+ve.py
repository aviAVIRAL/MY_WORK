


from typing import List

def getLongestSubarray(a: [int], k: int) -> int:
    n = len(a) # size of the array.

    length = 0
    for i in range(n): # starting index
        for j in range(i, n): # ending index
            # add all the elements of
            # subarray = a[i...j]:
            s = 0
            for K in range(i, j+1):
                s += a[K]

            if s == k:
                length = max(length, j - i + 1)
    return length

if __name__ == "__main__":
	a = [2, 3, 5, 1, 9]
	k = 10

	length = getLongestSubarray(a, k)
	print(f"The length of the longest subarray is: {length}")



from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0  # Initialize a variable to count the subarrays with sum k
        for i in range(n):
            s = 0  # Initialize the running sum
            for j in range(i, n):
                s += nums[j]  # Update the running sum
                if s == k:
                    count += 1  # Increment count when the sum equals k
        return count

if __name__ == "__main__":
	a = [1,2,3,1,1,1,1,4,2,3]
	k = 3

	length = getLongestSubarray(a, k)
	print(f"The length of the longest subarray is: {length}")
     











# ye practice ka likha hai check kr lena befor the revesion 


# # ///////////////////////////////



# print("// total no of sub arr")
# print()


# def total_number_of_subarr_haveequal_to_k(arr, k):
 
#     n = len(arr)  
#     count = 0 

#     for i in range(n):  
#         for j in range(i, n): 

#             subarray_sum = sum(arr[i:j+1])

#             if subarray_sum == k:
#                 count += 1

#     return count

 
# if __name__ == '__main__':
#     arr = [1, 1, 3, 2,1,1]

#     k = 2

#     count = total_number_of_subarr_haveequal_to_k(arr, k)
#     print("The number of subarrays is:", count)


# print()
# print()
# print("bilo")

# def findAllSubarraysWithGivenSum(arr, k):
#     n = len(arr)  # size of the given array.
#     cnt = 0  # Number of subarrays.

#     for i in range(n):  # starting index i.
#         subarray_sum = 0
#         for j in range(i, n):  

#             subarray_sum += arr[j]

#             # Increase the count if sum == k.
#             if subarray_sum == k:
#                 cnt += 1

#     return cnt

 
 
# if __name__ == '__main__':
#     arr = [1, 1, 3, 2,1,1]
#     k = 2

#     cnt = findAllSubarraysWithGivenSum(arr, k)
#     print("The number of subarrays is:", cnt)




# print( " / / ")
# print("longest length kis sub arr ki ")
# print( " / / ")


# def findAllSubarraysWithGivenSum(arr, k):
#     n = len(arr)  # size of the given array.
#     cnt = 0  # Number of subarrays.
#     length = 0 
#     for i in range(n):  # starting index i.
#         for j in range(i, n):  # ending index j.
#             # calculate the sum of subarray [i...j].
#             subarray_sum = sum(arr[i:j+1])

#             # Increase the count if sum == k.
#         if subarray_sum == k:
#             length = max(length, j - i + 1)
#     return length


 
# if __name__ == '__main__':
#     arr = [1, 2, 3, 1 ,  1]
#     k = 2

#     cnt = findAllSubarraysWithGivenSum(arr, k)
#     print("The longest of subarrays is:", cnt)


 

# def po(arr):
#     for i in range(len(arr)):
#         ans = max(arr)
#     return ans

# arr = [1,2,3,4,5,6,7]
# aw=po(arr)
# print(aw)


