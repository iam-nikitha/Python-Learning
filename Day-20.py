'''#Functions --> A Resuable block of code which is used to perform task.
def fuction_name(parameters):
    """docstring """
    statments(s)....
    ......
    return value(s)
fuction_name(Arguments) #actual arguments where data is passed
Types of Function Arguments:
1.Positional Arguments--->count of arguments to be matched
2.Default Arguments-->A default value is assigned to parameter
3.Keyword Arguments-->arguments are passed using parameters names
4.Variable Length Arguments(*args)--->we can use any number of positional arguments
Keyword  variable Length Arguments(**Kwargs)---->we can pass any number keyword arguments


#1.Positional Arguments:-Arguments are assigned to their position count and order should be matched
def data(a,b,c):
    """Function to perform Arthmetic Operations"""
    d = a+b+c
    e = a-b-c
    f = a*b*c
    g = a/b/c
    return d,e,f,g
#print(data(12,13,2))
#print(data(2,10))#it raises a type error as count is mismatched
#print(data(12,13,2,5))#TypeError: data() takes 3 positional arguments but 4 were given

g,m,f =map(int,input().split())
result = data(g,m,f)
print(f'Result is {result}')

username1 = "Nikitha"
password1 = "Nikitha@123"
def log(username,password):
    if username1 == username and password1 == password:
        print("you can login successfully")
    else:
        print("Ivalid login data")
c,d = map(str,input().split())
log(c,d)

#Default Arguments -- we can pass arguments as defualt values
if no value is passed during the function call,the defualt value is used.
def data(a,b=5,c=2):#non default arguments always follows default arguments
    """Function to perform Arthmetic Operations"""
    d = a+b+c
    e = a-b-c
    f = a*b*c
    g = a/b/c
    return d,e,f,g
#print(data(2,4,6))
#print(data(12))#we need to metion other args as they are default
#print(data(2,4))#here one default argument taken

d =int(input())
print(data(d))
'''
#3.Keyword Arguments: Arguments are passed using parameter names
#def grocery(item = 'Milk',price ):#not possible
#def grocery(item,price):
def grocery(item,price=40):
    """ Usage of keyword arguments"""
    print(f'item is {item}')
    print(f'Value of item is {price}')
#grocery('Milk',35)
#grocery(40,'bread') #in this case order differs result changes
grocery(item = 'Bread')
#print(groceery(price = 45,item = "Bread")) # returns none as output
#grocery(items = 'milk',price = 35)#type error as keyword is mismatch

#Variable length arguments --> We can give any number of positional arguments
#arguments we use(*args),captures excess positional arguments and pack them in tuple

def sample(*a):
    """Usage of arbitary argumenta"""
    print(a)
    print(type(a))
sample()
sample(1,2)
sample('Nikitha','Betch')
sample(12,3,4,5)
