'''#1. Student Name Formatter
#A college registration system receives student names in inconsistent formats.Normalize the name so that each word begins with a capital letter.

name = "sAkEtH kAlLePu"
print(name.title()) #Saketh Kallepu

#2. Customer Email
#Cleanup An online shopping application receives an email address with accidental spaces and uppercase letters.Clean it before storing it.

email = " Saketh.KALLEPU@GMAIL.COM "
email = email.strip().lower()
print(email)#saketh.kallepu@gmail.com

#3. Product Code Replacement
#A company has changed its product prefix from OLD to NEW. Update the product code.

product_code = "OLD-101-OLD-202"
product_code = product_code.replace('OLD','NEW')
print(product_code)#NEW-101-NEW-202 

#4. Username Generator
#A website creates usernames by combining a student's first name and graduation year, separated by an underscore. Convert the first name to lowercase.

first_name = "SAKETH"; year = 2027
print(first_name.lower(),year,sep='_') #output:saketh_2027
print(f'{first_name.lower()}_{year}')

#5. Sentence Character Count A content-writing application needs the total number of characters in a sentence, including spaces.

sentence = "Python makes coding easy"
print(len(sentence)) #output:24 

#6. Employee ID Extraction An employee ID starts with EMP followed by a six-digit number. Extract the numeric portion.

employee_id = "EMP582741"
print(employee_id[3:]) #output:582741

#7. Mask a Bank Account Number
#A banking application displays only the last four digits of an account number.Replace the preceding digits with eight asterisks.

account_number = "123456789012"
print('*' * (len(account_number)-4) + account_number[-4:]) #********9012
print(f"{'*' * 8}{account_number[-4:]}") #********9012 

#8. Alternating Character Extraction Extract every second character from the string, starting with the first character.

text = "CODEGNANPYTHON"
print(text[::2]) #output:CDGAPTO 

#9. Reverse a Product Serial Number Reverse a serial number for a device-testing format.

serial_number = "PYTHON123"
print(serial_number[::-1]) #output :321NOHTYP 

#10. Extract a File Extension A document system needs the final three characters of a filename as its extension.

filename = "student_report.pdf"
print(filename[-3:]) #pdf

#11. Search for a Course Name Count the occurrences of the word Python in a course description, ignoring case.

description = "Python is easy. I love PYTHON. Learn python today."
print(description.lower().count('python')) # output:3

#12. Convert a Sentence into Words Separate a sentence into individual words.

sentence = "Learn Python Full Stack Development"
print(sentence.split()) # output: ['Learn', 'Python', 'Full', 'Stack', 'Development']

#13. Generate a Formatted Address Combine the house number, street, city, and state into one address separated by commas.

house = "12-4";street = "MG Road";city = "Vijayawada";state = "Andhra Pradesh"
print(house,street,city,state,sep=',') #output : 12-4,MG Road,Vijayawada,Andhra Pradesh

#14. Count Words in a Message Calculate the number of words in a message without using loops.

message = "Your application has been successfully submitted"
print(len(message.split())) #output:6

#15. Validate a Coupon Code Display the result of checking whether a coupon code contains only alphabetic characters.

coupon_code = "CODEGNAN"
print(coupon_code.isalpha())#True
coupon_code = "CODEGNAN123"
print(coupon_code.isalpha())#False

#CONDITIONAL STATEMENTS PROGRAMS
1. if Statement Programs

Write a Python program to check whether a user gets a verified badge.
check whether the account is eligible for verification and Meta Verified subscription is active.
If active, display "Verified Badge Granted".
Test Case 1
Input:
Eligible Account: True
Meta Verified Subscription: True
Output:
Verified Badge Granted
Test Case 2
Input:
Eligible Account: True
Meta Verified Subscription: False
Output:
None

Eligible_Account = input("Enter the input:")
Meta_Verified_Subscription = input("Enter the input:")
if Eligible_Account == 'True' and Meta_Verified_Subscription=='True':
    print("Verified Badge Granted")
else:
     print("None")


2. if-else Statement Programs
Q1. Username and Password Login
Write a Python program to validate username and password.
Test Case 1
Input:
Username: admin
Password: admin123
Output:
Login Successful
Test Case 2
Input:
Username: admin
Password: test123
Output:
Invalid Credentials

username = input()
password = input()
if username == 'admin' and password == 'admin123':
    print('Login Successful')
else:
    print('Invalid Credentials')

Q2. Product Search
Write a Python program to check whether a product exists in the available product list.
Test Case 1
Input:
Available Products:
Laptop
Mobile
Watch
Search Product:
Mobile
Output:
Product Found
Test Case 2
Input:
Available Products:
Laptop
Mobile
Watch
Search Product:
Tv
Output:
Product Not Found

Available_Products = list(input())#["Laptop", "Mobile", "Watch"]

Search_Product = input("Search Product: ")

if Search_Product in Available_Products:
    print("Product Found")
else:
    print("Product Not Found")

Q2. Greeting Based on Time
Write a Python program to display greetings based on the current hour.
Conditions:500
● 5 to 11 → Good Morning
● 12 to 16 → Good Afternoon
● 17 to 20 → Good Evening
● Otherwise → Good Night
Test Case 1
Input:
8
Output:
Good Morning
Test Case 2
Input:
15
Output:
Good Afternoon
Test Case 3
Input:
22
Output:
Good Night

hour = int(input("Enter the current hour: "))

if hour >= 5 and hour <= 11:
    print("Good Morning")
elif hour >= 12 and hour <= 16:
    print("Good Afternoon")
elif hour >= 17 and hour <= 20:
    print("Good Evening")
else:
    print("Good Night")
    
Q3. Hostinger Hosting Plan 
Write a Python program to determine the hosting plan based on the customer's budget. 
Conditions: 
● Above ₹10000 → Cloud Hosting 
● Above ₹5000 → Business Hosting 
● Above ₹2000 → Premium Hosting 
● Otherwise → Single Hosting 
Test Case 1 
Input: 
15000 
Output: 
Cloud Hosting 
Test Case 2 
Input: 
7000 
Output: 
Business Hosting 
Test Case 3 
Input: 
3000 
Output: 
Premium Hosting 
Test Case 4 
Input: 
999 
Output: 
Single Hosting

budget = int(input("Enter your budget: "))

if budget > 10000:
    print("Cloud Hosting")
elif budget > 5000:
    print("Business Hosting")
elif budget > 2000:
    print("Premium Hosting")
else:
    print("Single Hosting")


 Instagram Story Visibility 
Write a Python program to check whether a user can view a Close Friends story. 
Conditions: 
● Check whether the user follows the account. 
● If the user follows the account, check whether they are in the Close Friends list. 
● If both conditions are True, display "Story Visible". 
● Otherwise display the appropriate message. 
Test Case 1 
Input: 
Follows Account: True 
Close Friend: True 
Output: 
Story Visible 
Test Case 2 
Input: 
Follows Account: True 
Close Friend: False 
Output: 
Not in Close Friends List 
Test Case 3 
Input: 
Follows Account: False 
Close Friend: False 
Output: 
Follow the Account First

Follows_Account =input("Follows Account: ")
Close_Friend = input("Close Friend: ")

if Follows_Account== 'True':
    if Close_Friend == 'True':
        print("Story Visible")
    else:
        print("Not in Close Friends List")
else:
    print("Follow the Account First")

Q2. BGMI Tournament Entry 
Write a Python program to check whether a player can join a BGMI tournament. 
Conditions: 
● Check whether the player has registered. 
● If registered, check whether the entry fee is paid. 
● If both conditions are True, display "Tournament Entry Confirmed". 
● Otherwise display the appropriate message. 
Test Case 1 
Input: 
Registered: True 
Fee Paid: True 
Output: 
Tournament Entry Confirmed 
Test Case 2 
Input: 
Registered: True 
Fee Paid: False 
Output: 
Entry Fee Pending 
Test Case 3 
Input: 
Registered: False 
Fee Paid: False 
Output: 
Registration Required

registered = input("Registered (True/False): ")
fee_paid = input("Fee Paid (True/False): ")

if registered == "True":
    if fee_paid == "True":
        print("Tournament Entry Confirmed")
    else:
        print("Entry Fee Pending")
else:
    print("Registration Required")

Q Google Drive File Access 
Write a Python program to check whether a user can access a shared file. 
Conditions: 
● Check whether the file link is active. 
● If the link is active, check whether access permission is granted. 
● If both conditions are True, display "File Opened Successfully". 
● Otherwise display the appropriate message. 
Test Case 1 
Input: 
Link Active: True 
Permission Granted: True 
Output: 
File Opened Successfully 
Test Case 2 
Input: 
Link Active: True 
Permission Granted: False 
Output: 
Access Denied 
Test Case 3 
Input: 
Link Active: False 
Permission Granted: False 
Output:  
Invalid File Link

Link_Active =input("Link Active: ")
Permission_Granted = input("Permission Granted: ")

if Link_Active == 'True':
    if Permission_Granted == 'True':
        print("File Opened Successfully")
    else:
        print("Access Denied")
else:
    print("Invalid File Link")
