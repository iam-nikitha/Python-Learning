#copy(),sort(),reverse()
detials = [['Sanjay','Python',50],['Akash','Flask',45],['vinay','Aptitude',30]]
print(detials)
print(len(detials))
print(type(detials))

#copy()--->Creates a shallow copy of the given collection
data = detials.copy()
print(data)
print(len(data))
print(data)
data[0].append('A')#changes done in nested list the reflects in both original and copy
print(data)
data.append('Vizag')#changes done outside the nested list will be reflect in the original but only changes in copy
print(data)
print(detials)
print(len(data))
print(len(detials))

data.extend(['PFS','JFS'])
print(data)
#[['Sanjay', 'Python', 50], ['Akash', 'Flask', 45], ['vinay', 'Aptitude', 30], 'PFS', 'JFS']
print(detials)
#[['Sanjay', 'Python', 50], ['Akash', 'Flask', 45], ['vinay', 'Aptitude', 30]]

detials.extend(['hyd','vizag','vjw','codegnan'])
print(detials) # we made changes in original that will not reflect in copy 
print(len(detials))
print(len(data))


#in the normal list the changes made in copy will not reflect in original
s = ['python','sql','aptitude','softskills']

data = s.copy()
data.insert(2,"forntend")
print(data)
#['python', 'sql', 'forntend', 'aptitude', 'softskills']
print(s)
#['python', 'sql', 'aptitude', 'softskills']

data = s # this is like complete clone of original data
data.insert(2,'forntend')
print(data)
#['python', 'sql', 'forntend', 'aptitude', 'softskills']
print(s)
#['python', 'sql', 'forntend', 'aptitude', 'softskills']
s.remove('python')
print(s)
#['sql', 'forntend', 'aptitude', 'softskills']
print(data)
#['sql', 'forntend', 'aptitude', 'softskills']

marks = [12,15,21,20,19]

#print(marks.sort()) #returns None as nothing to be returned
#marks.sort()
#print(marks)#[12, 15, 19, 20, 21]
#marks.sort(reverse = True)#
#print(marks)#[21, 20, 19, 15, 12]

#marks.append('saketh')
#marks.sort()# raises type error

marks.extend([-23,12,98])
print(marks)
marks.sort(reverse = True)#descending order
print(marks)
 =================================================
#[12, 15, 21, 20, 19, -23, 12, 98]
#[98, 21, 20, 19, 15, 12, 12, -23]


marks.reverse() # returns in reverse order
print(marks)
marks.extend(['poll','sunday',123])
marks.reverse() #it reverse the list and stores and changes in original list
print(marks)
print(marks[::-1]) # it just show reverse list and no changes in the list
print(marks)
#[19, 20, 21, 15, 12]
#[123, 'sunday', 'poll', 12, 15, 21, 20, 19]
#[19, 20, 21, 15, 12, 'poll', 'sunday', 123]
#[123, 'sunday', 'poll', 12, 15, 21, 20, 19]

#min(),max(),len(),type(),sorted()
marks = [20,12,23,25,30]
print(marks)
print(min(marks))#12
print(max(marks))#30
b = sorted(marks)# sorted() function returns a new list with elements in ascending order
print(b)#[12, 20, 23, 25, 30]
print(marks)#[20,12,23,25,30]


#Tuples -->Tuples are Immutable,Ordered,Indexed,Hetrogenous Collection ,it can also duplicates,we use () to store the data

data =()
print(len(data))#0
print(type(data))#tuple

data = 1,2,3
print(data)# considers as tuple
print(type(data))#tuple

data = ('')
print(len(data))#0
print(type(data))#string

data = ('',)
print(type(data))#tuple
print(len(data))#1

l = []
print(type(l))#list
print(len(l)) #0

l = ['']
print(type(l))#list
print(len(l))#1

data = (0)
print(data)
data = 1,2,3,4,
data[-2] = 'codegnan'
#print(data)#TypeError: 'tuple' object does not support item assignment


#Nested Tuples with lists

detials =('vizag',8,('pfs','jfs','da'),['aptitude','softskills'])

print(len(detials))#4
print(detials[:2])#('vizag', 8)
print(detials[2][1])#jfs
print(detials[2][::2])#('pfs', 'da')

print(detials[-1])
detials[-1].extend(['python','java'])
print(detials)
#['aptitud', 'softskills']
#('vizag', 8, ('pfs', 'jfs', 'da'), ['aptitud', 'softskills', 'python', 'java']) 
print(detials[0].upper())#VIZAG
print(detials)#same as orginal

#indexing,Slicing,repetation,Merging are possible
temp = (2.3,45,67)
print(len(temp))#3
b = temp*2
print(b)#(2.3, 45, 67, 2.3, 45, 67)
print(len(b))#6
print(b+temp)#(2.3, 45, 67, 2.3, 45, 67, 2.3, 45, 67)


#Tuple Method--> index(),count()

data = (12,3,24,3,12,4,5)

print(data)
print(data.index(3))#1 gives the index of first occurence of value
print(data.index(3,2))#3
print(data.count(3))#2

b = sorted(data)#returns sorted elements in ASC
print(tuple(b))#converts the list into tuple
c = tuple(sorted(data,reverse = True)) #returns tuple in DESC
print(c)
#(3, 3, 4, 5, 12, 12, 24)
#(24, 12, 12, 5, 4, 3, 3)

del data#it completely eleminates the variable
#print(data)#NameError: name 'data' is not defined

#sets:A set is an unordered,Unique,Mutable,collection.It will never duplicates

ids = set()
print(ids)
print(len(ids))#0
print(type(ids))#set


names ={'nikitha','deepu','harika',34,67,34,67}
print(names)
print(len(names))#5

#d = {12,3,4,[12,3,4],45} # we cannot have lists inside a set

d ={12,3,4,(12,3,4),45}
print(d)
print(len(d)) 

#Task: Create a Nested tuple with list inside it and make it call methods of list in tuple

a = ([1, 2, 3], (1, 2, 3), 3, 4, [6, 7, 8])

#print(a)
#print(type(a))
#print(len(a))
# ([1, 2, 3], (1, 2, 3), 3, 4, [6, 7, 8])
#<class 'tuple'>
#5

# Indexing
print(a[0])
print(a[1])
print(a[2])
print(a[-1])
print(a[0][1])
print(a[1][2])

# Slicing
print(a[0:3])
print(a[1:4])
print(a[:3])
print(a[2:])
print(a[:])

# Striding
print(a[::2])
print(a[1::2])
print(a[::-1])
print(a[::3])

print(a[0])
print(a[0][0])
print(a[0][1])
print(a[0][2])

print(a[4])
print(a[4][0])
print(a[4][1])
print(a[4][2])
a[0].extend([5, 6])
print(a)

print(a + (5, 6))

print(a * 2)

print(a.count(3))
print(a.count(4))
print(a.count([1, 2, 3]))
print(a.count((1, 2, 3)))

# index()
print(a.index(3))
print(a.index(4))
print(a.index([1, 2, 3]))
print(a.index((1, 2, 3)))

