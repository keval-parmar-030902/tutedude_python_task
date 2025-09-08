# List ---> [], index value
# list = [1,2,3,4,5,5,6,7]

# dictionary ---> {}, Key: Value pair
# dictionary = {key:value, key:value}

# my_dict = {'key1': 1, 'key2': 2, 'key3': [3], 'key4': (4), 'key5': 5}
# print(my_dict['key3'])

# dictionary = {1: 'a', 2: 'b', 3:'c'}
# print(dictionary)

# animal = {'a': 'apple', 'b': 'ball', 'c': 'cat', 'd': 'dog'}
# animal['e'] = 'elephant'
# print(animal)

# print(animal.keys())
# print(animal.values())
# print(animal.get('g', 'g not found'))

'''
################## LIST ####################
'''

# number = [1, 2, 3, 4, 5, 6]
# #         0  1  2  3  4  5   forward
# #        -6 -5 -4 -3 -2 -1   Reverse

# print(number[2])

# list1 = ['mike', 10.1, 1988]
# list2 = ['Pop', 1]
# print(list1 + list2)

# a = ['disco', 10.019301, 1991839488] # LIST ARE MUTABLE
# a[0] = 'hardword'
# print(a)

# n = [1,2,3]
# print(n * 3)

# game = ['football', 'chess', 'basketball']
# print('Cricket' in game)

'''
##################### LIST FUNCTIONS #########################
'''

list1 = [10.1, 1988, 10, 12]
# list1.append(10)   # Only one element at a time.
# print(list1)

# list1.extend([10,1]) # multiple element at a time.
# print(list1)

# list1.remove(10.1)   # Remove the entered elements from the list.
# print(list1)

# del list1[0]         # Remove multiple elements from the list.
# print(list1)

# list1.clear()        # clear all the elements from the list.
# print(list1)

# list1.pop(2)        # remove or delete(pop) the indexed element from the list.
# print(list1)

# list1.insert(2,'pop')  # insert out desire element with our desire index in the list.
# print(list1)

# list1.sort()           # sort the list in the acsending order.
# print(list1)

# list1.reverse()          # it can reverse the list
# print(list1)

# list1.index(1988)          # we can get in index value of element.
# print(list1)

# print(len(list1))               # total number of elements
# print(list1)

'''
######################### LIST SLICING ########################
'''

# numbers = [10, 20, 30, 40, 50, 60, 70]
# #           0   1   2   3   4   5   6

# #numbers[start:end+1:interval]
# #Get 10-50
# #numbers[0:4+1]
# print(numbers[0:4+1])

'''
##################### LIST COMPERIHENSION ####################
'''

# x = []
# for i in range(11):
#     z = i**2
#     x.append(z)
# print(x)

# # list comprehension

# x = [i**2 for i in range(11)] # we write 2 lines of code instead of 5.
# print(x)

# x = []
# for i in range(11):
#     if i%2==0:
#         z = i**2
#         x.append(z)
# print(x)

# # list comprehension

# x = [i**2 for i in range(11) if i%2==0] # we write 2 lines of code instead of 5.
# print(x)

'''
##################### SETS ##########################
'''

# Type of the collections
# immutables
# Unique elements

set2 = {}

# set1 = {1,2,3,4,5,6,7}
# print(set1)

# print(type(set1)) # <class 'set'>
# print(type(set2)) # <class 'dict'>

# set1 = {1,2,2,4,5,6,7} # print only unique elements.
# print(set1)

# set1 = {1,2,3,4,5,6,7}
# set1.add(8)              # add element at the end

# print(set1)

# set1 = {1,2,3,4,5,6,7}
# set1.remove(3)              # add element at the end

# print(set1)

# set1 = {1,2,3,4,5,7}
# set2 = {3,5,6,7,8}

# # Intersection of the sets.
# print(set1 & set2)   #{3, 5, 7}  
  
# set1 = {1,2,3,4,5,7}
# set2 = {3,5,6,7,8}

# # Union of the sets.
# print(set1.union(set2))   #{1, 2, 4, 5, 6, 7, 8}   
 
# set1 = {1,2,3,4,5,7}
# set2 = {3,5,7}

# # Union of the sets.
# print(set2.issubset(set1))   #Return bool as True    

'''
###################### String Functions ###################
'''

# a = 'kevaL pArMar'
# b = 'A'
# c = '8' 
# print(a.capitalize()) # capitalize the first character of the string.

# print(a.upper())      # It can convert the all character to the upper case.

# print(a.lower())      # It can convert the all character to the lower case.

# print(c.isnumeric())  # It can check whether thr number is numeric or not in this case it's return the truth.

# print(b.isalpha())    # It can check whether thr number is alphabatic or not in this case it's return the truth.

# string = 'Keval is an good listner.'
# #         0123456789012
# print(string.startswith('Keval')) # It's return bool value if there is an word or character starting with it.

# print(string.endswith('listner.')) # It's return bool value if there is an word or character ending with it.

# print(string.replace('Keval', 'Nike')) # It can replace the word that in the string.

# print(string.find('g')) # find the index of the character/word and return thr index number.

# string2 = 'Mike is good boy.'
# print(string2)
# print(string2.lstrip()) # It's remove thr leftside of the spaces in the string

# print(string2.rstrip()) # It's remove thr rightside of the spaces in the string

# print(string2.split()) # It can split from the spaces and return the words of list

# print(string2.splitlines()) # It can splitline and return the sentence of list

# a = 'Mike','Nick'
# print(','.join(a))

'''
################### String formatting ####################
'''

# name = 'Keval'
# number = len(name)*3

# print('Hello {}, your lucky number is {}'.format(name,number))

# example = 'format() example'
# string = 'This is an example of the {} on string'.format(example)
# print(string)

'''
################### Tuple ########################
'''

# tuple1 = (1,2,3,4,5,6)
# print(tuple1)
# # tuple1[1] = 1 # tuples are immutable
# print(tuple1[1])

# # string = ('Mike', 10.1, 1988)
# string = (4, 10.1, 1988, 1)
# print(len(string))

# print(string.count('Mike'))

# print(string.index(1988))

# print(sorted(string))
