



print()
print()

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

def delete_head(head):
    if head is None or head.next is None:
        return None  # If the list is empty or has only one node, return None

    prev = head
    head = head.next 
    head.back = prev
    prev.next = None
    
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
    head = delete_head(head)
    print_dll(head)

print()

































