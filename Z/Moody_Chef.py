


# def f(arr,n,l,r):
#     mincnt = 0 
#     maxcnt = 0 
#     for x in arr:
#         if l<=x and  x <= r:
#             maxcnt += 1
#         else :
#             mincnt -= 1
    
#     maxcnt = maxcnt -abs(mincnt) 
#     # return maxcnt, mincnt    (2, -1)
#     output = f"{maxcnt} {mincnt}"
#     return output


# if __name__=="__main__":
#     for x in range(int(input())):    
#         n, l , r = map(int, input().split())
#         arr = list(map(int, input().split()))

#         ans = f(arr, n , l , r)

#         print (ans)




def f(arr, n, l, r):
    mincnt = 0 
    maxcnt = 0 
    for x in arr:
        if l <= x <= r:
            maxcnt += 1
        else:
            mincnt -= 1
    
    maxcnt -= abs(mincnt)  # Adjust maxcnt
    
    return maxcnt, mincnt  # Return a tuple

if __name__ == "__main__":
    for _ in range(int(input())):    
        n, l, r = map(int, input().split())
        arr = list(map(int, input().split()))

        # ans = f(arr, n, l, r)

        # Print the output tuple
        print(*f(arr, n, l, r))  # Unpack the tuple for printing
















# def f(arr,n,l,r):
#     mincnt = 0 
#     maxcnt = 0 
#     for x in arr:
#         if l<=x and  x <= r:
#             maxcnt += 1
#         else :
#             mincnt -= 1
    
#     maxcnt = maxcnt -abs(mincnt) 
#     return maxcnt, mincnt    (2, -1)


# if __name__=="__main__":
#     for x in range(int(input())):    
#         n, l , r = map(int, input().split())
#         arr = list(map(int, input().split()))

#         ans = f(arr, n , l , r)

#         print (ans)


