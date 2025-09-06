## Assignment 3:

### Task1:

'''

Using factorial used in Recursion

factorial(1) = 1

factorial(2) = 2 \* 1

factorial(3) = 3 \* 2 \* 1

    .

    .

factorial(n) = n \* ..... 3 \* 2 \* 1

factorial(n) = n \* n-1 \* ..... 3 \* 2 \* 1

factorial(n) = n \* (n-1 \* ..... 3 \* 2 \* 1)

factorial(n) = n \* factorial(n-1)

'''

\# How Recurion work here:

\# factorial(5)  -> function call

\#   /   \\

\#  5 \* factorial(4)

\#      /  \\

\#  5 \* 4 \* factorial(3)

\#           /  \\

\#  5 \* 4 \* 3 \* factorial(2)

\#               /  \\  

\#  5 \* 4 \* 3 \* 2 \* factorial(1)  ## Checked condition and it's return 1 return 1

\#                  |  

\#  5 \* 4 \* 3 \* 2 \* 1

\#  return 120 as final answer

### Task2:

By using math library we can use several math property like squer root, log and trignomatery formula for easy mathamatics.

import math

math.sqrt(number)

math.log(number)

math.sin(number)