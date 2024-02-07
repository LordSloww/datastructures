import time
#define the data, and pointer placeholders for easier coding.
data = 0 
pointer = 1
#define head pointer
head = 0
#create 2D array named linked list.
LinkedList = [["Bob" , 1] , ["Sarah" , 2 ] , ["Sharon" ,3 ] , ["" , None ] , ["" , None ] , ["" , None ]] 
for i in range (0,5):
    if LinkedList[i][data] != "":
        LinkedList[i][pointer] = id(LinkedList[i + 1][data])
    else:
        print(LinkedList)
        break
#define adding data subroutine
def add(information):
    #create a current variable difined by the memory location of the variable data
    current = id(information)
    print ('The Location in memory of "', information, '" is:', current)
    locationofempty = id(getEmpty())
    print('The memory location where the value will be inserted is: ')
    time.sleep(1)
    print('Loading.')
    time.sleep(0.5)
    print('Loading..')
    time.sleep(0.5)
    print('Loading...')
    time.sleep(0.5)
    print(locationofempty)
    linkedlist[]

def getEmpty():
    for i in range(0, len(LinkedList)):
        if LinkedList[1][pointer] == None:
            temporary = i - 1
            return temporary

            
print('Would you like to:')
print('A, add a new variable')
print('B, delete an existing variable')
print('C, display the list on screen')
command = input('Please answer in A,B or C: ')
if command == 'A':
    name = input('What ')