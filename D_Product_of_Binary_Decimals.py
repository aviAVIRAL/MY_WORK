
# def f(a):



    
# for _ in range(int(input())):
#     a = map(int, input().split())
#     print(f(a))






for _ in range(int(input())):
    h, m = map(int, input().split(':'))
    print(f"{(h-1)%12+1:02d}:{m:02d} {'AP'[h>11]}M")


