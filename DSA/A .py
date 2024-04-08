def is_good_subarray(arr):
    counts = [0] * 21
    for num in arr:
        counts[num] += 1
    for count in counts:
        if count % 2 != 0:
            return False
    return True

def get_ans(n, A, q, t, queries):
    MOD = 10**9 + 7
    total_sum = 0
    
    for query in queries:
        if query[0] == 1:
            l, r = query[1], query[2]
            subarray = A[l-1:r]  # Adjust indices to Python's 0-based indexing
            if is_good_subarray(subarray):
                total_sum += (r - l + 1)
    
    return total_sum % MOD

# Sample Input 1
n1 = 5
A1 = [1, 2, 3, 4, 5]
q1 = 2
t1 = 3
queries1 = [[1, 0, 1], [1, 1, 4]]  # Adjusted to 0-based indexing

# Sample Output 1
output1 = get_ans(n1, A1, q1, t1, queries1)
print("Sample Output 1:", output1)


print()
n2 = 4
A2 = [1, 1, 1, 2]
q2 = 3
t2 = 3
queries2 = [[1, 1, 4], [2, 1, 2], [1, 1, 4]]

# Sample Output 2
output2 = get_ans(n2, A2, q2, t2, queries2)
print("Sample Output 2:", output2)