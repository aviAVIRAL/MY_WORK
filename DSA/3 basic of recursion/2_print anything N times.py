
# print avi avi ...n times  without global variable :


def func(i, n):
    if i > n:
        return
    print(i , end = " ")
    func(i + 1, n)

if __name__ == "__main__":
    n = int(input("Enter a value for n: "))
    func(1, n)

# output 
# 1 , 2 , 3 


# print 1,2,3...n  without global variable :

def func(i, n):
    if i > n:
        return
    print("avi")
    func(i + 1, n)

if __name__ == "__main__":
    n = int(input("Enter a value for n: "))
    func(1, n)

# output 
# avi 
# avi
# avi
