# File: employee.py
# Description: This program takes in two phrases, encrypts the first, and decrypts the second
# remaining line numbers
# Student Name: Kirsten Richards
# Student UT EID: KJR2599
# Partner Name: Steven Campbell
# Partner UT EID: SWC776
# Course Name: CS 313E
# Unique Number: 52520
# Date Created: September 17, 2022
# Date Last Modified: September 19, 2022

import sys
class Employee:
    # establishing arguments for variables of name, id, and salary to be used throughout 
    def __init__(self, **kwargs):
        self.name = kwargs['name'] #access args index like array does
        self.id = kwargs['id']
        self.salary = kwargs['salary']

    def __str__(self):
        return 'Employee' + "\n" + str(self.name) + ',' + str(self.id) + ',' + str(self.salary)

############################################################
############################################################
############################################################
class Permanent_Employee(Employee):

    def __init__(self, **kwargs):
        self.name = kwargs['name'] #access args index like array does
        self.id = kwargs['id']
        self.salary = kwargs['salary']
        self.benefits = kwargs['benefits']

# calculating various salaries of different permanent employee levels 
    def cal_salary(self):
        if self.benefits == ['health_insurance']:
            return self.salary * 0.9
        if self.benefits == ['retirement']:
            return self.salary * 0.8
        if self.benefits == ['retirement', 'health_insurance']:
            return self.salary * 0.7 


    def __str__(self):
        return ('Permanent Employee' + "\n" + str(self.name) + ',' + str(self.id) + ',' 
        + str(self.salary) + ',' + str(self.benefits))
        

############################################################
############################################################
############################################################


class Manager(Employee):

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.id = kwargs['id']
        self.salary = kwargs['salary']
        self.bonus = kwargs['bonus']
# manager salary is permanent employee salary + manager bonus 
    def cal_salary(self):
        return float(self.salary + self.bonus)
    def __str__(self):
        return ('Manager' + "\n" + str(self.name) + ',' + str(self.id) + ',' 
        + str(self.salary) + ',' + str(self.bonus))



############################################################
############################################################
############################################################


class Temporary_Employee(Employee):

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.id = kwargs['id']
        self.salary = kwargs['salary']
        self.hours = kwargs['hours']
# temporary employee is salary type * hours 
    def cal_salary(self): 
        return float(self.salary * self.hours)

    def __str__(self):
        return ('Temporary Employee' + "\n" + str(self.name) + ',' + str(self.id) + ',' 
        + str(self.salary) + ',' + str(self.hours))


############################################################
############################################################
############################################################


class Consultant(Temporary_Employee):
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.id = kwargs['id']
        self.salary = kwargs['salary']
        self.hours = kwargs['hours']
        self.travel = kwargs['travel']
# special salary * regular employee salary
    def cal_salary(self):
        return float((self.salary * self.hours) + (self.travel * 1000))

    def __str__(self):
        return ('Consultant' + "\n" + str(self.name) + ',' + str(self.id) + ',' 
        + str(self.salary) + ',' + str(self.hours) + ',' + str(self.travel))


############################################################
############################################################
############################################################


class Consultant_Manager(Consultant, Manager):

    def __init__(self,  **kwargs):
        self.name = kwargs['name']
        self.id = kwargs['id']
        self.salary = kwargs['salary']
        self.hours = kwargs['hours']
        self.travel = kwargs['travel']
        self.bonus = kwargs['bonus']
# highest salary calculation of hourly manager salary + travel salary + 2 bonuses 
    def cal_salary(self):
        return float((self.salary * self.hours) + (self.travel * 1000) + self.bonus)

    def __str__(self):
        return ('Consultant Manager' + "\n" + str(self.name) + ',' + str(self.id) + ',' 
        + str(self.salary) + ',' + str(self.hours) + ',' + str(self.travel)+ ',' + str(self.bonus))


############################################################
############################################################
############################################################
###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():
    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")
    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, 
    benefits=["health_insurance"])
    print(emma, "\n")
    sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
    print(sam, "\n")
    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")
    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")
    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, 
    travel=4, bonus=10000)
    print(matt, "\n")
    ###################################
    print("Check Salaries")
    print("Emma's salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]
    print("Emma's salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]
    print("Emma's salary is:", emma.cal_salary(), "\n")
    print("Sam's salary is:", sam.cal_salary(), "\n")
    print("John's salary is:", john.cal_salary(), "\n")
    print("Charlotte's salary is:", charlotte.cal_salary(), "\n")
    print("Matt's salary is:",  matt.cal_salary(), "\n")

if __name__ == "__main__":
  main()