class listnode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head = None
n = int(input("Enter the number of node: "))
for i in range (n):
    val = int(input(f"Enter value for {i+1} node: "))
    nextnode = listnode(val)
    if head is None:
        head = nextnode
    else:
        current = head
        while current.next is not None:
            current = current.next
        current.next = nextnode
print("Linked list: ")
current = head
while current is not None:
    print(current.val, end = "->")
    current = current.next
print("None")
    
num = int(input("Enter the value to be deleted: "))
current = head
prev = None
while current is not None:
    if current.val == num:
        if prev is None:
            head = current.next
        else:
            prev.next = current.next
        print("node deleted")
        print("Linked list after deletion of node: ")
        current = head
        while current is not None:
            print(current.val, end = "->")
            current = current.next
        break
    prev = current
    current = current.next
else:
    print("No such node in the list")
    
            
print("\nLinked list after deletion of node: ")
current = head
while current is not None:
    print(current.val, end = "->")
    current = current.next

