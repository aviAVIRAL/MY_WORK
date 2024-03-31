

def f(a, k):
    n = len(a)
    if n <= 2 : 
        return 2
    

    j = 0 
    i = n-1
    while( i < j ):
        if a[j] % k != 0:
            a[j] = a[j]*k
        elif a[i] % k == 0:
            a[i] = a[i] % k     

        i += 1 
        j -= 1
        
    cnt = 0 
    for x in a:
        if x > k :
            cnt += 1 
    return cnt 


if __name__=="__main__":
    t = int(input())

    while t > 0:
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        
        # Your code goes here
        print(f(a, k))
            
        t -= 1
