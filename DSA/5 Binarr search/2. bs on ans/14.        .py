
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
    t = int(input())

    while t > 0:
        n, x, y = map(int, input().split())
        a = list(map(int, input().split()))
        
        # Your code goes here
        print(f(a, x, y))
            
        t -= 1

