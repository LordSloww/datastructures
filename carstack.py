cars = [['', None], ['','0'], ['','1'], ['','2'], ['','3'], ['', 4]]
top = -1
data = 0
size = 0
pointer = 1
def push(item):
    global top
    global size
    top = top + 1
    size = size + 1
    cars[top][data] = item
    print(cars)
def pop():
    global top
    global size
    currentNodeData = cars[top][data]
    top = top - 1
    size = size - 1
    print(cars)
    return currentNodeData
def isFull():
    if cars[top][pointer] == 4:
        return True
    else:
        return False
def isEmpty():
    if top == -1:
        return True
    else:
        return False
def howBig():
    return size
def peek():
    return cars[top][data]

itemToPush = input('what would you like to add to the list? ')
push(itemToPush)