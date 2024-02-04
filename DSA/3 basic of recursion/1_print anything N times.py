# printing anything N times by usig recursion :

# print 1,2,3 using global variable :


count = 0  # This is a global variable

def recursion():
    
    global count  # Declare count as a global variable
    
    # Base condition
    if count == 3:
        return
    print(count)

    count += 1
    recursion()

if __name__ == "__main__":
    recursion()


# output 
# 0
# 1
# 2


# print avi 3 times using global variable :

count = 0  # This is a global variable

def recursion():
    
    global count  # Declare count as a global variable
    
    # Base condition
    if count == 3:
        return
    print("avi")

    count += 1
    recursion()

if __name__ == "__main__":
    recursion()

