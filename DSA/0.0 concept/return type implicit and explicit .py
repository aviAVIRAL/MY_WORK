
# implicit and explict return types 

print()

def function_(arr):
    for i in range(len(arr)):
        arr[i] += 1
    # No return statement

arr = [1, 2, 3]
function_(arr)
print(arr)  # Output: [2, 3, 4]

print()

def function_(arr):
    for i in range(len(arr)):
        arr[i] += 1
        return None 
    # No return statement

arr = [1, 2, 3]
function_(arr)
print(arr)  # Output: [2, 3, 4]

print()

def function_(arr):
    for i in range(len(arr)):
        arr[i] += 1
        return 
    # No return statement

arr = [1, 2, 3]
function_(arr)
print(arr)  # Output: [2, 3, 4]

print()
print()  #
def function_(arr):
    for i in range(len(arr)):
        arr[i] += 1
    # No return statement

arr = [1, 2, 3]
x = function_(arr)  #
print(x)  # error deg aop : None 
print()



print(" ................")
print(" ................")

def function_(arr):
    for i in range(len(arr)):
        arr[i] += 1
        return arr 
    # No return statement

arr = [1, 2, 3]
function_(arr)
print(arr)  # Output: [2, 3, 4]


def function_(arr):
    for i in range(len(arr)):
        arr[i] += 1
        return arr 
    # No return statement

arr = [1, 2, 3]
x = function_(arr)
print( x )  # Output: [2, 3, 4]







