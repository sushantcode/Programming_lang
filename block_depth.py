# Sushant Gupta
# 1001520302
# November 09, 2020

def isCommented(line):
    slashOn = 0
    for eachChar in line:
        if eachChar == '/' and slashOn == 0:
            slashOn = 1
        elif eachChar == '/' and slashOn == 1:
            break
        else:
            slashOn = 0
    return slashOn

if __name__ == "__main__":

    # Iterating over each line to execute them
    with open("input.txt", "r") as readFile:
        with open("output.txt", "w+") as writeFile:
            depth = 0
            for eachLine in readFile:
                isClosing = 0
                if isCommented(eachLine) == 0:
                    isInQuote = 0
                    for eachChar in eachLine:
                        if eachChar == '"' and isInQuote == 0:
                            isInQuote = 1
                        elif eachChar == '"' and isInQuote == 1:
                            isInQuote = 0
                        elif eachChar == '{' and isInQuote == 0:
                            depth += 1
                        elif eachChar == '}' and isInQuote == 0:
                            isClosing = 1
                eachLine = str(depth) + " " + eachLine[0:]
                if isClosing == 1:
                    depth -= 1
                    isClosing = 0
                # writeFile.write(eachLine)
                print(eachLine)