
# Longest Consecutive Sequence in an Array.

# Problem Statement: You are given an array of ‘N’ integers. 
# You need to find the length of the longest sequence which contains the consecutive elements.

# Examples
# Example 1:
# Input: [100, 200, 1, 3, 2, 4]

# Output: 4
# Explanation: The longest consecutive subsequence is 1, 2, 3, and 4.

# Input: [3, 8, 5, 7, 6]
# Output: 4
# Explanation: The longest consecutive subsequence is 5, 6, 7, and 8.


# brute   tc ~ n^2   sc 1

# r1 

def linearSearch(a, num):
    n = len(a)  
    for i in range(n):
        if a[i] == num:
            return True
    return False


def longestSuccessiveElements(a):
    n = len(a)  
    longest = 1
    for i in range(n):
        x = a[i]
        cnt = 1
        while linearSearch(a, x + 1):
            x += 1
            cnt += 1

        longest = max(longest, cnt)
    return longest


a = [100, 200, 1, 2, 3, 4]
ans = longestSuccessiveElements(a)
print("The longest consecutive sequence is", ans)


# r2 


def linearSearch(a, num):
    n = len(a)  # size of array
    for i in range(n):
        if a[i] == num:
            return True
    return False


def longestSuccessiveElements(a):
    n = len(a)  # size of array
    longest = 1

    for i in range(n):
        x = a[i]
        cnt = 1
        while linearSearch(a, x + 1) == True : # see
            x += 1
            cnt += 1

        longest = max(longest, cnt)
    return longest


a = [100, 200, 1, 2, 3, 4]
ans = longestSuccessiveElements(a)
print("The longest consecutive sequence is", ans)

# better   tc  nlogn + n    sc 1

def longestSuccessiveElements(a):
    
    n = len(a)
    if n == 0:
        return 0

    # sort the array
    a.sort()

    lastSmaller = float('-inf')
    cnt_curr = 0
    longest = 1

    for i in range(n):
    
        if a[i] - 1 == lastSmaller:   
            cnt_curr += 1
            lastSmaller = a[i]
    
        elif a[i] != lastSmaller:
            cnt_curr = 1
            lastSmaller = a[i]
    
        longest = max(longest, cnt_curr)

    return longest

a = [100,100,102,101,12,13,11,14,11,12,13,14]
ans = longestSuccessiveElements(a)
print("The longest consecutive sequence is", ans)

# optimal  using set data strutur 

# concept   set()  mein kese dale arr ke elm 

# m1 
arr = [ 4,1,2,3,4,4,5,5]
n = len(arr)
st = set()
for i in range(n):
    st.add(arr[i])
print(st)

# m2
arr = [ 1,2,3,4,4,5,5]
n = len(arr)
st = set(arr)    
print(st)

# optimal tc   sc 


def f(a):
    n = len(a)
    if n == 0:
        return 0

    longest = 1
    st = set()
    for i in range(n):
        st.add(a[i])

    for elm in st:
        if elm - 1 not in st:
            cnt = 1
            x = elm
            while x + 1 in st:
                x += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest

if __name__=="__main__":
    a = [100,200,1,2,3,3,101,101,2,3, 4]
    ans = f(a)
    print(ans)
