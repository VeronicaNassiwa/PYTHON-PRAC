#Adding two numbers
#num1= int(input("Enter first naumber"))
#num2= int(input("Enter second number"))

#ans= num1 + num2
#print(ans) 
from pickle import LIST
from unittest import result


var_num1="hi how are you"

#print(var_num1)
#EXERCISE

numm1=8
numm2=2

multi=numm1*numm2
#print(multi)
                #METHODS EXERCISE
def my_methods( num1,num2):
	return num1 + num2

result=my_methods(4,6)
#print(result)
  
    #LISTS, TUPLES AND SETS
grades=[40,34,56,45] #mutable u can add more grades
grade_tuple=(40,50,90) #unmutable/unchangable
grade_set={500,445,432} #uniq and unordered elements

grades.append(300)
#print(grades)
grade_tuple=grade_tuple + (60,)
#print(grade_tuple)
grade_set.add(90)
#print(grade_set)

    #SET OPERATION

Closewin_customers={"cathy","Nyla","Nasra","Betty"}
closelose_customers={"hussen","ashura","matha","cathy","salama","edith etc"}
#print(Closewin_customers.intersection(closelose_customers))
#print(Closewin_customers.union(closelose_customers))
#print(Closewin_customers.difference(closelose_customers))