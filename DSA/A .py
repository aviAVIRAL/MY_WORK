

print()

def f(x) :
    nu = str(x)
    su = sum(int(y) for y in nu )
    if x % su == 0:
        return su 
    else :
        return -1 
print(f(18))

print()


def f(x) :
    nu = str(x)

    if x % sum(map(int, str(x))) == 0:
        return sum(map(int, str(x)))
    return -1









print()


# print()
# x = 123 
# nu = str(x)
# su = (int(y) for y in nu)
# print(su)

# print()

# arr = [1,2]
# ans = sum(arr)
# print(ans)
# print()

# sol = sum([1,2])
# print(sol)


print()
# # test case
# # 5 3
# # 7 3 5 2 1

# def f(arr, target):
#     n = len(arr)
#     for i in range(n):
#         if arr[i] == target:
#             return "yes"
#     return "no"  # Element not found

# if __name__ == "__main__":
#     N, X = map(int, input().split())
#     Arr = list(map(int, input().split()))

#     ans = f(Arr, X)
#     print(ans)
print("................")

ans =sum( list(map(int, [1,2,3] ))  )
print(ans)


ans = [map(int, ["1","2","3"] )]
print(ans)

ans = map(int, ["1","2","3"] )
print(ans)

print(".........")
ans =sum( list(map(int, "123" ))  )
print(ans)

ans =sum( list(map(int,  ["1","2","3"] ))  )
print(ans)
ans =sum( list(map(int, [1,2,3] ))  )
print(ans)

print(".........")
ans = list(map(int, "123" ))
print(ans)

ans = list(map(int,  ["1","2","3"] ))
print(ans)
ans = list(map(int, [1,2,3] ))
print(ans)

print(".........")
ans = list(map(str, [1,2,3]  ))
print(ans)

ans = list(map(int,  ["1","2","3"] ))
print(ans)
ans = str(map(int, [1,2,3] ))
print(ans)

