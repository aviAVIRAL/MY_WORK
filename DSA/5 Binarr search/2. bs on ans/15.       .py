




def f(arr, x, y):
    n = len(arr)
    sumi = sum(arr)
    ans = x 
    for i in range(n):
        if arr[i] > y:
            ans += arr[i] - y

    if ans < sumi :
        return "COUPON"
    else:
        return "NO COUPON"
    
if __name__=="__main__":
    arr = [15, 8, 22, 6]
    print(f(arr, 30, 10))
if __name__=="__main__":
    arr = [15, 8, 22, 6]
    print(f(arr, 40, 10))



# 4 34 10
# 15 8 22 6
# 2 10 100
# 60 80
# 3 30 5
# 50 60 50

    
# COUPON
# NO COUPON
# NO COUPON
# COUPON
# NO COUPON








