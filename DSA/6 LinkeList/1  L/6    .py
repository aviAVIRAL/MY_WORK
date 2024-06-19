print()

class Node:
    def __init__(self, data, NexT_node=None):
        self.data = data
        self.next = NexT_node

def convert_arr_to_ll(arr):
    head = Node(arr[0])
    mover = head
    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp
    return head

if __name__ == "__main__":
    arr = [12, 44, 5]
    head = convert_arr_to_ll(arr)
    print(head.data)

print()


class Node:
    def __init__(self, data, NexT_node=None):
        self.data = data
        self.next = NexT_node

def convert_arr_to_ll(arr):
    head = Node(arr[0])
    mover = head
    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        # mover = temp
        mover = mover.next 
         
    return head

if __name__ == "__main__":
    arr = [12, 44, 5]
    head = convert_arr_to_ll(arr)
    print(head.data)



