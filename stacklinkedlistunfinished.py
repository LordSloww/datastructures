class newNode():
    def __init__(self, data):
        self.data = data
        self.previous = None
class stack():
    def __init__(self):
        #define top pointer
        self.top = None
    def push(self, data):
        #create node
        node = newNode(data)
        #set node pointer to top
        node.previous = self.top
        #set top to node
        self.top = node
    def pop(self):
        if self.top == None:
            print('Nothing to remove ')
        else:
            print(self.top.data, 'has been removed ')
            temp = self.top.data
            self.top = self.top.previous
            return temp
