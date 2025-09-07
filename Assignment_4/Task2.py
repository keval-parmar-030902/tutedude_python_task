
text = input('Enter text to write to the file: ')
with open('Assignment_4/output.txt', 'w') as f:
    f.write(text + '\n')
print('Data successfully written to output.txt\n')

additional_data = input('Enter additional data to append: ')
with open('Assignment_4/output.txt', 'a') as f:
    f.write(additional_data+ '\n')
print('Data successfully appended.\n')

print('Final content of output.txt')
with open('Assignment_4/output.txt') as f:
    print(f.readline())
    print(f.readline())
