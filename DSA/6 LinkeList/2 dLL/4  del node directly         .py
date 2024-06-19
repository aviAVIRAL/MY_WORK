# # inmplicit and explicit retun tuypr s sss 



# print()

# def function_(arr):
#     for i in range(len(arr)):
#         arr[i] += 1
#     # No return statement

# arr = [1, 2, 3]
# function_(arr)
# print(arr)  # Output: [2, 3, 4]

# print()

# def function_(arr):
#     for i in range(len(arr)):
#         arr[i] += 1
#         return None 
#     # No return statement

# arr = [1, 2, 3]
# function_(arr)
# print(arr)  # Output: [2, 3, 4]

# print()

# def function_(arr):
#     for i in range(len(arr)):
#         arr[i] += 1
#         return 
#     # No return statement

# arr = [1, 2, 3]
# function_(arr)
# print(arr)  # Output: [2, 3, 4]

# print()
# print()  #
# def function_(arr):
#     for i in range(len(arr)):
#         arr[i] += 1
#     # No return statement

# arr = [1, 2, 3]
# x = function_(arr)  #
# print(x)  # error deg aop : None 
# print()



# print(" ................")
# print(" ................")

# def function_(arr):
#     for i in range(len(arr)):
#         arr[i] += 1
#         return arr 
#     # No return statement

# arr = [1, 2, 3]
# function_(arr)
# print(arr)  # Output: [2, 3, 4]


# def function_(arr):
#     for i in range(len(arr)):
#         arr[i] += 1
#         return arr 
#     # No return statement

# arr = [1, 2, 3]
# x = function_(arr)
# print( x )  # Output: [2, 3, 4]

# ...............................................

print()
print()



print()

class Node:
    def __init__(self, data, next_node=None, back_node=None):
        self.data = data
        self.next = next_node
        self.back = back_node

def convert_arr_to_dll(arr):
    if not arr:
        return None

    head = Node(arr[0])
    prev = head

    for i in range(1, len(arr)):
        temp = Node(arr[i], None, prev)
        prev.next = temp
        prev = temp

    return head


# .............................

def del_node(temp):

    prev = temp.back
    front = temp.next


    if front is None:
        prev.next = None
        temp.back = None
        return

    prev.next = front
    front.back = prev
    temp.next = None
    temp.back = None
# ............
def print_dll(head):
    while head is not None:
        print(head.data, end=" -> " if head.next else "")
        head = head.next
    print()

if __name__ == "__main__":
    arr = [12, 5, 8, 7,2 ]
    head = convert_arr_to_dll(arr)

    print("Origi  ", end=" ")
    print_dll(head)

    # Deleting a middle node
    print("After  ", end=" ")
    del_node(head.next.next)
    print_dll(head)


print()



