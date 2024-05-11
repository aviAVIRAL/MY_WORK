# print()



# def f(arr):
#     n = len(arr)
#     j = -1
#     i = 0

#     while i < n:
#         if arr[i] == 0:
#             j = i
#             break
#         i += 1

#     i = j + 1
#     while i < n:
#         if arr[i] != 0:
#             arr[j], arr[i] = arr[i], arr[j]
#             i += 1
#             j += 1
#         else:             #  imp* : else 
#             i += 1

#     return arr





# # if __name__=="__main__":
# #     arr = [1,2,0,4,0,0,5,0]
# #     print(f(arr))

# # print()

# # if __name__=="__main__":
# #     arr = [1,2,0,4,0,0,5,0]
# #     k = f(arr)
# #     for x in k :
# #         print(x, end= " ")

# # print()
# # if __name__=="__main__":
# #     arr = [1,2,0,4,0,0,5,0]
# #     print(*f(arr))



# # print("......")

# # a = [[1,2,3],[4,5,6],[6,7,7]]
# # print(*a)


# # a = [1,2,3]
# # print(*a)


# def f(arr):
#     n = len(arr)
#     j = -1
#     i = 0

#     while i < n:
#         if arr[i] == 0:
#             j = i
#             break
#         i += 1

#     i = j + 1
#     while i < n:
#         if arr[i] != 0:
#             arr[j], arr[i] = arr[i], arr[j]
#             i += 1
#             j += 1
#         else:             #  imp* : else 
#             i += 1

#     return arr



# for _ in range(int(input())):
#     n, k = map(int,input().split())
#     arr = list(map(int,input().split()))


for _ in range(int(input())):
    # n = map(int, input().split())
    n = int(input())
    arr = list(map(int, input().split()))
 

    n = len(arr) # imp to define len gth 
    j = -1
    i = 0

    while i < n:
        if arr[i] == 0:
            j = i
            break
        i += 1

    i = j + 1
    while i < n:
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
            j += 1
        else:             #  imp* : else 
            i += 1

    # print(*arr) 
    k = arr
    for x in k: 
        print(x, end = " ")


    

# 2
# 5
# 5 0 3 2 0
# 4
# 0 0 2 1

