import time
#define list1
list1 = [9,6,2,54,7,765,32,6,865,342,634,543,76,234,654,345,754,435,234,654,2,432,4,6,5,43,432,54,23,1]
print('This is list 1:')
print(list1)
#define list2
list2 = [321,543,6,4,32,4,7,4,43,2,43,543,543,324,534,543,54345,354,75]
print('This is list 2:')
print(list2)
#bubble sorting algorithm
def bubbleSort(list):
    #find the length of the list
    n = len(list)
    swapped = False
    #sort through every value furthest right to left
    for i in range(n-1):

        for j in range(0, n-i-1):
            if list[j] > list[j + 1]:
                #if something can be sorted it will be sorted
                swapped = True
                print(list)
                time.sleep(0.001)
                list[j], list[j + 1] = list[j + 1], list[j]
        if not swapped:
            #returns a value when no sorts can be done 
            return
mergelist = list1 + list2
#make mergelist a combination of both lists
print('This is list one with list two on the end:')
print(mergelist)
#mergelist.sort()
#call the sorting algorithm
bubbleSort(mergelist)
print('This is the whole list sorted.')
#print the merged and sorted list
print(mergelist)