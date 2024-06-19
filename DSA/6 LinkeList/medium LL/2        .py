

if __name__ == '__main__':
    head = None
    head = insertNode(head, 1)
    head = insertNode(head, 3)
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 4)
    head1 = head
    head = head.next.next.next
    headSec = None
    headSec = insertNode(headSec, 3)
    head2 = headSec
    headSec.next = head




#     head1: 1 -> 3 -> 1 -> 2 -> 4
#                      ^
#                      |
# head2: 3 -------------



# head1: 1 -> 3 -> 1 --
#                        -> 2 -> 4
#                           ^
#                           |
# head2: 3 -----------------

