class Employee:
    def __init__(self, firstName, lastName, dob, hours, hourlyRate):
        self.firstName = firstName
        self.lastName = lastName
        self.dob = dob
        self.hours = hours
        self.hourlyRate = hourlyRate

    def salary(self):
        return self.hours * self.hourlyRate

class Manager(Employee):
    def __init__(self, firstName, lastName, dob, hours, hourlyRate, bonus):
        Employee.__init__(self, firstName, lastName, dob, hours, hourlyRate)
        self.bonus = bonus

    def salary(self):
        return self.hours * self.hourlyRate + self.bonus

employeeList = []
employeeList.append(Employee("Sam","Pham","20171012", 23,34))
employeeList.append(Manager("Sam","Pham","20171012", 23,34,2000))
total = 0
for x in employeeList:
    total += x.salary()
print(total)