class Node():
    def __init__(self, givenData):
        #constructor method
        self.data = givenData
        self.next = None
        
    #getter method
    def get_data(self):
        return self.data
    #getnect method
    def get_next(self):
        return self.next
    #setter method
    def set_next (self, newNext):
        self.next = newNext

class LinkedList():
    def __init__(self):
        #constructor method
        self.head = None

    def add(self, data):
        #create a new node
        newNode = Node(data)
        #check if the head node exists
        if self.head is None:
            self.head = newNode
        else:
            #update the pointers so the new node is the head
            newNode.set_next(self.head)
            self.head = newNode

    def traverse(self):        
        #set the current node as the head
        current = self.head

        #repeat until there are no more linked nodes
        while current is not None:
            print(current.get_data())
            current = current.get_next()

#instantiate an emptu linked list object
myList = LinkedList()