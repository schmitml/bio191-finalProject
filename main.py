# BIO191-finalProject
# Marc Schmitt, Chuck Alexa
import os

def main():
    file = 'script.txt'
    textMap = readScript(file)
    # for key in textMap:
    #     print(key)
    runPrompt(textMap)

def runPrompt(textMap):
    # clearPrompt()
    print("Welcome to Choose Your Development!\nLet's get started!\n")
    stop = False
    currentbloc = textMap['_first_']
    printBloc(currentbloc)
    while not stop:
        next = input("Which option?(Press q to quit)")
        if next == 'q':
            stop = True
        else:
           # print("Input: " + next + " Options: " + str(len(currentbloc)-1))
            print("\n")
            if int(next) >= len(currentbloc) or int(next) <= 0:
                print("Oops, that wasn't right.")
                continue
            currentbloc = getBloc(currentbloc[int(next)][0], textMap)
            if not currentbloc:
                print("The story ended!")
                return
            printBloc(currentbloc)

def getBloc(key, textMap):
    #print("Looking for: " + key)
    try:
        return textMap[key]
    except:
        return ""

def printBloc(bloc):
    print(bloc[0])
    for x in range(1, len(bloc)):
        print(str(x)+". "+bloc[x][1])

def clearPrompt():
    os.system('cls' if os.name=='nt' else 'clear')

# Takes the path to the script file(.txt)
# Parses a script into a dictionary
def readScript(path):
    lines = open(path).read().split('\n')
    values = {}
    index = 0
    while index < len(lines)-1:
        # Skip empty lines
        if not lines[index]:
            index += 1
            continue
        
        # Skip Comments
        if (lines[index][0] == '#'):
            index += 1
            continue
        # Read in Text Blocks
        elif (lines[index][0] == '+'):
            prompt = lines[index].replace('+', '').split('|')
            options = [prompt[1]]
            index += 1
            # Read in Options
            while lines[index] and index < len(lines) and lines[index][0] == '-':
                line = lines[index].replace('-', '').split('|')
                options.append(line)
                index += 1
            # Save Block
            values[prompt[0]] = options
            # print("Key: " + prompt[0] + " Options: " + str(values[prompt[0]]))
        else:
            index += 1
    return values

if __name__ == "__main__":
    main()