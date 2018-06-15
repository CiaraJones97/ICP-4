class Employee:
    """Employee class"""
    total = 0 # public total count member

    def __init__(self,n,f,s,d):
        self.name = n
        self.family = f
        self.salary = s
        self.department = d
        Employee.total = Employee.total + 1

    def average_salary(self): # calculate the average salary
        average = self.salary/12
        return average



class Fulltime(Employee) :
    """Derived class for Employee"""
    full_time = True


# Add an employee then increment the count
E2 = Fulltime("melkam","Getachew", 120000,"software")
E1 = Employee('abc', "getcheq", 140000,'soft')

# Print the count and information of the employees
print("Number of Employees:", Employee.total)
print(E2.name)
print(E2.average_salary())
print(E2.family)

print(E1.name)
print(E1.average_salary())
