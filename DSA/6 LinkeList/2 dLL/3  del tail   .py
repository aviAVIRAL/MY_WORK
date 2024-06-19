print()
# striver  
class Node:
    def __init__(self, data, next_node=None, back_node=None):
        self.data = data
        self.next = next_node
        self.back = back_node

def convert_arr_to_dll(arr):
    # Create the head node with the first element of the array
    head = Node(arr[0])
    # Initialize 'prev' to the head node
    prev = head

    for i in range(1, len(arr)):
        # Create a new node with data from the array and set its 'back' pointer to the previous node
        temp = Node(arr[i], None, prev)
        # Update the 'next' pointer of the previous node to point to the new node
        prev.next = temp
        # Move 'prev' to the newly created node for the next iteration
        prev = temp

    # Return the head of the doubly linked list
    return head

def print_dll(head):
    while head is not None:
        # Print the data in the current node
        print(head.data, end=" ")
        # Move to the next node
        head = head.next

def delete_tail(head):
    if head is None or head.next is None:
        return None  # If the list is empty or has only one node, return None

    tail = head
    while tail.next is not None:
        # Traverse to the last node (tail)
        tail = tail.next

    new_tail = tail.back
    new_tail.next = None
    tail.back = None

    # Free memory of the deleted node
    del tail

    return head

if __name__ == "__main__":
    arr = [12, 5, 8, 7]
    head = convert_arr_to_dll(arr)

    print("Original dll", end=" ")
    print_dll(head)
    print()
    print("After delet tail ", end=" ")
    head = delete_tail(head)
    print_dll(head)
# ....................................

print()
# ye aapne aap kiy a hai 

class Node:
    def __init__(self, data, next_node=None, back_node=None):
        self.data = data
        self.next = next_node
        self.back = back_node

def convert_arr_to_dll(arr):
    head = Node(arr[0])
    prev = head

    for i in range(1, len(arr)):
        temp = Node(arr[i], None, prev)
        prev.next = temp
        prev = temp
    return head

def delete_tail(head):
    if head is None or head.next is None:
        return None  # If the list is empty or has only one node, return None
    
    temp = head 
    while temp.next.next is not None: 
        temp = temp.next 
    tail = temp.next 
    tail.back = None 
    temp.next = None 
    
    return head


def print_dll(head):
    while head is not None:
        # Print the data in the current node
        print(head.data, end=" ")
        # Move to the next node
        head = head.next


if __name__ == "__main__":
    arr = [12, 5, 8, 7]
    head = convert_arr_to_dll(arr)

    print("Original :", end=" ")
    print_dll(head)
    print(  )   
    print("After del:", end=" ")
    head = delete_tail(head)
    print_dll(head)

print()

































