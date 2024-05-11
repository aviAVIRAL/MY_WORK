
def find_missing_number(arr):
    n = len(arr)
    freq = [0] * 100

    for i in range(n):
        freq[arr[i]] += 1

    for i in range(1, 100):
        if freq[i] == 0:
            

            return i
    return -1 
arr =[1,2,3,5]
ans =find_missing_number(arr)
print(ans)




