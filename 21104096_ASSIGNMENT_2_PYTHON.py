
#ASSIGNMENT 2
#KUNAL SHARMA(21104096)
#ELECTRICAL


#********************************************************************************


#QUESTION 1:-


p="Python is a case sensitive language"

#Part a:

print(len(p))

#Part b:

print(p[::-1])

#Part c:

q=str(p[9:26])
print(q)

#Part d:

print(p[0:10]+"object oriented "+p[-8:])

#Part e:

print(p.find("a"))

#Part f:

print(p[0:6]+p[7:9]+p[10:11]+p[12:16]+p[17:26]+p[27:35])


print('***************************************************************************')


# QUESTION 2:-


a="KUNAL SHARMA"
b=21104096
c="ELECTRICAL"
d=9.9

print("Hey,"+ str(a)+ " Here!\nMy SID is "+ str(b) +"\nI am from " +str(c)+ " department and my CGPA is "+ str(d))


print('***************************************************************************')


# QUESTION 3:-


a=56
b=10

#part A:

print(a&b)

#part B:

print(a|b)

#part C:

print(a^b)

#part D:

print(a<<2)
print(b<<2)

#part E:

print(a>>2)
print(b>>4)


print('***************************************************************************')


# QUESTION 4:-


x=int(input('ENTRE FIRST NUMBER= '))
y=int(input('ENTRE SECOND NUMBER= '))
z=int(input('ENTRE THIRD NUMBER= '))

if x>y and x>z:
    print("GREATEST NUMBER IS: ",x)

elif y>x and y>z:
    print("GREATEST NUMBER IS: ",y)
    
elif z>x and z>y:
    print("GREATEST NUMBER IS: ",z)


print('***************************************************************************')


# QUESTION 5:-


a=input("ENTRE STRING HERE: ")

if "name" in a:
    print('Yes')

else:
    print('No')


print('***************************************************************************')


# QUESTION 6:-


a=int(input("ENTRE FIRST SIDE: "))
b=int(input("ENTRE SECOND SIDE: "))
c=int(input("ENTRE THIRD SIDE: "))

if a>=(b+c) or b>=(a+c) or c>=(a+b):
    print("No")
    
# 'No' means, the entred three numbers cannot form a triangle.

else:
    print("Yes")

# 'Yes' means, the entred three numbers can form a triangle.



print('***************************************************************************')



