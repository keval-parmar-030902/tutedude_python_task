'''
################ Task1: Create a Dictionary of Student Marks ####################
'''
student_data = {'Alice':87, 'Keval':89, 'Joy':90}
try:
    student_name = input('Enter Student\'s name: ')
    print(f'{student_name}\'s is: {student_data[student_name]}')
except KeyError:
    print(f'{student_name} was not found in list')