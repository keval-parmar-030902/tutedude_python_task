'''
################ Task2:  Demonstrate List Slicing ####################
'''
l = [x for x in range(1,11)] # lisr Comprehension

print('Original list: ',l)
new_l = l[:5] # Here we can't change directly to the list so we need a small copy of it and we need to assign new variable list for only access the 5 elements.
print('Extracted list: ',new_l)
print('Reversed list: ',new_l[::-1]) #  for this we can revers the list with out inbuilt function.