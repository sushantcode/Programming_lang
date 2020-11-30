# Sushant Gupta
# 1001520302
# November 30, 2020


# Function to check if the line is commented. return 1 if commented else 0
def isCommented(line):
    # Variable to keep track of / in the line
    slashOn = 0
    for eachChar in line:
        # slashOn is set to 1(true) whenever found first /. If secon consecutive / is
        # found the loop breaks and return 1, else the slashOn is set back to false
        if eachChar == '/' and slashOn == 0:
            slashOn = 1
        elif eachChar == '/' and slashOn == 1:
            break
        else:
            slashOn = 0
    return slashOn

if __name__ == "__main__":
    # Opening file in read mode
    with open("input.txt", "r") as readFile:
        # initializing the block depth level counter
        depth = 0
        # iterating over each line in the file
        for eachLine in readFile:
            # Status checker for whether there is block closing tag
            isClosing = 0
            # If line is not commented check each character and perform task accordingly
            if isCommented(eachLine) == 0:
                # Status checker for whether there is double quotes
                isInQuote = 0
                for eachChar in eachLine:
                    # If there is double quotes is found, set isInquote on and if the second
                    # quote is found set isInQuote to off. depth is immediately increased if
                    # characters are not in double quotes. If closing curing brace is found isClosing 
                    # sets to on(true)
                    if eachChar == '"' and isInQuote == 0:
                        isInQuote = 1
                    elif eachChar == '"' and isInQuote == 1:
                        isInQuote = 0
                    elif eachChar == '{' and isInQuote == 0:
                        depth += 1
                    elif eachChar == '}' and isInQuote == 0:
                        isClosing = 1
            # eachLine is modified to add the depth string
            eachLine = str(depth) + " " + eachLine[0:]
            # the depth counter is decreased and isClosing tracker is set back to false.
            if isClosing == 1:
                depth -= 1
                isClosing = 0
            # the line is printed with depth counter
            print(eachLine)