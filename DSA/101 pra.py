

def f(a, k):
    n = len(a)
    t = []
    for i in range(n-k, n):
        t.append(a[i])

    for i in range(n-k):
        t.append(a[i])
    return t
if __name__=="__main__":
    a = [1,2,3,4,10,20]
    s = f(a, 2)
    for x in s:
        print(x, end=" ")
    print()


print()


def f(a):
    n = len(a)
    # t = []
    s = 0 
    for i in range(1,n):
        s = max(s, abs(a[i] - a[i-1]))
    return s
if __name__=="__main__":
    a = [1,2,3,4,23, 999]
    # s = f(a)
    # for x in s:
    #     print(x, end=" ")
    # print()
    print(f(a))

print()



# or example:
# Suppose n1=11 and n2=15.
# There is the number 11, which has repeated digits, but 12, 13, 14 and 15 have no repeated digits. So, the output is 4.
# Case 1:
# Input:
# 11 — Vlaue of n1
# 15 — value of n2












