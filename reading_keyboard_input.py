# Información extraida desde Curso de Python de Microsoft
# https://learn.microsoft.com/en-us/training/modules/intro-to-python


# User input

name = input('Enter your name:')
print(name)


# call the input function without a parameter

print('What is your name?')
name = input()
print(name)

# Reading numbers as input

# this code and entering the value '5' would display <class 'str'>
x = input('Enter a number: ')
print(type(x))


# Turn the value into a true integer variable, you can use the int() function
x = int(input('Enter a number: '))
print(type(x))


# Converting numbers to strings - str() function

x = 5
print('The number is ' + str(x))

# Solicita 2 números y luego los suma

first_number = int(input('Type the first number: ')) ;\
second_number = int(input('Type the second number: ')) ;\
print("The sum is: ", first_number + second_number)