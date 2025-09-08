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

## Assignment 4:

### Task1:

Handling the error in files and i found this output from there.

first, I use try for the Error handling and there i use with operatir with open for retrive data from the file sample.txt the i get this output.

Reading file content:   
Line: This is a simple text file.

Line: It contains multiple lines. 

Here i attached the sample.txt path: ‘tutedude\_python\_task\\Assignment\_4\\sample.txt’

### Task2:

Step1: Firstly, I take input from the user.

Step2: then i created an file output.txt with open function for file handaling and i give the user string to it so it can write the in output.txt and i use mode ‘w’.

Step3: then I print the Data was successfully enterd in the output.txt file.

Step4: After that i again use take user input for additional data addition. 

Step5: with open file for append the data in output.txt file.

Step6: print data succesfully append in file.

Step7:Read the file of both lines of data appended in output.txt

Here i attched output.txt path: ‘tutedude\_python\_task\\Assignment\_4\\output.txt’

## Assignment 5:

### Task1: Create a Dictionary of Student Marks

Frist of all I created an dictionary then I use try except block for error handling.

### Task2: Demonstrate List Slicing

Step1: For list i use List comprehension to create an list.

Step2: Then i use slicing method to slice to 1 to 5 elements.

Step3: After that I assign a new variable to store that another list.

Step4: Then i provide an slicing to themto reverse the list.