

# mapping concept   

# using Counter   capital mein C hai     

from collections import Counter
nums = [1,1,1,1,3,3,3,33,   4,4]
ans = Counter(nums) # Counter({1: 4, 3: 3, 4: 2, 33: 1})
for key, val in ans.items():
    if val == 2: 
        print(key) #4 

# ...................................................

arr = [1,1,1,1,3,3,3,33,   4,4]
mp = {}
for x in arr: 
    if x not in mp: 
        mp[x] = 1
    else : 
        mp[x] += 1   # {1: 4, 3: 3, 33: 1, 4: 2}
for x in mp : 
    if mp[x] == 2 :
        print(x) #4 

# ....................................................




