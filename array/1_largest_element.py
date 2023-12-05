# largest element of arr 

# 1. brute :
# sort kr and last element return kr de 
# tc = same as sorting 

# 1. brute : 
# max()  function ka direct use kr de 

# 3. optimal   tc = o(n)  sc = o(1)
def largest_element(arr):
    largest = arr[0]
    n = len(arr)
    for i in range(0, n):
        if  arr[i] > largest  :
            largest = arr[i] 
    return largest

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)

ans = largest_element(arr)
print(ans)
