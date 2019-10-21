from selenium import webdriver
name = "Roman"
height = 180
weight = 83.5
married = False
age = 65

height = height + 6
height += 6


a = 4
b = 6.5
c = "2.5"

print (weight + height)
print (name + str(height))
print (name + " is " + str(height) + " cm and " + str(weight) + " kg")
print ("My name is " + name)
print ("name is {} and height is {}". format(name, height))

print (a+b)

print(b + float(c))
print(str(b) +c)

if (age < 10):
    print("child")
elif (age <= 19):
    if (age < 13):
        print ("small")
    print("teenager")
elif (age < 65):
    print ("old")
else:
    print("retiree")

lis = [12, 44.3, 'a', ['h', 'i']]

lis.append('new')

lis.insert(1, 14)
lis.remove(44.3)

print(lis)
print(lis[3])
print(lis[3][0])

set = {'Alex', 12, 12, 'Peter', 'Nick'}

print(set)

set = ('Alex', 12, 12, 'Peter', 'Nick'
print(set)

for element in lis:
    print(element)

d = {'name': name, 'profession': {3, 2, 3}, 'name1': 'bcd', 'name2': 'hi', 'name3': 'hi'}
print(d['name'])
print(d['profession'])


def sum(a, b):
    # a = 4
    # b = 3
    print(a + b)


sum(weight, height)
sum(weight+height, height-weight)

import math
pi = math.pi
c = math.cos(60/pi)

print(c)
print(pi)
#about xpath
#//input[@name='username']
# contains text: //button[contains(test(),"Submit")]   //div[contains(test(),"Submit")]
#

#for element in set:
#    print(element)

print(len(set))
print(set)
print(len(lis))
print(lis)



