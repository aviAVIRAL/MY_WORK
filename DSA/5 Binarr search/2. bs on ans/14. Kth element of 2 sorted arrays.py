# K-th Element of two sorted arrays


# 12

# 1
# Problem Statement: Given two sorted arrays of size m and n respectively, you are tasked with finding the element that would be at the kth position of the final sorted array.

# Examples :

# Input: m = 5
#        n = 4
#        array1 = [2,3,6,7,9]
#        array2 = [1,4,8,10]
#        k = 5

# Output:
#  6

# Explanation: Merging both arrays and sorted. Final array will be -
#  [1,2,3,4,6,7,8,9,10]
# We can see at k = 5 in the final array has 6. 


# Input:
#  m = 1
#        n = 4
#        array1 = [0]
#        array2 = [1,4,8,10]
#        k = 2

# Output:
#  4

# Explanation:
#  Merging both arrays and sorted. Final array will be -
#  [1,4,8,10]
# We can see at k = 2 in the final array has 4



def kthelement(array1, array2, m, n, k):
    p1 = 0
    p2 = 0
    counter = 0
    answer = 0


    while (p1 < m and p2 < n):
        if (counter == k):
            break
        elif (array1[p1] < array2[p2]):
            answer = array1[p1]
            p1 += 1
        else:
            answer = array2[p2]
            p2 += 1
        counter += 1
    if (counter != k):
        if (p1 != m-1):
            answer = array1[k-counter]
        else:
            answer = array2[k-counter]
    return answer




if __name__ == "__main__":
    array1 = [2, 3, 6, 7, 9]
    array2 = [1, 4, 8, 10]
    m = len(array1)
    n = len(array2)
    k = 5
    print("The element at the kth position in the final sorted array is",
          kthelement(array1, array2, m, n, k))





















