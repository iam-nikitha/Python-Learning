''' #range(stop) --> takes by defuallt minimum value as 0
for i in range(5):
    print(f'Value of i is {i}')
    print(f'Square of i is {i**2}')

#range(start,stop)---> u can metion start and stop positions
#start is included ,end is excluded
for i in range(1,11):
    print(i,i**2)
    print('<---->')

#range(start,stop,step)
for i in range(1,21,1):
    print(i)
for i in range(1,21,2):
    print(i)
#get first 10 even numbers
for i in range(2,21,2):
    print(i)

for i in range(10,0,-1):
    print(i)

#chr takes the input as ascii value of alphabets and ord takes input string
for i in range (65,91):
    #print(i,chr(i))
    print(chr(i),end=' ')
# reverse alphabets

for i in range(90,64,-1):
    print(chr(i),end=' ')  

names = ['Akash','Kaushik','Vijay','Sanjay','Lokesh']
#for name in names:
    #print(name,end=' ')
for i in range(len(names)):
    print(names[i])

#ask input from user and get sun of numbers as per input

num = int(input('Enter the value :'))
if num >0:
    sum = 0
    for i in range(num+1):
        sum += i
    print(sum)
else:

    print("No Output")
#use case : checking daily workout app usage

work_log = [1,1,1,0,1,1,0]
longest_workout_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
        current_streak+=1
        if current_streak > longest_workout_streak:
            longest_workout_streak = current_streak
    else:
        current_streak = 0
print(f'Longest Streak is {longest_workout_streak}')

'''
work_log =[1,1,1,0,1,1,0]
longest_workout_streak = 0
current_streak = 0
for day in range(len(work_log)):
    if work_log[day] == 1:
        current_streak+=1
        if current_streak > longest_workout_streak:
            longest_workout_streak = current_streak
    else:
        current_streak = 0
print(f'Longest Streak is {longest_workout_streak}')
        
                
