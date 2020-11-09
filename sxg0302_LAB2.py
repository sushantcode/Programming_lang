# Sushant Gupta
# 1001520302
# November 09, 2020

import os

# defining set of lambda functions for each each operator
operations = {
    "+": (lambda x, y: x + y),
    "-": (lambda x, y: x - y),
    "*": (lambda x, y: x * y),
    "/": (lambda x, y: x / y)}

# Function to process each line in the file
def execution(eachLine):
    # striping the trailing new line from each line of command
    line = eachLine.rstrip("\n")
    # Spliting each numbers and operators in the line and stroing in an array
    elementStack = line.split(" ")
    # An list(stack) to store all operands including intermediate one
    operandStack = []
    # Using for loop to process each element in the elementStack
    for item in elementStack:
        # Looking for an operator and when found poping two operands to pass to operations for execution
        if item in operations:
            # poping the operands
            operand1 = operandStack.pop()
            operand2 = operandStack.pop()
            # Storing intermediate results after performing operations on the operands
            interResult = operations[item](operand2, operand1)
            # pushing the intermediate result to the operandStack to be used in later operations
            operandStack.append(interResult)
        else:
            # Pushing the number(operands) to operandStack after casting to respective float value
            operandStack.append(float(item))
    # Checking if there is more or less than 1 element in the operandSTack left
    if len(operandStack) == 1:
        # Returning the final element as the result
        return operandStack[0]
    else:
        # If less or more than 1 element left, there must be something error in the input
        return "Something went wrong"

if __name__ == "__main__":
    # Opening the file in reading mode
    openedFile = open("input_RPN.txt", "r")
    # reading each line and storing in Lines array
    Lines = openedFile.readlines()
    # Creating list to store final output of each line
    resultStack = []
    # Iterating over each line to execute them
    for eachLine in Lines:
        # Getting result of each line from execution function
        result = execution(eachLine)
        # pushing the results in the resultStack to print later
        resultStack.append(result)
    # Iterating over the resultStack and printing each result in new line
    for eachResult in resultStack:
        print(eachResult)