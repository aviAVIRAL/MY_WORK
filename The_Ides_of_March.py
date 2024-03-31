
if __name__=="__main__":
    t = int(input())

    while t > 0:
        n, x, y = map(int, input().split())
        a = list(map(int, input().split()))
        
        # Your code goes here
        print(f(a, x, y))
            
        t -= 1
