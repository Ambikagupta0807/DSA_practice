class Listnode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
node1 = Listnode(10)
node2 = Listnode(20)
node3 = Listnode(30)
node4 = Listnode(40)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1
current = head

num = int(input("Enter the number to search"))
found = False
while current is not None:
    if current.val == num:
        found = True
        break
    current = current.next
    
print(found)