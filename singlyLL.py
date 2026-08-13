class Node:
    def __init__(self, info, next = None):
        self.data = info
        self.next = next
        
class singlylinkedlist:
    def __init__(self, head = None):
        self.head = head
        
    def insertAtEnd(self,value):
        temp = Node(value)
        if(self.head!= None):
            t1=self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp
    
    def insertAtBeg(self, value):
         temp = Node(value)
         temp.next = self.head
         self.head = temp  
         
    def insertAtMid(self, value, x):
        temp = Node(value)
        t1=self.head
        
        while(t1.next!= None):
            if(t1.data==x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next         
            
    #deleting a node
    def deleteLL(self, value):
        t1 = self.head

        if t1 == None:
         return

        if t1.data == value:
            self.head = t1.next
        return

        prev = t1
        t1 = t1.next

        while(t1 != None):
            if(t1.data == value):
                prev.next = t1.next
            return
        else:
            prev = t1
            t1 = t1.next


    def printLL(self):
        t1 = self.head

        if t1 == None:
            print("Linked List is empty")
        return

        while(t1 != None):
            print(t1.data)
            t1 = t1.next
        
        
                            
        
obj = singlylinkedlist()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeg(50)
obj.insertAtMid(40,20)
obj.deleteLL(10)
obj.printLL()
    
            
                
           
            