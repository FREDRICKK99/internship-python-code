# s = "If Comrade Napoleon says it, it must be right."
# a = [100, 200,300]

# def foo(arg):
#     print(f "arg = {arg}")

# class Foo:
#   pass

# import mod
# print mod.s

# greeting = input("Hello")
# name = "Fred"
# print(greeting)

# age = input("How old are you?")
# age = int(age)
# print(age

# n = int(input())
# for i in range (1, n+1):
#   print(i, end ="")

age = 24
greeting = "Bruce"
print(greeting , age)

parrot = "Norwegian Blue"
print(parrot)
# print(parrot[30])
print(parrot[3])
print(parrot[-1])
print(parrot[0])
print(parrot[0:6])
print(parrot[:6])
print(parrot[6:])
print(parrot[-4:2])
print(parrot[0:6:2])

number ="9,223,372,036,854,775,807"
print(number[1::4])      #we are returning the whole string, skipping three elements, begining with index 1
 
numbers="1, 2, 3, 4, 5, 6, 7, 8, 9" 
print(numbers[0::3])

string1= " he's "
string2="probably "
print(string1+" "+string2)
print(string1 + string2)

print("he's " "probably " "pining ")

print("Hello " * 5)
# print("Hello " * 5 + 4)
print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

# string is a sub string of another returning true or false

today="friday"
print("day" in today)
print("fri" in today)
print("thur" in today)
print("parrot" in today)


# formatting strings in python
age = 24
print("My age is " + str(age) + " years")


#replacemenrt field

print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7} ".format(31, "January", "March", "May", "July", "August", "October", "Dececmber"))

print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30 , 31))

print("My age is %d years" %age)

print("My age is %d %s, %d %s" %(age, "years", 6, "months")