
from datetime import datetime

t = int(input())
for i in range(t):
    s = input()
    d = datetime.strptime(s, "%H:%M")
    print(d.strftime("%I:%M %p"))

    
# from datetime import datetime

# n = int(input())

# for i in range(n):
#     time = input()
#     print(datetime.strptime(time, "%H:%M").strftime("%I:%M %p"))

# for _ in range(int(input())):
#     h, m = map(int, input().split(':'))
#     print(f"{(h-1)%12+1:02d}:{m:02d} {'AP'[h>11]}M")




# integers = [9, 41] map se ho jaye ga 
# strings = [str(num) for num in integers]
# print(strings)  # Output: ["9", "41"]
# ...............................
# def f(a):
#     if a[0] > 12:
#         ans = abs(a[0] - 12)
#         a[0] = ans
#     stri = [str(num) for num in a]
#     stri += "PM"
#     re = ":".join(stri)

#     return re
    
# for _ in range(int(input())):
#     a = list(map(int, input().split(":")))
#     print(f(a))
# ................................
# substrings = ['09', '41']
# result = ":".join(substrings)
# print(result)  # Output: "09:41"



# s = "09:41"
# substrings = s.split(":")
# print(substrings)  # Output: ['09', '41']

