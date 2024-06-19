
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
        # Print the data in the current node
        print(head.data, end=" ")
        # Move to the next node
        head = head.next
    print()


def reverse_dll(head):
    # If head is empty or there is only
    # one element, return the head directly
    if head is None or head.next is None:
        return head

    # Initialize a stack to store values
    st = []
    # Initialize the node pointer
    #'temp' at head
    temp = head

    # Traverse the doubly linked list
    # via the 'temp' pointer
    while temp is not None:
        # Insert the data of the current
        # node into the stack
        st.append(temp.data)
        # Traverse further
        temp = temp.next

    # Reinitialize 'temp' to head
    temp = head

    # Second iteration of the DLL
    # to replace the values
    while temp is not None:
        # Replace the value pointed to
        # by 'temp' with the value from
        # the top of the stack and pop it
        temp.data = st.pop()
        # Traverse further
        temp = temp.next

    # Return the updated doubly linked list
    # where the values of nodes from both
    # ends have been swapped
    return head


# Example usage:
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


