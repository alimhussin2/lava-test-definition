#!/usr/bin/python3
print("hello world!")

# function

def printme():
	me='this print passes the function'
	print(me)
	return


# just another function pass by references
def changeme(mylist):
	mylist = [1,2,3,4]
	print('values inside the functiom: ', mylist)
	return
def printinfo(name, age):
	print('Name: ', name)
	print('Age: ', age)
	return

# Variables
counter = 100	# integer
miles = 100.0	# floating point
name = "alim"	# a string

print (counter)
print  (miles)
print (name) 

#if statement
print("\nThis is if statement section\n")

var = 0
var =int(input("Give any value: "))
if (var > 100):
	print ("Your value is high")
elif (var > 120):
	print("Your value is too high")
elif (var < 100):
	print ("Your value is low")
elif (var < 80):
	print ("Your value is too low")
else:
	print("You got it right")

print("\n\nThis is out of if statement")

# while loop

print("\n\nWHILE LOOP\n")

print("We are out of WHILE LOOP")
range (0,5)

for letter in 'Python3':
        print('current letter:', letter)
print()
fruits = ['banana', 'apple', 'mango', 'papaya'] # list datatype
for fruit in fruits:
        print('Current fruit: ', fruit)

# else statements with for loop
# execute else statement after loop if no condition meet

numbers = [11,33,55,39,75,37,21,23,41,13, 12]
for num in numbers:
	if (num %2 == 0):
		print('the list contains an even number')
		break
else:
	print('the list doesnt contain even number')

printme()
mylist = [10,20,30,40]
changeme(mylist)
print('value outside the function: ', mylist)
print('Calculate something...')
name=input('Who are you?>> ')
age=input('How old are you? >> ')
printinfo(name, age)
