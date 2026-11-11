'''
python -->POP,OOP
POP-->procedure oriented programming --->functions

function --> a function is a block of code(statements) which performs a specific task.it is a reusable code -->readbility,reusability and easy to maintain .....

types  of functions-
---------------------
1.user defined function -->def
2.bulit in functions---> python by default (print,len,max,min,sorted,str,list,bool,dict....)
3.Anonymous functions ---> nameless function -->lambda (map filter)
4.Recursive functions ----> recursion -->factorial,fibonnacci---> decorators




syntax:

def fname(parameters):#Function header
     """doc string(description of function)"""
     statement(s).....#body of function
     .........
     return value(s)
     fname(args)#function call


#simple function to understand the reusability
def add(a,b):
    """this function returns the sum of objects""" 
    c = a+b
    #print(c)
    return c
print(add(21,32))
print(add(89,13))
print(add('code','gnan'))
print(add([1,2],[1,4,5]))



def add(a,b):
    """sample add function"""
    return f'result is {a+b}'
c,d = map(int,input().split())
print(add(c,d))
print(add('code','gnan'))
g,h = 67,-98.5
e = add(g,h) #assigning function to the variable
print(a)
'''

#functions are also objects
def greetings():
    """greetings to the user"""
    #return "welcome to codegnan"
    #return 24+234#a function can have multiple values to return but not multiple return statements
    return len(("hey","guys","python","pfs-vsp-007"))
print(greetings())
print(greetings()*5)
print(type(greetings))#returns function
print(type(greetings()))#returns type of function

