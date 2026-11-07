'''
usage of for with for
Nested loops --->loops inside another loop.
they are common used in pattern printing ,matric operation,
and solving various alogorithms problem


Syntax:
for i in range(outer_loop_range):
for j in range(inner_loop_range):
#code...

#understand with the simple example
for i in range(3):#outer loop runs 3 times
    for j in range(2):#inner loop runs 2 times for each output
        print(f'i={i},j={j}')
# for every outerloop inner loop will be completely excuted..
# outer loop -->rows --->inner loop ---> colums

for i in range(3): # --->i -->0,1
    for j in range(4):#--->j-->0,1,2,3
        print(i,j)
# numbers patterns --> Row based number patterns,colums based numbers patterns

1 2 3
1 2 3
1 2 3

for i in range(1,4): #i-->1,2,3
    for j in range(1,4):
        print(j,end=' ')
    print()
    
#1 1 1 1 1
#2 2 2 2 2
#3 3 3 3 3
#4 4 4 4 4


for i in range(1,5): # --->i -->0,1
    for j in range(1,6):#--->j-->0,1,2,3
        print(i,end=' ')
    print()

#A B C D
#A B C D
#A B C D
#A B C D

for i in range(1,5):
    for j in range(1,5):
        print(chr(64+i),end=' ')
    print()

#1 2 3
#4 5 6
#7 8 9
num = 1
for i in range(1,4): # --->i -->0,1
    for j in range(1,4):#--->j-->0,1,2,3
        print(num,end=' ')
        num = num + 1
    print()

#square patterns-->with * with n number of row and columns
n = int(input("Enter the value:"))
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()

# change this with different values

n = int(input("Enter the value:"))
for i in range(n):
    for j in range(n+1):
        print('*',end=' ')
    print()
'''
#Right angled triangle
'''
*
* *
* * *
* * * *
* * * * *

n = int(input('enter the value:'))
for i in range(1,n+1):
    for j in range(i):
        #print(f'value of i is {i},value of j is{j}')
        print('*',end=' ')
    print()


inverted Triangle
* * * * *
* * * *
* * *
* *
*
'''
n = int(input('enter the value:'))
for i in range(n,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()
#task
#1
#2 3
#4 5 6
#7 8 9 10
num = 1

for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


#A
#B C
#D E F
#G H I J
ch = 65

for i in range(1, 5):
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()

#A
#A B
#A B C
#A B C D
#A B C D E

for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


    
    
