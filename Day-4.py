'''
Sequence Datatype --->Strings,List[],Tuples(),Sets{},frozensets,Mapping(Dictionaries)
#List ---> A list is ordered,Mutable,Indexed and Heterogenous Collection
#we use [] to represent lists
#EX: Students detials,Orders,stock entries..
#list creation
Details = [1,'Nikitha','PFS7','vizag',56.7]
print(len(Details))
print(type(Details))
stu_ids = ['CGVI0123','CGVI0234','CGVI0345']
print(stu_ids[1]) #Indexing-->Accessing the elements of list
stu_ids[0] = 'Codegnan'#Mutable --> it can changed after creating
print(stu_ids)
#tuples --> Tuples are also Immutable,Ordered,Indexed and hetrogenous Collections
#we use () Parenthesis
#dimensions,coordinates..It can contain duplicates
Places = ('Vizag','Hyberabad','Chennai')
print(Places)
print(type(Places))
print(len(Places))
#Places[0] = 'Delhi'
#print(Places) #TypeError: 'tuple' object does not support item assignment
#even if u not specificed the () if it a values seperated with , it consider as tuples
dimension = 10,20,30
print(dimension)
print(type(dimension)) --->(10, 20, 30) <class 'tuple'> 
#sets --> A set is unordered unindexed,Mutable collection
#unique collection(remove duplicates)
ids = set()#empty set
print(ids)
ids = set([123,124,125,123])#set(){123, 124, 125}
print(ids)
ids = set((123,124,125,123))
courses = {'PFS','java','DA'}#{'java', 'PFS', 'DA'}
print(courses)
print(type(courses))#<class 'set'>
print(courses[0])#TypeError: 'set' object is not subscriptable
#set is unordered so it is not indexed
#Dictionaries--> A dictionary (mapping object) is a collection of key_value paris
#dict ={k:v} we can access values through keys,and keys should be unique(keys can be int,flaot,str
details = {'branch':'Vizag',
           'batch':['PFS-Vsp-007','PFS-Vsp-005','PFS-Vsp-006','PFS-Vsp-007'],
           'course':'PFS',
           'count':19}
print(details)#{'branch': 'Vizag', 'batch': 'PFS-Vsp-007', 'course': 'PFS', 'count': 19}
print(type(details))#<class 'dict'>
print(len(details))#4
print(details['batch'])#PFS-Vsp-007
#every built-in datatype is built -in fuction
#functions -- int,flaot,complex,bool,str,lists,tuple,sets,dictionary
marks = [35,25,54] # converting list into 
a = tuple(marks)
print(a)#(35, 25, 54)
b = set(marks)
print(b)#{25, 35, 54}
c=str(marks)# no
print(c)#[35, 25, 54]
print(len(c))#12 it considers every symbol as a character
t = (1,2,3)
d = list(t)#[1, 2, 3]
print(d)
e = str(t)#(1, 2, 3)
print(e)
f = set(t)
print(f)#{1, 2, 3}
m = [12,34,56]#l--->d
t = (12,24,56)#t--->dict
#d = dict(marks) # it is not possible like this
e = dict.fromkeys(m)#we need to use fromkeys(),list values are taken as keys and value will be null
print(e)#{12: None, 34: None, 56: None}
e1 = dict.fromkeys(t)
print(e1)#{12: None, 24: None, 56: None}
#Dictionaries--->list,tuples,sets
ids ={1:123,2:234}
a = list(ids)#[1, 2] it will avoid the values only fetch keys
print(a)
b = set(ids)#{1, 2} it will avoid the values 0nly fetch keys
print(b)
c = str(ids)#{1: 123, 2: 234}#every  symbol will be a character
print(c)
#Fronzensets ---> it is an immutable set,unindexed,unoredered
#we can typecase it to list,tuple,set,dict
a = frozenset((12,32,12,32))
print(a)#frozenset({32, 12})
b = set(a)
print(a)
c = tuple(a)
print(c)
d = list(a)
print(d)
e = dict.fromkeys(a)
f = str(a)
print(e)
print(f)'''
"""(32, 12)
[32, 12]
{32: None, 12: None}
frozenset({32, 12})"""
#str--->list,set,tuple,dict
n = 'nikitha reddy'
a = set(n)
b = tuple(n)
c = list(n)
d = dict.fromkeys(c)
print(a,b,c,d)

#operator--> Aritmetic operators,Assignment operators,Comparison operators,Logical operators
#membership,Indentity,Bitwise
#Arithmetic operators
a = 3
b= 2
print(a+b) #5
print(a-b)#1
print(a*b)#6
print(a**b)#expotential 3 square 9
print(a//b) # gives quotient and that is integer 1
print(a%b)# gives remainder 1
