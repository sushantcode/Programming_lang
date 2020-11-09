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

def parseToRPN(eachLine):
    # striping the trailing new line from each line of command
    line = eachLine.rstrip("\n")
    # Spliting each numbers and operators in the line and stroing in an array
    elementStack = line.split(" ")
    operatorStack = []
    rpnStack = []
    for item in elementStack:
        # Looking for an operator and when found poping two operands to pass to operations for execution
        if item in operations:
            operatorStack.append(item)
        elif item in ["(", ")"]:
            if item == ")" :
                if len(operatorStack) > 0:
                    for op in operatorStack:
                        tempOp = operatorStack.pop()
                        rpnStack.append(tempOp)
        else:
            rpnStack.append(item)
    
    if len(operatorStack) > 0:
        for op in operatorStack:
            tempOp = operatorStack.pop()
            rpnStack.append(tempOp)
    return rpnStack

if __name__ == "__main__":
    # Opening the file in reading mode
    openedFile = open("input_RPN.txt", "r")
    
    # reading each line and storing in Lines array
    Lines = openedFile.readlines()
    # Creating array to store final output of each line
    resultStack = []
    # Iterating over each line to execute them
    for eachLine in Lines:
        # Getting result of each line from execution function
        result = parseToRPN(eachLine)
        # pushing the results in the resultStack to print later
        resultStack.append(result)
    # Iterating over the resultStack and printing each result in new line
    for eachResult in resultStack:
        print(eachResult)