database = [['Joe', '100', '52', '81'], ['Lucy', '10' , '85', '21'], ['Jarquavious', '100', '100', '100']]
def search(name):
    for row in database:
        if name in row:
            return row
namesearch = input('What student would you like to view? :')
whatrow = search(namesearch)
term = 0
while term == 0:
    term = int(input('What term would you like to view? :'))
print()
print(whatrow[0], 's grade is:')
print(whatrow[term])
print()
term = 0
temp = input('Would you like to see total results for a term? [Y/N]')
if temp == 'Y' or 'Yes' or 'yes' or 'y':
    while term == 0:
        term = input('What term do you want the total grade for? :')
    rows = database.len
    #FINISH THIS BIT IT DOESNT WORK.
    print(rows)
    print(term)
else:
    print()