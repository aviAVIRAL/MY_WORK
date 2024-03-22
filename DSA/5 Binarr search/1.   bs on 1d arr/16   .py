




import sys
def findKRotation(arr : [int]) -> int:
    n = len(arr)  # Size of array
    ans = float('inf')
    index = -1
    for i in range(n):
        if arr[i] < ans:
            ans = arr[i]
            index = i
    return index

if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    ans = findKRotation(arr)
    print("The array is rotated", ans, "times.")
print()

def findKRotation(arr : [int]) -> int:
    n = len(arr)  # Size of array
    ans = float('inf')
    index = -1
    for i in range(n):
        if arr[i] < ans:
            ans = arr[i]
            index = i
    return index

if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    ans = findKRotation(arr)
    print("The array is rotated", ans, "times.")


