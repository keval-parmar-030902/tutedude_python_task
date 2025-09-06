'''
Using factorial used in Recursion 
factorial(1) = 1
factorial(2) = 2 * 1
factorial(3) = 3 * 2 * 1
    .
    .
factorial(n) = n * ..... 3 * 2 * 1
factorial(n) = n * n-1 * ..... 3 * 2 * 1
factorial(n) = n * (n-1 * ..... 3 * 2 * 1)
factorial(n) = n * factorial(n-1)
'''
# How Recurion work here:

# factorial(5)  -> function call
#   /   \
#  5 * factorial(4)
#      /  \
#  5 * 4 * factorial(3)
#           /  \ 
#  5 * 4 * 3 * factorial(2)
#               /  \   
#  5 * 4 * 3 * 2 * factorial(1)  ## Checked condition and it's return 1 return 1
#                  |   
#  5 * 4 * 3 * 2 * 1 
#  return 120 as final answer

    
def factorial(num):                                  
    if(num==1):
        return 1
    return num * factorial(num-1)

number = int(input('Enter the Factorial: '))

print(f'Factorial of {number} is : {factorial(number)}')