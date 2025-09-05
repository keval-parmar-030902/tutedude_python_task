operand_1 = int(input("Enter Operand 1 : "))
operand_2 = int(input("Enter Operand 2 : "))
operator = input("Enter the Operator (+, -, *, /, //, %, **): ")

if operator == "+":
    print(f'the Addition is: {operand_1 + operand_2}')
elif operator == "-":
    print(f'the Substraction is: {operand_1 - operand_2}')
elif operator == "*":
    print(f'the Multiplication is: {operand_1 * operand_2}')
elif operator == "/":
    if(operand_2 == 0):
        print("Zero Error...")
    else:    
        print(f'the Division is: {operand_1 / operand_2}')
elif operator == "//":
    if(operand_2 == 0):
        print("Zero Error...")
    else:
        print(f'the Floor Division is: {operand_1 // operand_2}')
elif operator == '%':
    print(f'the Modulo Division (remainder) is: {operand_1 % operand_2}')
elif operator == '**':
    print(f'the {operand_1} rest to {operand_2} is: {operand_1 ** operand_2}')