# Allocate Minimum Number of Pages
# Problem Statement: Given an array ‘arr of integer numbers, ‘ar[i]’ represents the number of pages in the ‘i-th’ book. There are a ‘m’ number of students, and the task is to allocate all the books to the students.
# Allocate books in such a way that:

# Each student gets at least one book.
# Each book should be allocated to only one student.
# Book allocation should be in a contiguous manner.
# You have to allocate the book to ‘m’ students such that the maximum number of pages assigned to a student is minimum. If the allocation of books is not possible. return -1

# Examples
# Example 1:
# Input Format: n = 4, m = 2, arr[] = {12, 34, 67, 90}
# Result: 113
# Explanation: The allocation of books will be 12, 34, 67 | 90. One student will get the first 3 books and the other will get the last one.

# Example 2:
# Input Format: n = 5, m = 4, arr[] = {25, 46, 28, 49, 24}
# Result: 71
# Explanation: The allocation of books will be 25, 46 | 28 | 49 | 24.

# brute 

def countStudents(arr, pages):
    n = len(arr)  # size of array
    students = 1
    pagesStudent = 0
    for i in range(n):
        if pagesStudent + arr[i] <= pages:
            # add pages to current student
            pagesStudent += arr[i]
        else:
            # add pages to next student
            students += 1
            pagesStudent = arr[i]
    return students

def findPages(arr, n, m):
    # book allocation impossible
    if m > n:
        return -1

    low = max(arr)
    high = sum(arr)

    for pages in range(low, high + 1):
        if countStudents(arr, pages) == m:
            return pages
    return low

arr = [25, 46, 28, 49, 24]
n = 5
m = 4
ans = findPages(arr, n, m)
print("The answer is:", ans)


# optimal

def countStudents(arr, pages):
    n = len(arr)  # size of array
    students = 1
    pagesStudent = 0
    for i in range(n):
        if pagesStudent + arr[i] <= pages:
            # add pages to current student
            pagesStudent += arr[i]
        else:
            # add pages to next student
            students += 1
            pagesStudent = arr[i]
    return students

def findPages(arr, n, m):
    # book allocation impossible
    if m > n:
        return -1

    low = max(arr)
    high = sum(arr)
    while low <= high:
        mid = (low + high) // 2
        students = countStudents(arr, mid)
        if students < m:
            high = mid - 1
        else:
            low = mid + 1
    return low

arr = [25, 46, 28, 49, 24]
n = 5
m = 4
ans = findPages(arr, n, m)
print("The answer is:", ans)







