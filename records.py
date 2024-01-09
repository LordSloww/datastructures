class recordType():
    def __init__(self,theID , theLastName, theFirstName, theDept):
        self.id = theID
        self.lastName = theLastName
        self.firstName = theFirstName
        self.dept = theDept

# record = record(ID, lastName, firstName, dept)
# How you would do it but puthon doesnt allow you to do it like this ^
record1 = recordType(2468, 'Jones', 'John', 243)

print(record1.lastName)
record2 = recordType(1231, 'Stevens', 'Not a legend', 2313)
print(record2.lastName)

#people = (
#    recordType(2468, 'Jones', 'John', 243)
#    recordType(1231, 'Stevens', 'Not a legend', 2313)
#)