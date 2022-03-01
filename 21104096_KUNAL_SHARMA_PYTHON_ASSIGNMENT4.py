#ASSIGNMENT 4:
#KUNAL SHARMA
#(EE-21104096)




# Question 1:

# Recursive Python function to solve tower of hanoi
def TowerOfHanoi(n, source, auxiliary, target):  
    if(n == 1):  
        print('Move disk 1 from rod {} to rod {}'.format(source, target))  
        return  
    # function call itself  
    TowerOfHanoi(n - 1, source, target, auxiliary)  
    print('Move disk {} from rod {} to rod {}'.format(n, source, target))  
    TowerOfHanoi(n - 1, auxiliary, source, target)  
  
  
n = 3 #no. of disks 
print('Tower of Hanoi with 3 disks: \n')
# Referring source: A, auxiliary: B, and target: C  
TowerOfHanoi(n, 'A', 'B', 'C')  # Calling the function  

print('\n####################################################################################################################################################\n')


# Question 2 : Iterative Approach

n = int(input("Enter the number of rows : "))

print("Pascal's triangle: \n")

for i in range(0, n):
    coff = 1
    for j in range(1, n-i):
        print("  ", end="") 
    
    for k in range(0, i+1):
        print("  ", coff, end="")
        coff = int(coff * (i - k) / (k + 1))
    print()

print('\n####################################################################################################################################################\n')


# Question 2 : Recursive Approach

n = int(input("Enter the number of rows : "))

def triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = triangle(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
    return result

print("Pascal's triangle: \n",triangle(n))

print('\n####################################################################################################################################################\n')


# Question 3

# Taking numbers in input
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))

if(n2 != 0):
  # Calculating Quotient and Remainder
  quotient, remainder = divmod(n1,n2)  # Calling the built-in divmod() function

  # Checking Callable or not
  check = callable(divmod)   # Built-in function to check whether a function/value is callable or not
  if check == True:
    print('\n The function is callable. \n')
  else: 
    print('The function is not callable. \n')

  # Creating a list
  lst = [n1,n2,quotient,remainder]

  # Checking null values
  if(lst.count(0)>0):
      print('There are {} null values present in the list. \n'.format(lst.count(0)))
  else:
      print('No null values present. \n')


  # Adding given values to the list 
  lst.append(4)
  lst.append(5)
  lst.append(6)
  print('Updated list: ',lst, end="\n")

  # Filtering out values>4
  new_lst = []
  for x in lst:
      if x>4:
          new_lst.append(x)
  print('New list: ', new_lst, end='\n')

  # Converting to set
  result = set(new_lst)
  print('Set: ', result)

  # Making set immutable
  print('Frozen set: ', frozenset(result), end='\n')

  # Maximum value
  print('Maximum Value: {} and its Hash Value: {}'.format(max(result),hash(max(result))), end='\n')

else:
  print("Error: Denominator can't be 0. \n")



print('\n####################################################################################################################################################\n')

#Question 4

# Class for Student
class Student:

  # Initializing
  def __init__(self,name, rollNo):
    self.name = name
    self.rollNo = rollNo
  
  # Printing 
  def show(self):
    print('Name: {}'.format(self.name) + '\t Roll No.: {}'.format(self.rollNo))

  # Deleting (Calling destructor)
  def __del__(self):
    print('Destructor called, Object named {} deleted.'.format(self.name))

# Object of Student class
student1 = Student("Kunal", 21104096)
student1.show()
del student1


print('\n####################################################################################################################################################\n')


#Question 5

class Employee:

    # Initializing
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    # Printing
    def show(self):
        print('Name: {}'.format(self.name) + '\t Salary: {}'.format(self.salary))

    # Updating
    def update(self):
      if(self.name == 'Mehak'):
        self.salary = 70000

    # Deleting (Calling destructor)
    def __del__(self):
      if(self.name == 'Viren'):
        print('Destructor called, Object named {} deleted.'.format(self.name))


# Objects of Employee class
emp1 = Employee("Mehak",40000)
emp2 = Employee("Ashok",50000)
emp3 = Employee("Viren",60000)

# Initial details
print('Initial details of employee: ')
emp1.show()
emp2.show()
emp3.show()

# Updating record
print('Updated details of Employee: ')
emp1.update()
emp1.show()

# Deleting record
del emp3

print('\n####################################################################################################################################################')


# Question 6

# Taking George's word in input
George = input("Enter the word uttered by George: ")
George = George.lower()

# Taking Barbie's word in input
Barbie = input("Enter a new meaningful created by Barbie: ")
Barbie = Barbie.lower()

# Matching whether the two words have exactly all same characters
def countChar(George):
    count = {}
    lst = list(George)
    
    n = len(lst)
    for i in range(n):
        if lst[i] in count:
            count[lst[i]] += 1
        else:
            count[lst[i]] = 1
    return count

#Checking whether Barbie's word makes sense or not
def friendshipCheck():
    if countChar(George) != countChar(Barbie):
        print("Friendship is fake as there is letter mismatch in Barbie's word. \n")
        return
    check = input("Does the Barbie's word make sense? Enter either y/Y or n/N ")

    if check == 'y' or check == 'Y':
        print("Friendship test passed. \n")
    elif check == 'n' or check=='N':
        print("Friendship is fake as Barbie's word is meaningless")
    else:
        print("Please try again with either y/Y or n/N in order to confirm whether Barbie's word makes sense. \n ")
        friendshipCheck()

friendshipCheck()


print('\n####################################################################################################################################################')




