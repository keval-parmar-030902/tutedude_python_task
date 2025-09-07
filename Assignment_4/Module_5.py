'''
################# Types of Errors ####################
'''

#1: Syntax Error
'''
a=2
if a<1:
    print('Hello')
else:
    print('Welcome')
'''  
#2: Indentation Error
'''
a=2
if a<1:
    print('Hello')
else:
print('Welcome')
'''

#3: Zero Division Error

# print(1/0)

#4: Module Error
'''
import mathamatics
print(mathamatics.pi)
'''

#5: Type Error
'''
a = 2
b = '5'
print(a+b)
'''

#6: Logic Error
'''
a = 2
b = 2
print(a * b) # here you can multiply by them with square method or a**2 method so it is an Logic Error.
'''

''' 
################ Exception Handling ########################
'''
try:
    a = 2
    b = 2
    print(a/b)
except ZeroDivisionError:
    print('There is an Error.')
finally:
    print('COntinue with follwing code.')
    
'''
############### Files IO ##################
'''
#1:
file1 = open('file1.txt','r')
# Directory specify the locations
# mode: ('r','w','a','r+')
file1.close()

#2:
with open('file1.txt' ,'w') as f:
    f.read()
    # Read and Write, Append content of file.