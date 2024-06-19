print()
print()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertNode(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    last = head
    while last.next:
        last = last.next
    last.next = new_node
    return head
# ...........................................
def f(head1, head2):
    mp = {}
    temp = head1

    while temp:
        mp[temp] = 1
        temp = temp.next

    temp = head2
    while temp:
        if temp in mp:
            return temp  # Returning the node itself
        temp = temp.next
    return None

def printList(head):
    while head and head.next:
        print(head.data, end='->')
        head = head.next
    if head:
        print(head.data)

if __name__ == '__main__':
    head = None
    head = insertNode(head, 1)
    head = insertNode(head, 3)
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 4)
    head1 = head
    
    # Move head to point to the 2nd node
    head = head.next.next.next

    headSec = None
    headSec = insertNode(headSec, 3)
    head2 = headSec
    headSec.next = head  # Create intersection

    print('List1: ', end='')
    printList(head1)
    print('List2: ', end='')
    printList(head2)
    
    answerNode = f(head1, head2)
    if answerNode is None:
        print('No intersection')
    else:
        print('The intersection point is', answerNode.data)


print()
print()