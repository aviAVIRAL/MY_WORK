
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

# optimal using set data strutur
#   tc  n + 3n or 4n   sc 1 

# Time Complexity: O(N) + O(2*N) ~ O(3*N), where N = size of the array.
# Reason: O(N) for putting all the elements into the set data structure. After that for every starting element, we are finding the consecutive elements. Though we are using nested loops, the set will be traversed at most twice in the worst case. So, the time complexity is O(2*N) instead of O(N2).
# Space Complexity: O(N), as we are using the set data structure to solve this problem.

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



# ...........100 % correct code...
# bhai ye aapne  aap kiya hai HashMap  

print()

def f(a):
    n = len(a) 
    a.sort()
    mp = { }
    for x in a : 
        if x not in mp : 
            mp[x] = 1 
        else : 
            mp[x] += 1 
    return mp  

# if --name--  "--mian--":
a = [100, 200, 1, 2, 3, 4]
k = f(a) # {1: 1, 2: 1, 3: 1, 4: 1, 100: 1, 200: 1}
sol = [(key,val) for key, val in k.items()] # [(1, 1), (2, 1), (3, 1), (4, 1), (100, 1), (200, 1)]

temp = [ ]
for x, y in sol: 
    temp.append(x)   # [1, 2, 3, 4, 100, 200]

cnt = 1
maxi = -1 
for i in range(len(temp)-1):
    if temp[i] + 1 == temp[i+1]:
        cnt += 1
        maxi = max(maxi , cnt )
    else : 
        cnt = 1 
print(maxi) 
 


