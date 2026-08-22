class Listnode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
node1 = Listnode(1)
node2 = Listnode(2)
node3 = Listnode(3)
node4 = Listnode(4)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1
current = head
while current is not None:
    print(current.val)
    current = current.next
