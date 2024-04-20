from itertools import permutations
def f(nums):
    x = tuple(nums) # concept 
    nums.sort()
    sol = [x for x in permutations(nums)]
    print(sol)
    n = len(sol)
    if x == sol[n-1]:
        return sol[0]
    for i in range(n - 1):
        if sol[i] == x :
            return sol[ i +1 ]
            
nums =[ 1,5,1  ]
print(f(nums))

# ,,,,,,,,,,,,,,,,,,,,,,,,,,

# nums =
# [1,5,1]

# Use Testcase
# Output
# [1,1,5]
# Expected
# [5,1,1]

print("hhhhhhhhhhhhhhhhhh")
from itertools import permutations
def f(nums):
    x = tuple(nums) # concept 
    # nums.sort()
    sol = [x for x in permutations(nums)]
    print(sol)
    n = len(sol)
    if x == sol[n-1]:
        return sol[0]
    for i in range(n - 1):
        if sol[i] == x :
            return sol[ i +1 ]
print()            
nums =[ 1,5,1  ]
print(f(nums))
