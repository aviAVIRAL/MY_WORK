



class Node:
    def __init__(self, data, next_pointer=None):
        self.data = data
        self.next = next_pointer

def delete_tail(head):
    if head is None or head.next is None:
        return None
    temp = head
    while temp.next.next: # while temp.next.next  != None:
        temp = temp.next
    temp.next = None
    return head

def print_ll(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Example usage
arr = [12, 5, 8, 7]
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])
head.next.next.next = Node(arr[3])

print("Original list:")
print_ll(head)  # Output: 12 5 8 7 

head = delete_tail(head)
print("List after deleting tail:")
print_ll(head)  # Output: 12 5 8











