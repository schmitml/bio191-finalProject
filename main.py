# BIO191-finalProject
# Marc Schmitt, Chuck Alexa

def main():
    file = 'script.txt'
    readScript(file)

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
            prompt = lines[index][1:]
            options = []
            index += 1
            # Read in Options
            while lines[index] and index < len(lines) and lines[index][0] == '-':
                line = lines[index].replace('-', '').split('|')
                options.append(line)
                index += 1
            # Save Block
            values[prompt] = options
            print("Key: " + prompt + " Options: " + str(values[prompt]))
        else:
            index += 1

if __name__ == "__main__":
    main()