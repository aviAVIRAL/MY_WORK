# check arr is sorted in Asending oder(1->2->3 chote se bada)
# optimal approach   tc = o(n)

def f(arr):
    n = len(arr)

    for i in range(n - 1):  # [ 0 to n-2 ] index range 
        if arr[i + 1] < arr[i]:
            return False
    return True


if __name__=="__main__":
    arr=[8,8,7,6,5,4,3,2]
    print("original arr:" , arr)
    print("answer is ", f(arr))
# output False


if __name__=="__main__":
    arr=[1,2,3,4]
    print("original arr:" , arr)
    print("answer is ", f(arr))
# output true

