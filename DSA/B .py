






# Function to find the maximum height of the mountains
def f(arr):
    max_height = 0
    for height in arr:
        if height > max_height:
            max_height = height
    return max_height


if __name__ == "__main__":
    # Input number of test cases
    T = int(input())

    # Iterate over each test case
    for _ in range(T):
        # Input number of mountains and their heights
        N = int(input())
        arr = list(map(int, input().split()))

        # Find the maximum height and print it
        print(f(arr))


# 3
# 5
# 1 2 3 4 5
# 4
# 1 2 3 4
# 2
# 12 10
