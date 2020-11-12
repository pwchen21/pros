class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

		
class Solution(object):
    def getImportance(self, employees, id):	
        emp=Employee(2,3,1)
        print emp.id()

Sol=Solution()
Sol.getImportance([2,3,2])