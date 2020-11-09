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
def execution(elementStack):
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

def parseToRPN(eachLine):
    # striping the trailing new line from each line of command
    line = eachLine.rstrip("\n")
    # Spliting each numbers and operators in the line and storing in an list
    elementStack = line.split(" ")
    # A list to store all operators in the expression
    operatorStack = []
    # Defing list or stack to store final RPN
    rpnStack = []
    for item in elementStack:
        # inspecting each elements in the expression and taking action accordingly
        # if the element in the expression is an operator, store in operator stack
        if item in operations:
            operatorStack.append(item)
        # if the element is parenthesis, don't store
        elif item in ["(", ")"]:
            # if the element is closing parenthesis, push the operators to RPN
            if item == ")" :
                # making sure if the operator stack is not empty
                if len(operatorStack) > 0:
                    # pushing all operators to RPN stack after poping from operator stack
                    while operatorStack:
                        tempOp = operatorStack.pop()
                        rpnStack.append(tempOp)
        # if nothing, it is a number and go to rpn stack
        else:
            rpnStack.append(item)
    
    # making sure if the operator stack is not empty
    # if no parenthesis at all in the expression, this push back the operators to RPN stack
    if len(operatorStack) > 0:
        while operatorStack:
            tempOp = operatorStack.pop()
            rpnStack.append(tempOp)
    # returning the final rpn stack
    return rpnStack

if __name__ == "__main__":
    # Opening the file in reading mode
    openedFile = open("input_RPN_EC.txt", "r")
    
    # reading each line and storing in Lines array
    Lines = openedFile.readlines()
    # Creating list to store RPN output
    rpnStack = []
    # Creating list to store final output of each line
    resultStack = []
    # Iterating over each line to execute them
    for eachLine in Lines:
        # Getting rpn result for each line calling parseToRPN function
        rpnResult = parseToRPN(eachLine)
        # pushing the rpn results in the rpnStack to print later
        rpnStack.append(rpnResult)
        # Passing rpn result to do execution and get result
        result = execution(rpnResult)
        # pushing the results in the resultStack to print later
        resultStack.append(result)

    # Iterating over the rpnStack and printing each rpn in new line
    for eachRPN in rpnStack:
        # creating string to store all rpn elements in single element to print
        rpnStr = ""
        for element in eachRPN:
            # concatenating all elements in the each rpn from rpnStack
            rpnStr = rpnStr + element + " "
        print(rpnStr)
    # Iterating over the resultStack and printing each result in new line
    for eachResult in resultStack:
        print(eachResult)