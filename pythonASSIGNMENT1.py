# ASSIGNMENT-1

#KUNAL SHARMA
#21104096(ELECTRICAL)


#Question 1:-

a=input("Entre first number= ")
b=input("Entre second number= ")
c=input("Entre third number= ")
Average=(int(a)+int(b)+int(c))/3
print("Average= ",Average)


print('***************************************************************')

#Question 2:-

p=input("Entre Gross Income= ")
q=input("Entre Number of Dependents= ")
r=10000          #standard deduction
s=3000           #Dependent deduction
t= float(p)-int(r)-(int(s)*int(q))      #t is taxable income
tax=t*(20/100)
print("Taxable income= ",t)
print("Tax= ",tax)


print('***************************************************************')

#Question 3:-

SID=input("Entre your SID= ")
NAME=input("Entre your Name= ")
GENDER=input("Entre F for Female, M for Male , U for Unknown= ")
COURSE_NAME=input("Entre your Course Name= ")
CGPA=input("Entre your CGPA= ")
a=[int(SID), NAME , GENDER , COURSE_NAME , float(CGPA)]
print(a)


print('***************************************************************')

#Question 4:-

p=input("Entre Marks of 1st Student= ")
q=input("Entre Marks of 2nd Student= ")
r=input("Entre Marks of 3rd Student= ")
s=input("Entre Marks of 4th Student= ")
t=input("Entre Marks of 5th Student= ")

a=[int(p),int(q),int(r),int(s),int(t)]
a.sort()
print(a)


print('***************************************************************')



# Question 5:-

color=['RED','GREEN','WHITE','BLACK','PINK','YELLOW']

#part a

color.pop(3)
print('New List after deleting fourth item= ',color)

#part b

color[3]=color[4]='PURPLE'
print('New List after replacing BLACK And PINK= ',color[0:4]+color[5:])
