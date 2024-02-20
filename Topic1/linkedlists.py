
import time
#define the data, and pointer placeholders for easier coding.
data = 0 
pointer = 1
#define head pointer
head = 0
#create 2D array named linked list.
Linkedisttext = open("linkedlists.txt", "r")
LinkedList = (Linkedisttext.read())
Linkedisttext.close

#define adding data subroutine
def add(information):
    #create a current variable difined by the memory location of the variable data
    current = id(information)
    print ('The Location in memory of "', information, '" is:', current)
    #find where empty location is
    locationofempty = getEmpty()
    print('The memory location where the value will be inserted is: ')
    time.sleep(0.5)
    print('Loading.')
    time.sleep(1)
    print(locationofempty)
    #assign the data at the location to the name
    LinkedList[locationofempty][data] = information
    time.sleep(0.5)
    Linkedisttext = open("linkedlists.txt", "w")
    Linkedisttext.write(LinkedList)
    Linkedisttext.close
    print(LinkedList)

#define subroutine finding where an empty space in the array is
def getEmpty():
    for i in range(0, len(LinkedList)):
        if LinkedList[i][data] == "":
            return i

def delete(information):
    for i in range(0, len(LinkedList)):
        if LinkedList[i][data] == information:
            p = i-1
            LinkedList[p][pointer] = LinkedList[i][pointer]
            deletedname = LinkedList[i][data]
            LinkedList[i][data] = ""
            print(LinkedList)
            print(deletedname, 'has oficially been removed from the array. ')

            
print('Would you like to:')
print('A, add a new variable')
print('B, delete an existing variable')
print('C, display the list on screen')
command = input('Please answer in A,B or C: ')
if command == 'A':
    name = input('What name would you like to insert: ')
    add(name)
if command == 'B':
    name = input('What name would you like to delete?')
    delete(name)
if command == 'C':
    print(LinkedList)

    #FIX UP THE CODE ///////////////// LINKEDLISTS.TXT NEEDS TO BE ARRAY FOR IT TO WORK 