
# concept
arr = [2, 2, 1, 1, 1, 2, 9 ]
from collections import Counter
sol = Counter(arr)
print(sol)

# code 
from collections import Counter

def majorityElement(arr):
    n = len(arr)
    # Count the occurrences of each element using Counter
    counter = Counter(arr)

    # Searching for the majority element
    for num, count in counter.items():
        if count > (n // 2):
            return num

    return -1

arr = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)

print("............")


