class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head = None
n = int(input("Enter the no.of nodes: "))
for i in range(n):
    val = int(input(f"enter value of {i+1} node: "))
    nextnode=ListNode(val)
    if head is None:
        head = nextnode
    else:
        current = head
        while current.next is not None:
            current=current.next
        current.next = nextnode
print("Linked list is: ")
current = head
while current is not None:
    print(current.val, end = " -> ")
    current = current.next
print("None")

new_val = int(input("\nEnter new node's value: "))
newnode = ListNode(new_val)

newnode.next = head
head = newnode

print("\nAfter inserting: ")
current = head
while current is not None:
    print(current.val)
    current = current.next 
print("None")