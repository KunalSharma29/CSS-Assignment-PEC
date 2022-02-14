
#ASSIGNMENT 3
#KUNAL SHARMA (21104096)
#ELECTRICAL


#QUESTION 1:

#Enter the input string
string = input("Enter the input string ")
string = string.lower()                   #Converting string to lower case to handle the case sensitivity
tokens = string.split()                   #Creating a list named tokens consisting of the words present in the input string
if(len(tokens)==1):                       #Input string is a word
  char_set = set()                        #Set of all the uniques words present in the string
  for char in string:
    char_set.add(char)               
  for char in char_set:
    print("Number of occurances of ",char,"in the given input string:", string.count(char),'\n')
else:                                       #Input string is a sentence
  word_set = set()                          #Set of all the uniques words present in the string
  for word in tokens:
    word_set.add(word)
  for word in word_set:
    print("Number of occurances of ",word,"in the given input string:", string.count(word),'\n')                                        

print('******************************************************************************************************************************')


# QUESTION 2:

#Enter the input date
day = int(input("Enter the Day "))
month = int(input("Enter the Month "))
year = int(input("Enter the Year "))
d=0       #updated day
m=0       #updated month
y=0       #updated year
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:            #for months having 31 days
  if(day == 31 and month is not 12):
    d=1
    m=month+1
  elif(day==31 and month==12):
    d=1
    m=1
  else:
    d=day+1
    m=month

  if(d<10):                                        #converting date to the required format
    d=str(0)+str(d)

  if(m<10):                                              #converting month to the required format     
      m=str(0)+str(m)

elif month == 4 or month == 6 or month == 9 or month == 11:                  #for months having 30 days
  if(day == 30):
    d=1
    m=month+1
  else:
    d=day+1
    m=month

  if(d<10):                                                                  #converting date to the required format
    d=str(0)+str(d)

  if(m<10):                                                                 #converting month to the required format                                
    m=str(0)+str(m)

elif month==2:                                                     #for February
  if(day==29 and (year%4)==0):                                     #leap year
    d=1
    m=month+1
  elif(day==28 and (year%4) is not 0):
    d=1
    m=month+1
  else:
    d=day+1
    m=month

  if(d<10):                                                                #converting date to the required format
    d=str(0)+str(d)

  if(m<10):                                                                    #converting month to the required format
    m=str(0)+str(m)

if(day==31 and month==12):                                        #updating year
  y=year+1
else:
  y=year
print("New Date:",d,'/',m,'/',y)


print('******************************************************************************************************************************')


# QUESTION 3:

#Enter the size of the list
s = int(input("Enter the size of the list of numbers "))
#Creating the list of numbers
lst = []
for x in range(s):
  num = int(input("Enter the number "))
  lst.append(num)
output = []
for x in lst:
  output.append((x,x*x))              #appending a tuple of list item and its square to the output list
print("Numbers and their squares:")
print(output)



print('******************************************************************************************************************************')


#QUESTION 4:


#Enter the grade in input
grade = int(input("Enter the grade\t"))
if grade<4 or grade>10:
  print("Error \n Grade out of range", end=" ")
else:
  if grade==4:
    print("Your Grade is 'D' and Poor Performance")
  elif grade==5:
    print("Your Grade is 'C' and Below Average Performance")
  elif grade==6:
    print("Your Grade is 'C+' and Average Performance")
  elif grade==7:
    print("Your Grade is 'B' and Good Performance")
  elif grade==8:
    print("Your Grade is 'B+' and Very Good Performance")
  elif grade==9:
    print("Your Grade is 'A' and Excellent Performance")
  elif grade==10:
    print("Your Grade is 'A+' and Outstanding Performance")

   


print('******************************************************************************************************************************')


#QUESTION 5:

inc = 11            #total increment till K alphabet: 65+11
# outer loop
for row in range(0,6):
    spaces=0
    for spaces in range(0,row):      #Handling spaces
      print(' ',end='')
    # inner loop
    for j in range(65,65+inc):
      print(chr(j),end="")  
    row=row+1
    inc=inc-2            #decrementing the count of alphabets by 2 for every next line
    print()

print('******************************************************************************************************************************')


#QUESTION 6:

#Enter Y/N to ask if the user wants to give the entry
a = input("Enter Y if you want to give student entry else N: ")
d = {}   #Creating the dictionary
while(a=='Y'):
  #Enter the student credentials
  sid = int(input("Enter SID of the student: "))
  name = input("Enter name of the student: ")
  d.update({sid:name})
  a = input("Enter Y if you want to give entry else N: ")
  if(a=='N'):
    break

#Part-A
if(a=='N'):
  print("Student details: ",d)

#Part-B
sd_names = dict(sorted(d.items(), key=lambda item: item[1]))
print("Sorted dictionary according to names: ",sd_names) 

#Part-C
sd_key = {k : d[k] for k in sorted(d)}     
print("Sorted dictionary according to SID: ",sd_key)

#Part-D
search = int(input("Enter the SID you want to search for: "))
if search in d:
  print("Name of the student: ", d[search])
else:
  print("Not a valid SID")


print('******************************************************************************************************************************')



#QUESTION 7:

# Enter number of terms needed in Fibonacci Series                
num = int(input("Enter the number of terms in the Fibonacci Series: "))
first = 0                                         #first element of series
second = 1                                        #second element of series
sum = 0
if num==1:
    print("The requested series is",first)
else:
    print(first,second,end=" ")
    sum = sum + second                     
    for x in range(2,num):
        next = first + second                      
        print(next,end=" ")
        sum = sum + next
        first = second
        second = next
    print("\nAverage of the resultant Fibonacci series", sum/num, '\n')
    




print('******************************************************************************************************************************')


#QUESTION 8:

set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}
set_union = set().union(set1).union(set2).union(set3)             #union of set1, set2 and set3
set_a = set()
set_b = set()
set_c = set()
set_d = set()
set_e = set()

#Part-A
set_a = set1^set2                 #XOR Operator for adding elements in set_a which are present in set1 and set2 but not both
print("Set of elements present in either set1 or set2:", set_a)

#Part-B
set_b = set1^set2^set3                      #XOR operator for adding elements that are in only one of the three sets set1, set2 and set3
print("Set of elements that are present in only one of the three sets set1, set2 and set3:", set_b)

#Part-C
set_c = set_union - (set1^set2^set3) - (set1&set2&set3)    #Union - elements present in only 1 of the three sets - elements present in all three sets
print("Set of elements that are exactly in two of the sets Set1, Set2 and Set3:",set_c)

#Part-D
for x in range(1,11):                    
  if x not in set1:                          
    set_d.add(x)                                            #adding elements in the range 1 to 10 that are not in Set1:
print("Set of all integers in the range 1 to 10 that are not in Set1:",set_d)

#Part-E
for x in range(1,11):
  if ((x not in set1) and (x not in set2) and (x not in set3)):
    set_e.add(x)                                   #adding elements in the range 1 to 10 that are not in Set1, Set2 and Set3:
print("Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3:",set_e)




print('******************************************************************************************************************************')











































