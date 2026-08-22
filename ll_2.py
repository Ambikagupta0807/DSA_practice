class Listnode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
node1 = Listnode(10)
node2 = Listnode(20)
node3 = Listnode(30)
node1.next = node2
node2.next = node3
head = node1
counter = 0
current = head
while current is not None:
    counter+=1
    current = current.next
print(f"The number of nodes is {counter}")
    