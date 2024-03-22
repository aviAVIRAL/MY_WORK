


import math

def minimumRateToEatBananas(v, h):
    # Find the maximum number

    # Find the minimum value of k
    for i in range(1, max(v)):
        reqTime = calculateTotalHours(v, i)
        if reqTime <= h:
            return i
        
def calculateTotalHours(v, hourly):
    totalH = 0
    n = len(v)
    # Find total hours
    for i in range(n):
        totalH += math.ceil(v[i] / hourly)
    return totalH



    # Dummy return statement

v = [7, 15, 6, 3]
h = 8
ans = minimumRateToEatBananas(v, h)
print("Koko should eat at least", ans, "bananas/hr.")


