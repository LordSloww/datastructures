queue = ['', '', '', '', '']

front = 0
rear = -1
size = 0

def enQueue(studentName):
    if queue.isFull():
        print("The list is full.")
    else:
        size = size + 1
        rear = rear + 1
        queue.append[rear] = studentName

def deQueue(queue):
    if queue.isEmpty():
        print("The list is empty.")
    else:
        return()

def isFull(queue):
    if size == 5:
        return True
    else:
        return False

def isEmpty(queue):
    if size == 5:
        return False
    else:
        return True