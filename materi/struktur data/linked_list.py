class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def popLeft(self):
        if self.head is None:
            return
        self.head = self.head.next
    
    def showList(self):
        current_node = self.head   
        while current_node is not None:
          print(current_node.data, end=" ")
          current_node = current_node.next
    

ls = LinkedList()
for x in range(10):
    ls.push(x+1)

ls.showList()