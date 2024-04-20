
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
a = [100, 200, 1, 2, 3, 4]
print(f(a))
# k = f(a)
# cnt = 1 
# maxi = -1 
# for x in k : 
#     if 


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

# # ................
# ple 1:
# Input:
#  [100, 200, 1, 3, 2, 4]

# Output:
#  4

# Explanation:
#  The longest consecutive subsequence is 1, 2, 3, and 4.

# Input:
#  [3, 8, 5, 7, 6]

# Output:
#  4

# Explanation:
#  The longest consecutive subsequence is 5, 6, 7, and 8.
# Practice:
# Solve Problem
# code-studio
print()
print()
print()
mp = {1: 1, 2: 1, 3: 1, 4: 1, 100: 1, 200: 1}
sol = [(key, val) for key, val in mp.items()]

print(sol)


# print("letsee")



