
# from math import ceil

# for T in range(int(input())):
    
#     A,B = map(int,input().split())
    
#     if A >= B + 10:
#         print(0)
        
#     else:
#         left  = B + 10 - A
#         shots = ceil(left/3)
#         print(shots)
        


# import math
# for T in range(int(input())):
    
#     A,B = map(int,input().split())
    
#     if A >= B + 10:
#         print(0)
        
#     else:
#         left  = B + 10 - A
#         shots = math.ceil(left/3)
#         print(shots)
        

# def f(a, b ):
#     diff = abs(a-b)
#     if diff > 10 :
#         return 0  
    
#     else :
#         cnt = 0 
#         an = a 
#         an += an + 2
#         if an > 
        

#             if i + 2 < 10 + b:
#                 cnt += 1
#             else :
#                 break 
#         return cnt 

# if __name__=="__main__":
#     T = int(input())

#     for _ in range(T):
#         a,b = (map(int, input().split()))

#         print(f(a, b))


def f(a, b):
    if abs(a-b) > 10 :
        return 0 
# else :
    num = a
    cnt = 0 
    tar = b + 10 
    while (num < tar):
        num += 3 
        cnt += 1 
    return cnt 




if __name__=="__main__":
    T = int(input())

    for _ in range(T):
        a,b = (map(int, input().split()))

        print(f(a, b))



