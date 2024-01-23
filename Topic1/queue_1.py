#define the queue
queue = ['', '', '', '', '']
#difine the front rear and size :D
front = 0
rear = -1
size = 0
#create enqueue supprogram too ad student names to the queue
def enQueue(studentName):
    #check if you can put any more names in the queue
    if queue.isFull():
        print("The list is full.")
    else:
        #increase size and rear pointer by one and append name to the queue
        size = size + 1
        rear = rear + 1
        queue.append[rear] = studentName
#create dequeue subprogram to take students out of the queue
def deQueue(queue):

    if queue.isEmpty():
        print("The list is empty.")
    else:
        #return the value of front and increase the front pointer by 1
        return(queue[front])
        front = front + 1
#create subprogram to check if the queue is full or not 
def isFull(queue):
    #check if the size is the max length of the queue
    if size == 5:
        return True
    else:
        return False
#create subprogram to check if the queue is empty or not
def isEmpty(queue):
    #check if the size is the max length of the queue or not
    if size == 5:
        return False
    else:
        return True