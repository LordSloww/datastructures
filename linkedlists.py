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
        print(LinkedList)
    else:
        break
#define adding data subroutine
def add(information):
    #create a current variable difined by the memory location of the variable data
    current = id(information)
    print ('The Location in memory of "', information, '" is:', current)
    getEmpty()
         
    #USE GET EMPTY TO PLACE CURRENT AND INFORMATION INTO LINKED LIST :) IMPORTANT /////////////////////////////////////////////////////////////////////

def getEmpty():
    for i in range(0, len(LinkedList)):
        if LinkedList[1][pointer] == None:
            return i

            
add('Sasha')