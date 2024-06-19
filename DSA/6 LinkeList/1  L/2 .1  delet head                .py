




class Node:
    def __init__(self, data, next_pointer=None):
        self.data = data
        self.next = next_pointer

def print_ll(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

def delete_head(head):
    if head is None:
        return None
    temp = head
    head = head.next
    del temp  # Python's garbage collector will handle the memory cleanup
    return head

if __name__ == "__main__":
    arr = [12, 5, 8, 7]
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])
    
    head = delete_head(head)
    print_ll(head)  # Output: 5 8 7



# rep2  Without Explicit del

class Node:
    def __init__(self, data, next_pointer=None):
        self.data = data
        self.next = next_pointer

def delete_head(head):
    if head is None:
        return None
    head = head.next
    return head

# Testing the function
def print_ll(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

arr = [12, 5, 8, 7]
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])
head.next.next.next = Node(arr[3])

head = delete_head(head)
print_ll(head)  # Output: 5 8 7


