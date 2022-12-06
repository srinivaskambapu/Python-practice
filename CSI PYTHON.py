#!/usr/bin/env python
# coding: utf-8

# In[2]:



N = int(input("Enter the number of rows: "))   
k = 2 * N - 2    
for i in range(0, N):  
    for j in range(0,k):  
        print(end=" ")  
    k = k -2
    for j in range(0, i + 1):  
        print(" * ", end=" ")  
    print(" ")  


# In[2]:


N = int(input("Enter the number of rows: "))   
k = 2 * N - 2    
for i in range(N, -1 , -1):  
    for j in range(k, 0 , -1):  
        print(end=" ")  
    k = k + 1  
    for j in range(0, i + 1):  
        print("*", end=" ")  
    print("")  
    


# In[23]:


def fb(N):
    a=0
    b=1
    print(a)
    print(b)
    for i in range (2,N+1):
        c=a+b
        a=b
        b=c
        print(c)
fb(int(input("NUM")))


# In[50]:


N = int(input("Enter the number of rows"))  
k = 2 * N - 2      
for i in range(0, N): 
    for j in range(0, k):  
        print(end=" ")  
    k = k - 1   
    for j in range(0, i + 1):  
        print("* ", end="")  
    print("")    
k = N - 2  
for i in range(N, -1, -1): 
    for j in range(k, 0, -1):  
        print(end=" ")   
    k = k + 1   
    for j in range(0, i + 1):  
        print("* ", end="")  
    print("")  


# In[55]:


n = int(input("Enter the number of rows "))
m=1
for i in range(1, n+1):
    for j in range(1,i+1):  
        print(m, end=' ') 
    print("")
    m=m+1


# In[1]:


nums = [1,2,3,4,5]
for num in nums:
    if num>3:
        break
    print(num)


# In[5]:


st=(input("enter any sentence for finding length:- "))
print(st)
c=len(st)
print(c)


# In[15]:


st= ("   from lpu   ")
stt=st.strip()
print(stt)


# In[3]:


a="hello "
b="hello"
c="Hello"
print(a==b)
print(a*5)
d="welcome to vit"
e=d.replace("vit","lpu")
print(e)
f=d.split(" ")
print(f)


# In[26]:


nums="1,2,3,4,56,7,8,9"
n= nums.split(",")
print(n)
b= '-'.join(n)
print(b)
a="python"
print(a.swapcase())
print(a.upper())
print(a.title())


# In[27]:


q="Hello"+"world"
print(q)
print(min(2,100))
print(max(3,100))


# In[28]:


s="hello world"
d=s[1:4]
print(d)
d=s[:4]
print(d)
f=s[5:]
print(f)


# In[4]:


s="hello world"
d=s[::-1]
print(d)


# In[33]:


s="hello world"
print(s.endswith("rd"))
print(s.startswith("hell"))
print(s.count("o"))
print(s.rfind("o"))
print(s.find("o"))


# In[2]:


l=["csi",1,"ece",2,"pes"]
print(l)


# In[13]:


li=[10,20,30,40]
print(len(li))
print(max(li))
print(min(li))
print(sum(li))


# In[26]:


li=[10,20,30,40]
print(li[-2:])


# In[41]:


li=[10,20,30,40] 
li2=[10,20,30,40,50]
li3=li+li2
li[2]=99
print(li3)
li4=(li3+li2)*2
print(li4)
if 10 in li4:
    print("true")


# In[42]:


li=[10,20,30,40] 
li2=[10,20,30,40,50]
li[2]=99
li3=li+li2
print(li3)


# In[49]:


li=[10,20,30,40,10] 
c1=[99,25,7,5]
li.extend(c1)
print(li)
li.append(40)
print(li)


# In[67]:


li=[10,20,30,40,100]
i=li.index(40)
print(i)
li.pop(3)
print(li)
li.insert(2,30)
print(li)


# In[68]:


li=[10,20,30,40,10]
li.remove(10)
print(li)
li.reverse()
print(li)
li.sort()
print(li)


# In[73]:


subjects=["English:" , "Science:" , "C++ :" , "C:" , "Python:" ]
Marks=[20,10,50,60,40]
subjects.pop(1)
print(subjects)
Marks.pop(2)
print(Marks)
subjects.insert(2,"Java")
print(subjects)


# In[5]:


#largest number in the list
li=[1,2,3,4,5,66666,99,56]
li.sort()
print("larget number is" , li[-1])


# In[16]:


#Python program to count the number of strings where the string length is 2 or more 
#and the first and last character are same from a given list of strings
a=0
l=["sasuke","itachi","madara","hashirama","naruto","obito"]
for i in l: 
    if len(i)>1 and i[0]==i[-1]:
        print(i)
        a+=1
print(a)


# In[18]:


#Python program to select the odd items of a list
a=["q","w","e","r","t","y","u","i","op","a","s","d",'f','gh','j','k','l','x','c','v','b']
print(a[::2])


# In[22]:


#Python program to iterate over two lists simultaneously
subjects=["English:" , "Science:" , "C++ :" , "C:" , "Python:" ]
Marks=[20,10,50,60,40]
for (a,b) in zip (subjects,Marks):
    print(a,b)


# In[23]:


#program to display those items from a list that is divisible by 7
a=[7,14,21,35,42,4,48,69]
for i in a:
    if i%7==0:
        print(i,"is divisible by 7")
    else:
        print(i,"not divisible by 7")


# In[11]:


thisdict1=["BCA","MCA","MBA"]
thisdict2=[101,102,103]
thisdict3=["itachi","sasuke","kakashi"]
for (a,b,c) in zip (thisdict1,thisdict2,thisdict3):
    print("Course:-",a,",UID:-",b,",studentname:-",c)


# In[16]:


thisdict={"Courses":["BCA","MBA","MCA"],"UID":[101,102,103],"STUDENTNAME":["ITACHI","SASUKE","KAKASHI"]}
for x in thisdict.values():
    print(x)


# In[18]:


thisdict={"Courses":["BCA","MBA","MCA"],"UID":[101,102,103],"STUDENTNAME":["ITACHI","SASUKE","KAKASHI"]}
for x,y in thisdict.items():
    print(x,y)


# In[14]:



for i in range (100):
    i=i+1
    print(i)


# In[22]:


dic={"uchiha":["sasuke","itachi","madara"]}
print(len(dic))


# In[26]:


mydict={"uchiha":["sasuke","itachi","madara"]}
print(mydict.keys())


# In[27]:


mydict={"uchiha":["sasuke","itachi","madara"]}
mydict["uchiha"]="kakashi"
print(mydict)


# In[29]:


mydict={"uchiha":["sasuke","itachi","madara"]}
mydict1={"uzumaki":["naruto","kushina","nagato"]}
mydict.update(mydict1)
print(mydict)


# In[36]:


mydict={"uchiha":["sasuke","itachi","madara"]}
mydict1={"uzumaki":["naruto","kushina","nagato"]}
if "uchiha" in mydict:
    print("TRUE")
else:
    print("False")


# In[37]:


mydict={"uchiha":["sasuke","itachi","madara"]}
mydict1={"uzumaki":["naruto","kushina","nagato"]}
mydict["uchiha"]="sasuke","itachi","madara","kakashi"
print(mydict)


# In[45]:


tup1=(1,2,3,4,5)
tup2=(6,7,8,9,10)
print(len(tup1))
print(tup2+tup1)
print(sum(tup1))
print(max(tup1))
print(min(tup2))
print(tup2*3)
print(tup1[:2])
print(tup1[2:])


# In[47]:


list1=[1,2,3,4,5]
tup1=tuple(list1)
print(tup1)


# In[53]:


set={1,2,3,4,5,6,7,8,9}
print(set)


# In[3]:


set={1,2,3,4,5,6,7,8,9}
set1={1,2,23,34,45,56,67,78,89}
print(set.intersection(set1))
print(set)
set.pop()
print(set)
print(set.union(set1))
print(set.pop())


# In[21]:


class Shape:
    type1="circle"
    type2="square"
    type3="rectangle"
    def display(self):
        print("type1:%s\ntype2:%s\ntype3:%s"%(self.type1,self.type2,self.type3))
sp=Shape()
sp.display()


# In[10]:


class Animals:
    def __init__(self,mood):
        self.mood=mood
        print("Hi I'm ",self.mood)
sent= Animals('HUNGRY')
        


# In[19]:


class Animals:
    def __init__(self,mood):
        self.mood=mood
    def var(self):
        print("Hi I'm ",self.mood)
sent= Animals('HUNGRY')
sent.var()


# In[24]:


class Employee:    
    id = 10   
    name = "John"    
    def display (self):    
        print("ID: %d \nName: %s"%(self.id,self.name))     
emp = Employee()    
emp.display()    


# In[34]:


class Employee:  
    def __init__(self, name, id):  
        self.id = id  
        self.name = name
    def display(self):  
        print("ID: %d \nName: %s" % (self.id, self.name))  
emp1 = Employee("John", 101)  
emp2 = Employee("David", 102)  
emp1.display()   
emp2.display()  


# In[40]:


class Student: 
    def __init__(self):  
        print()
    def display(self,name):  
        print("Hello",name)  
student = Student()  
student.display("John")     


# In[41]:


class Student: 
    def __init__(self, name):   
        self.name = name  
    def display(self):  
        print("Hello",self.name)  
student = Student("John")  
student.display()    


# In[5]:


class Student:  
    roll = 10  
    name = "Itachi" 
    def display(self):  
        print("Roll: %d \nName: %s"% (self.roll,self.name))
abc= Student()  
abc.display()


# In[54]:


class Student:  
    def __init__(self):  
        print("The First Constructor")  
    def __init__(self):  
        print("The second contructor")  
st = Student()  


# In[59]:



class Student:  
    def __init__(self, name, id, age):  
        self.name = name  
        self.id = id  
        self.age = age  
a= Student("Itachi", 6, 18)    
print(getattr(a, 'name'))  
setattr(a, "age", 19)  
print(getattr(a, 'age'))  
print(hasattr(a, 'id'))  
delattr(a, 'age')  
print(a.age)  


# In[66]:


class Student:    
    def __init__(self,name,id,age):    
        self.name = name;    
        self.id = id;    
        self.age = age    
    def display_details(self):    
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id))    
s = Student("Itachi",6,9)    
print(s.__doc__)    
print(s.__dict__)    
print(s.__module__)


# In[68]:


class Human:  
    def speak(self):  
        print("Human Speaking")    
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
d = Dog()  
d.bark()  
d.speak()  


# In[74]:


class Animal:  
    def speak(self):  
        print("Animal Speaking")   
class Dog(Animal):  
    def bark(self):   
        print("dog barking")  
class DogChild(Dog):  
    def eat(self):  
        print("Eating bread")  
d = DogChild()  
d.bark()  
d.speak()  
d.eat()  


# In[81]:


class Calculation1:  
    def sum(self,a,b):  
        return a+b;  
class Calculation2:  
    def multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def divide(self,a,b):  
        return a/b;  
d = Derived()  
print(d.sum(10,20))  
print(d.multiplication(10,20))  
print(d.divide(10,20)) 


# In[84]:


class Calculation1:  
    def sum(self,a,b):  
        return a+b;  
class Calculation2:  
    def multiplication (self,a,b):  
        return a*b;  
class obtained(Calculation1,Calculation2):  
    def divide(self,a,b):  
        return a/b;  
d = Derived()  
print(issubclass(obtained,Calculation1))  
print(issubclass(Calculation1,Calculation2))  


# In[85]:


class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
d = Derived()  
print(isinstance(d,Derived)) 


# In[86]:


class Bank:  
    def roi(self):  
        return 10;  
class SBI(Bank):  
    def roi(self):  
        return 7;  
class ICICI(Bank):  
    def roi(self):  
        return 8;  
b1 = Bank()  
b2 = SBI()  
b3 = ICICI()  
print("Bank Rate of interest:",b1.roi());  
print("SBI Rate of interest:",b2.roi());  
print("ICICI Rate of interest:",b3.roi()); 


# In[95]:


class Employee:  
    count = 0;  
    def __init__(self):  
        Employee.count = Employee.count+1    
emp = Employee()  
emp2 = Employee()
print("The number of employees:-",Employee.count) 


# In[3]:


class Employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name
    def display(self):
        print("Id: %d \nName: %s"%(self.id,self.name))
emp1= Employee('abc',11)
emp2= Employee('xyz',12)
emp1.display()
emp2.display()


# In[4]:


class Student:    
    count = 0    
    def __init__(self):    
        Student.count = Student.count + 1    
s1=Student()    
s2=Student()    
s3=Student()    
print("The number of students:",Student.count) 


# In[1]:


class Student:
    def __init__(self):
        print("This is non-parameterized constructor")
    def show(self,name):
        print("hello",name)
student=Student()
student.show("abc")


# In[17]:


class Employee:
    def __init__(self,designation,id,salary):
        self.designation= designation
        self.id= id
        self.salary= salary
a= Employee("hr", 1, 1000000)
print(getattr(a,"designation"))
setattr(a,"designation","manager")
print(getattr(a,"designation"))
setattr(a,"salary")


# In[6]:


from abc import ABC, abstractmethod   
class Car(ABC):   
    def mileage(self):   
        pass  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class Duster(Car):   
     def mileage(self):   
        print("The mileage is 24kmph ")    
class Renault(Car):   
    def mileage(self):   
        print("The mileage is 27kmph ") 
t= Tesla ()   
t.mileage()   
r = Renault()   
r.mileage()   
s = Suzuki()   
s.mileage()   
d = Duster()   
d.mileage()  


# In[1]:


from abc import ABC  
class Polygon(ABC):   
    def sides(self):   
        pass  
class Triangle(Polygon):  
    def sides(self):   
        print("triangle has 3 sides")   
class Pentagon(Polygon):    
    def sides(self):   
        print("pentagon has 5 sides")   
class Hexagon(Polygon):   
    def sides(self):   
        print("hexagon has 6 sides")   
class square(Polygon):
    def sides(self):   
        print("square have 4 sides")   
t = Triangle()   
t.sides()   
s = square()   
s.sides()    
p = Pentagon()   
p.sides()    
k = Hexagon()   
k.sides()   


# In[12]:


class A:  
    def display(self):  
        print("A IS FIRST ALPHABET ")    
class B(A):  
    def vision(self):  
        print("B IS SECOND ALPHABET ") 
class C(B):  
    def sight(self):  
        print("C IS THIRD ALPHABET ")  
d = C()
d.sight()
d.vision()  
d.display()  


# In[32]:


class Deposit:  
    def sight(self,b):  
        return b;  
class Withdraw:  
    def display(self,c):  
        return c;  
class Derived(Deposit,Withdraw):  
    def vision(self,a,b,c):  
        return a+b-c;  
d = Derived()  
print("opening balance:100000")
print("deposit:",d.sight(20000))  
print("withdraw:",d.display(10000))
print("balance:",d.vision(100000,20000,10000))


# In[13]:


class a:
    def d1(self):
        print("Hi")
class b(a):
    def d1(self):
        super().d1()
        print("Hello")
ob=b()
ob.d1()


# In[1]:


class obj:
    def display1(self,a,b):
        print(a+b)
    def display(self,a,b,c):
        print(a+b+c)
a=obj()
a.display1(2,2)
a.display(1,2,3)


# In[16]:


class Human:
    def sayhello(self,name=None):
        if name is not None:
            print("hello"+ name)
        else:
            print("hello")
obj=Human()
obj.sayhello()


# In[18]:


def my_func():
    x=10
    print("value inside function:",x)
x=20
my_func()
print("value outsude function:",x)


# In[19]:


x="hell"
def ob():
    print("x inside",x)
ob()
print("x outside",x)


# In[24]:


x="global"
def fyp():
    global x
    y="local"
    x=x*2
    print(x)
    print(y)
fyp()
    


# In[2]:


n=int(input("enter number:"))
a=n+1
b=a*n
z=b/2
if n>0:
    print(z)
else:
    print("n is not natural number")


# In[17]:


num=int(input("enter number:"))
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not natural  number")


# In[22]:


num=int(input("enter number:"))
if num>1 and num%2==0:
    print("number is even")
else:
    print("number is not even")


# In[21]:


def fb(N):
    a=0
    b=1
    print(a)
    print(b)
    for i in range (2,N+1):
        c=a+b
        a=b
        b=c
        print(c)
fb(int(input("NUM")))


# In[10]:


a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
if a>b and a>c:
    print("a is largest number")
elif b>c and b>a:
    print("b is largest number")
elif c>a and c>b:
    print("c is largest number")
else:
    (" minmum two number equal or all three")


# In[23]:


x = 10
y = 5
x = x + y
y = x - y
x = x - y
print("x =", x, " y =", y)


# In[24]:


x = 10
y = 5
z = x + y
y = z - y
x = z - y
print("x =", x, " y =", y)


# In[3]:


try:
    print(x)
except:
    print("an exception occured")


# In[4]:


try:
    print(x)


# In[11]:


try:
    print("hello")
except NameError:
    print("Something else is went wrong")
else:
    print("nothing went wrong")


# In[13]:


try:
    print(a)
except NameError:
    print("Something else is went wrong")
else:
    print("nothing went wrong")


# In[3]:


a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
d=[a,b,c]
try:
    print("second element=%d"%(d[1]))
    print("fourth element=%d"%(d[3]))
except:
    print("An error occurred ")


# In[5]:


def fun(a):
    if a<4:
        b=a/(a-3)
    print("value of b=",b)
try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("Zero divison error has error has occured and handled")
except NameError:
    print("Name error occured and handled")


# In[6]:


try:
    div=-4//0
    print(div)
except ZeroDivisionError:
    print("Attempting to divide zero")
finally:
    print("this is code of finally clause")
    


# In[10]:


try:
    raise NameError("hi there")
except NameError:
    print("an exception")    


# In[ ]:




