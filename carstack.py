cars = [['', None], ['','0'], ['','1'], ['','2'], ['','3'], ['','4']]
top = -1
data = 0
pointer = 1
def push(item):
    global top
    top = top + 1
    cars[top][data] = item
    print(cars)

def pop():
    cars.pop()
    print(cars)
def isFull():
    if len(cars) == 6:
        return True
    else:
        return False
def isEmpty():
    if len(cars) == 0:
        return True
    else:
        return False
def size():
    return len(cars)
def peek():
    temp = len(cars)
    return cars[temp]

itemToPush = input('what would you like to add to the list? ')
push(itemToPush)