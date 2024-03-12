# dublicate bee hai to bus ye edge case fit ke de 



        # # Edge case  :    [ 3,1,4,5,3,3,3,3,3] target = 3
        # if arr[low] == arr[mid] and arr[mid] == arr[high]:
        #     low += 1
        #     high -= 1
        #     continue




def f(arr):
    low = 0
    high = len(arr) - 1
    ans = float("inf")

    while low <= high:
        mid = (low + high) // 2

        
        # Edge case  :    [ 3,1,4,5,3,3,3,3,3] target = 3
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue

        if arr[low] <= arr[mid]:  # if left part is sorted
            ans = min(ans, arr[low])  # keep the minimum
            low = mid + 1  # eliminate left half
            
        else:  # if right part is sorted
            ans = min(ans, arr[mid])  # keep the minimum
            high = mid - 1  # eliminate right half

    return ans

if __name__ == "__main__":
    arr = [ 3,1,4,5,3,3,3,3,3] 
    ans = f(arr)
    print("The minimum element is:", ans)




