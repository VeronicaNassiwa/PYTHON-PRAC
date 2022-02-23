from turtle import clear
from unicodedata import name


def students():
    student_1= {'name': 'Veronica',
    'age':'50',
    'religion':'Islam',
    'coursunits':['basicmath','computer ethics','database programming','softwareprogramming']}
    #return student_1['coursunits']
    #print(student_1['coursunits'])
    student_name=input("Enter the student name: ")
    if  student_name==student_1['name']:
        print("{} is enlolled".format(student_1['name']) )
    else:
        print("{} is not studing from here!".format(student_name))    

students() 


