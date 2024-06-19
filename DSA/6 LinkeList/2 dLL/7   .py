
# class Node:
#     def __init__(self, data, next_node=None, back_node=None):
#         # Data stored in the node
#         self.data = data
#         # Reference to the next node
#         # in the list (forward direction)
#         self.next = next_node
#         # Reference to the previous node
#         # in the list (backward direction)
#         self.back = back_node

# def convert_arr_to_dll(arr):
#     # Create the head node with
#     # the first element of the array
#     head = Node(arr[0])
#     # Initialize 'prev' to the head node
#     prev = head

#     for i in range(1, len(arr)):
#         # Create a new node with data from the
#         # array and set its 'back' pointer
#         # to the previous node
#         temp = Node(arr[i], None, prev)
        
#         # Update the 'next' pointer of the
#         # previous node to point to the new node
#         prev.next = temp
#         # Move 'prev' to the newly created 
#         # node for the next iteration
#         prev = temp

#     # Return the head of the doubly linked list
#     return head

# def print_dll(head):
#     while head is not None:
#         print(head.data, end=" ")
#         # Move to the next node
#         head = head.next
#     print()


# def reverse_dll(head):
#     if head is None or head.next is None:
#         return head

#     curr = head 
#     while curr is not None:
#         last = curr.back
#         front = curr.next

#         curr.next = last 
#         curr.back = front

#         curr = curr.back         

#     return curr 


# arr = [12, 5, 6, 8, 4]
# # Convert the array to a
# # doubly linked list
# head = convert_arr_to_dll(arr)
# # Print the doubly linked list
# print('Doubly Linked List Initially:  ')
# print_dll(head)

# print('Doubly Linked List After Reversing :')

# # Reverse the doubly linked list
# head = reverse_dll(head)
# # Print the reversed doubly linked list
# print_dll(head)


class Node:
    def __init__(self, data, next_node=None, back_node=None):
        # Data stored in the node
        self.data = data
        # Reference to the next node
        # in the list (forward direction)
        self.next = next_node
        # Reference to the previous node
        # in the list (backward direction)
        self.back = back_node

def convert_arr_to_dll(arr):
    # Create the head node with
    # the first element of the array
    head = Node(arr[0])
    # Initialize 'prev' to the head node
    prev = head

    for i in range(1, len(arr)):
        # Create a new node with data from the
        # array and set its 'back' pointer
        # to the previous node
        temp = Node(arr[i], None, prev)
        
        # Update the 'next' pointer of the
        # previous node to point to the new node
        prev.next = temp
        # Move 'prev' to the newly created 
        # node for the next iteration
        prev = temp

    # Return the head of the doubly linked list
    return head

def print_dll(head):
    while head is not None:
        print(head.data, end=" ")
        # Move to the next node
        head = head.next
    print()


#     curr = head 
#     while curr is not None:
#         last = curr.back
#         front = curr.next
#         curr.next = last 
#         curr.back = front
#         curr = curr.back         
#     return curr 
def reverse_dll(head):
    if head is None or head.next is None:
        return head
    curr = head 
    while curr is not None:
        last = curr.back
        front = curr.next

        curr.next = last 
        curr.back = front

        # Move to the next node (previously back)
        curr = curr.back         

    # After the loop, curr will be None,
    # so we need to return the new head,
    # which is the last node we processed.
    # 'last' was the previous node, so it
    # will be the new head.
    return last.back 

arr = [12, 5, 6, 8, 4]
# Convert the array to a
# doubly linked list
head = convert_arr_to_dll(arr)
# Print the doubly linked list
print('Doubly Linked List Initially:  ')
print_dll(head)

print('Doubly Linked List After Reversing :')
# Reverse the doubly linked list
head = reverse_dll(head)
# Print the reversed doubly linked list
print_dll(head)
