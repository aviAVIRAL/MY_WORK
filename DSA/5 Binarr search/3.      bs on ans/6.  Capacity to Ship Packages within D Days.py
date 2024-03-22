# Capacity to Ship Packages within D Days
# Problem Statement: You are the owner of a Shipment company. You use conveyor belts to ship packages from one port to another. The packages must be shipped within ‘d’ days.
# The weights of the packages are given in an array ‘of weights’. The packages are loaded on the conveyor belts every day in the same order as they appear in the array. The loaded weights must not exceed the maximum weight capacity of the ship.
# Find out the least-weight capacity so that you can ship all the packages within ‘d’ days.

# Examples
# Example 1:
# Input Format: N = 5, weights[] = {5,4,5,2,3,4,5,6}, d = 5
# Result: 9
# Explanation: If the ship capacity is 9, the shipment will be done in the following manner:
# Day         Weights            Total
# 1        -       5, 4          -        9
# 2        -       5, 2          -        7
# 3        -       3, 4          -        7
# 4        -       5              -        5
# 5        -       6              -        6
# So, the least capacity should be 9.

# Example 2:

# Input Format: N = 10, weights[] = {1,2,3,4,5,6,7,8,9,10}, d = 1
# Result: 55
# Explanation: We have to ship all the goods in a single day. So, the weight capacity should be the summation of all the weights i.e. 55.



# brute 


def fun(weights, cap):
    days = 1  # First day
    load = 0
    n = len(weights)  # size of array

    for i in range(n):
        if load + weights[i] > cap:
            days += 1  # move to next day
            load = weights[i]  # load the weight
        else:
            # load the weight on the same day
            load += weights[i]
    
    return days

def f(weights, d):
    for i in range(max(weights), sum(weights) + 1):
        if fun(weights, i) <= d:
            return i
    # dummy return statement
    return -1

weights = [5, 4, 5, 2, 3, 4, 5, 6]
d = 5
ans = f(weights, d)
print("The minimum capacity should be:", ans)

# rep also as
def fun(weights, cap, d):
    days = 1  # First day
    load = 0
    n = len(weights)  # size of array

    for i in range(n):
        if load + weights[i] > cap:
            days += 1  # move to next day
            load = weights[i]  # load the weight
        else:
            # load the weight on the same day
            load += weights[i]

    if days <= d: return True
    else : return False

def f(weights, d) :

    for i in range(max(weights), sum(weights) + 1):
        if fun(weights, i, d) :
            return i
    # dummy return statement
    return -1

weights = [5, 4, 5, 2, 3, 4, 5, 6]
d = 5
ans = f(weights, d)
print("The minimum capacity should be:", ans)

# optimal 
print()

def fun(weights, cap, d):
    days = 1  # First day
    load = 0
    n = len(weights)  # size of array

    for i in range(n):
        if load + weights[i] > cap:
            days += 1  # move to next day
            load = weights[i]  # load the weight
        else:
            # load the weight on the same day
            load += weights[i]

    if days <= d: return True
    else : return False

def f(wt, d) :
    l = max(wt)
    h = sum(wt)
    while l <= h:
        m = (l + h)//2                             
        if fun(wt, m , d):
            h = m - 1
        else :
            l = m + 1
    return l 

                        
weights = [5, 4, 5, 2, 3, 4, 5, 6]
d = 5
ans = f(weights, d)
print("The minimum capacity should be:", ans)

print()



