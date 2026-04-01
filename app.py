# Variable
# What is a variable. A variable is a container that is used to store informations.
# If you must store information in the ram, then you must have to declare a variable.
#  e.g
name = "i am joy"
print(name)

# A Dictionary is a collection of key pair values.
obj = {
"Username": "Julius Sarah",
"Email": "juliusarah237@gmail.com",
"PhoneNumber": "09045831170"
}
print(obj)
# Accessing values in python.
print(obj)
print(obj["Username"])
print(obj["Email"])
print(obj["PhoneNumber"])


obj2 = {
"Username": "Emmanuel",
"Email": "emmanuel237@gmail.com",
"PhoneNumber": "08044444674"
}
print(obj2)

# Accessing values in python.
print(obj2)
print(obj2["Username"])
print(obj2["Email"])
print(obj2["PhoneNumber"])


# A List allows us to store sequence of mutiple values. This data type are mutable :
#  Meaning the can be modify after been created. However, values that cannot be modify after 
# been created are called immutable. e.g tuple.

Username = ["kale", "Sarah", "Goerge", "Anderson", "Victory"]
print(len(Username))
Username.append('gloria')
print(Username)

Username.insert(2,"Amaka")
print(Username)

print(Username[0])

print(Username[1])

print(print(Username[2]))

print(Username[3])

print(Username[4])



phnonenumber = ["09045888888", "60099999993", "66555555555", "5666666666666", "45566767766666767", "566777766767667",
"566556656556565"]
print(phnonenumber)
print(phnonenumber[0])
print(phnonenumber[1])
print(phnonenumber[2])
print(phnonenumber[3])
print(phnonenumber[4])
print(phnonenumber[5])
print(phnonenumber[6])
print(len(phnonenumber))
# Comparisoning Operator: This are operators that allows you to compair two operands and return one value. This will 
# offen always return a boolen value. e.g
# == (equality operator)
# < (less than operator)
# > (greater than operator)
# >= (greater or equate)
# <= (less than or equates)
# != (Not equates)
print(2==2)
print(7<5)
print(10>11)
print(15<=15)


print(5!=2)
print(30>=2)
print(30<=2)

# if statement is an action that is excuted base on certain condition.
age = 19
name = "Martha"
if name == "Emmanuel":
   print(f'{name} You Welcome')


# elif is an optional clause so that if the if clause doesn't return through the the elif is going to return through.
elif  name == "Martha":
    print(f'{name} Although We Need Sarah But You Are An Option')




# else statement is part of the if statement. else is a placeholder that will be excuted if the if block statement
# is not true.

else:
    print("You are not Welcome")


# forloop is use to iterate or loop over certain value.
fruit = [ "Apple", "Mango", "Orange", "Grape", "Banana"]


for i in fruit:
    print(i)

    student = ["Blessing", "Sarah", "Grace", "Dinma", "Ogechi", "Joy"]
    for s in student:
        print(s)


 # functions are block of codes that is meant to do a single task. The are used as a mechanism to make a certain 
 # code reusable. to define a function in python you have to start with the word def.

def greetMe(name):
    

    print(f'how are you')

greetMe('Sarah')



def sum(num1,num2):
    print(num1-num2)
sum(55,5)



def janeJames(day1,day2):
    print(day1+day2)
janeJames(8,2)
janeJames(4,4)







# Environment Variable? help us to create an eyesolated environment for your application run time.
# pip install (A python packages used to install or dependences in our application).(Virtual Env)
# Any package you wnat to  install just say:(pip install.......(the appplication name)).

# To activate my virtual environment: sarah/Scripts/Activate.ps1