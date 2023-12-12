check = True
while check == True:
    database = ['Joe', '100', '52', '81'], ['Lucy', '10' , '85', '21'], ['Jarquavious', '100', '100', '100']
    def search(name):
        for row in database:
            if name in row:
                return True
        return False
    namesearch = input('What student would you like to view? :')
    tempvariable = search(namesearch)
    if tempvariable == False:
        print('The name was not on the database please try again: ')
        print()
    if tempvariable == True:
        term = int(input('What term would you like to view? :'))
        print()
        print(database[term])