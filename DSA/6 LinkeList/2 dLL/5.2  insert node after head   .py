



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


def print_dll(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next


def insert_befor_head_(head, val):
    if head is None or head.next is None:
        return None  # If the list is empty or has only one node, return None
    
    newnode = Node(val , head.next, head)
    head.next.back = newnode
    head.next = newnode  

    return head


if __name__ == "__main__":
    arr = [12, 5, 8, 7]
    head = convert_arr_to_dll(arr)

    print("Original :", end=" ")
    print_dll(head)
    print(  )   
    print("After del:", end=" ")
    head = insert_befor_head_(head, 9)
    print_dll(head)

print()



