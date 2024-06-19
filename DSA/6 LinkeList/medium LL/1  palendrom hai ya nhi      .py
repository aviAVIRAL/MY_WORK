



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

def functionhai(head):
    if head is None or head.next is None:
        return None
    
    st = []
    temp = head
    while temp: # while temp.next.next  != None:
        st.append(temp.data)
        temp = temp.next

    temp = head 
    while(temp):
        if temp.data != st.pop() : return False 
        temp = temp.next
    return True 

# Example usage
arr = [12, 5, 8, 7]
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])
head.next.next.next = Node(arr[3])

print("Original list:")
print_ll(head)  # Output: 12 5 8 7 

# head = functionhai(head)
# print("List after deleting tail:")
# print_ll(head)  # Output: 12 5 8
print(functionhai(head))

print()
# Example usage
arr = [1,2,2,1]
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])
head.next.next.next = Node(arr[3])

print("Original list:")
print_ll(head)  # Output: 12 5 8 7 

print(functionhai(head))








