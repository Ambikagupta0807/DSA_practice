class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next=next
        
head = None
n = int(input("Enter the number of node: "))
for i in range(n):
    val = int(input(f"Enter value of {i+1} node: "))
    nextnode = ListNode(val)
    if head is None:
        head = nextnode
    else:
        current = head 
        while current.next is not None:
            current = current.next
        current.next=nextnode
        
print("Linked list: ")
current = head
while current is not None:
    print(current.val, end = "->")
    current = current.next
print("None")

end_val = int(input("Enter the last value to add: "))
endnode = ListNode(end_val)

if head is None:
    head = endnode
else:
    current = head
    while current.next is not None:
        current = current.next
    current.next = endnode
    
print("\nAfetr adding in the end: ")
current = head
while current is not None:
    print(current.val, end = "->")
    current = current.next
print("None")
            