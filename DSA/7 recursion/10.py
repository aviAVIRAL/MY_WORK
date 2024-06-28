
def f(i, k, ds):
    if k == 0:
        print(ds)
        return
    for j in range(i, len(arr)):
        if j > i and arr[j] == arr[j - 1]:
            continue
        # if arr[j] > k:
        #     break
        ds.append(arr[j])
        f(j + 1, k - arr[j], ds)
        ds.pop()

arr= [1,1,1,2,2]
f(0, 4, [])
.