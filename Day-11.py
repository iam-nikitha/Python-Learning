'''Sets : A set is an unordered,Unindexed,allow unique values,Heterogenous Collection of ietems,Mutable Collection
#A set can contain only tuples in it but not lists,sets.we use set() or data inside {} braces

#subjects = {}#By default it will be empty dictionary
subjects = set()
print(type(subjects))
print(len(subjects))#0
data = ['Python','Aptitude','SQL','SS']
subjects = set(data)
print(subjects)
print(len(subjects))#4
#ids ={123,125,126,129,['poll']}#type Error set does accept list in it 

#Set properties --->Membership,Concatenation
print(123 in {123,124,125})#True
ids = {123,124,125}
new_ids = {126,127}
#total = ids + new_ids # TypeError: unsupported operand type(s) for +: 'set' and 'set'
'''
'''#set is a Mutable collection --> Methods --> insertion,Deletion,along with mathematical set operations

marks = {45,25,35,20,21}

print(type(marks))
print(len(marks))
marks.add(25)# no change in len as set does not add duplicate
print(len(marks))
marks.add(250)
print(type(marks))
print(len(marks))
marks.add((1,2,4))# add tuple in set as len increass by 1
print(marks)
#marks.add([1,2,3])#error

d_marks = [1,2,3,4,5]
marks.update(d_marks) # update the set within itself or can take other sequence
print(marks)
print(len(marks))
marks.update('codegnan')
print(marks)
marks.add('c')
print(marks)

#marks.update(1,2,3)#type error

#print(marks.remove(4)) --> to that value ,value must present in the set it rasis errors existing gives none or not existing gives error
print(marks.remove(45)) 
#discard() removes the an element from the set if exisiting if not it overrides the error
marks.discard(20)
print(marks)
print(marks.discard(20)) #None ..already 20 has been removed it gives none not error
#pop() --> will remove and returns an arbitary element from the set
print(marks.pop())
print(marks.pop())
print(marks.pop())
print(marks.pop())
print(marks.pop())
print(marks.pop())#KeyError: 'pop from an empty set'

#clear --> removes all the elements and returns an empty set
marks.clear()
print(marks)#returns empty set()
'''
#Mathemetical set operations --> union(),intersection(),difference()

a1 = {12,34,23,45}
a2 = {3,34,23,45}
'''
a3 = a1.union(a2) # combine all the elements in both sets without duplicates
print(a3)
print(len(a3))
a4 = a1|a2
print(a4)
print(len(a4))#{34, 3, 12, 45, 23}
#5

a5 = a1.intersection(a2) # returns common elements in both sets
print(a5)
print(len(a5)) # 3
a6 = a1&a2
print(a6)
print(len(a6))# 3

a7 = a1.difference(a2) # {12}
print(a7)#removes the common elements from both sets and returns the elements in the first set

a8 = a1-a2
print(a8) # 12

a9 = a1.symmetric_difference(a2) # removes the common elements in both the sets and gives the remaining elements in both sets
print(a9)
a10  = a2^a1 # {12,3}
print(a10)


# intersection_update() --> performs intersection and update the first set
a3 = a1.intersection_update(a2)
print(a3)
print(a1)
#None
#{34, 45, 23} 

a4 = a1.difference_update(a2)
#print(a4) # none
print(a1)
a5 = a1.symmetric_difference_update(a2) # it removes common elements and give all remaning , that will be updated in first set
print(a1) #{3, 12}

print(a1,a2)
a1.add(3)
print(a1,a2)
#a1 contains all the elements of a2 then a1 is supperset
#a2 is subset
print(a1.issuperset(a2))# true
print(a2.issubset(a1))# true
print(a1.isdisjoint(a2))#false # returns True only when both sets have null intersection

#Dictionaries:A Dictionary is a muttable collection of key ,values pairs we use {k:v}
#keys must be Unique,Mutable,Ordered,Indexed,through keys can be strings,numbers(int,float)

data = {1:'vinay',
        2:'vijay',
        3:'ajay'}
print(data)
print(len(data)) #2
print(type(data))#dict
print(data[2])#vijay
print(type(data[1]))#string
'''

detials = {'ids':['CGVI0242','CGVI0249','CGVI0224','CGVI0240'],
           'names':['Nikitha','Deepthi','Vinay','Tej'],
           'batch':'PFS-VSP-007',
           'place':('Vizag','Vjwda','Hyd','Banglre'),
           'subjects':{'Python','Aptitude','Softskills'}}
#print(detials)
#print(len(detials))#5
#print(detials.keys())
#print(detials['ids'])
print(type(detials['ids']))
detials['ids'].append('CGVI045')
print(detials['ids'])
detials['ids'].insert(3,'CGVI0247')
print(detials['ids'])
print(detials['ids'][:3])#returns first 3 ids
print(detials['ids'][::2])

detials['names'].append('Raju')
detials['names'].append('Sanju')
detials['names'].append('Nihanth')
print(detials)
detials['subjects'].update(['SQL','Flask','FastApi'])
print('detials',detials)
detials['place'] = list(detials['place'])
detials['place'].remove('Vizag')
detials['place'].remove('Banglre')
detials['place'] = tuple(detials['place'])
print(detials['place'])
detials['batch'] = detials['batch'].lower()
print(detials['batch'])




