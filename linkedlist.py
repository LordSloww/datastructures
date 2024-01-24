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
    
    def delete(myList, data):
        #start at the head of the list
        current = myList.head
        #check if node is to be deleted
        if current.data == data:
            #update the head pointer
            myList.head = current.next
        else:
            #repeat untill the node has been found
            while current.next.data != data:
                #change the current node to be the next node
                current = current.next

            #set the pointer to be the next nodes pointer
                current.next = current.next.next
                      

    def traverse(self):        
        #set the current node as the head
        current = self.head

        #repeat until there are no more linked nodes
        while current is not None:
            print(current.get_data())
            current = current.get_next()

#instantiate an emptu linked list object
myList = LinkedList()