import sys
import re
import os


def main():

    # check command line args for -f flag, indicating file input, or -c flag for command line input
    # default case (no flag): command line input
    if len(sys.argv) == 1:
        fileFlag = False
    # flag but no filename: assume command line input or provide usage
    elif len(sys.argv) == 2:
        if sys.argv[1] == "-c":
            fileFlag = False
        else:
            print("usage: morse.py [-c] [-f filename]\n")
            return 1
    # 3+ args: assume file input or provide usage
    else:
        if sys.argv[1] == "-f":
            fileFlag = True
            inFilename = sys.argv[2]
        else:
            print("usage: morse.py [-c] [-f filename]\n")
            return 1

    # from a file
    if fileFlag:
        # check proper filename extension
        if not inFilename.endswith(".txt"):
            print("Please provide a text file.\n")
            return 2
        # make sure it actually exists
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        if not os.path.exists(os.path.join(__location__, inFilename)):
            print("The file " + sys.argv[2] + " does not exist.\n")
            return 2

        # create an output file; just append "_out" to the input filename
        outFilename = inFilename.rstrip(".txt") + "_out" + ".txt"

        inFile = open(os.path.join(__location__, inFilename), "rt")
        outFile = open(os.path.join(__location__, outFilename), "wt")

        lines = inFile.readlines()
        for line in lines:
            outString = translate(line)
            outFile.write(outString)

        inFile.close()
        outFile.close()

        return 0

    # input from command line
    else:
        while True:
            content = input("What would you like to translate? Enter 'quit' to quit.\n")
            if content == "quit":
                break
            print(translate(content))

    # print(translate("  ".join(sys.argv[1:])))
    return 0


# translate(): determine whether we are translating from or to morse
# in:  String sentence
# out: String output
def translate(sentence):
    # turn our array of words into a string, if applicable
    # print(sentence)
    # sentence = " ".join(sentence)
    # print(sentence)

    # check for english characters, numbers, and spaces
    if any(letter.isalnum() for letter in sentence):
        return trans_to(sentence)

    # if there aren't english characters, assume morse
    # we could alternatively check for dots and dashes, but we already
    # ignore anything that we don't expect in the trans_from() function
    else:
        return trans_from(sentence)


# translate from english characters to morse
# in:  String sentence
# out: String output
def trans_to(sentence):
    outString = []
    for letter in sentence:
        if letter in toMorse:
            outString.append(toMorse[letter])
        # ignore anything we don't expect
        else:
            continue
    # there's a space at the beginning of each new line, so let's remove that and return as a string
    return ("".join(outString)).replace("\n ", "\n")


# translate from morse to english characters
# in:  String sentence
# out: String output
def trans_from(sentence):
    outString = []
    for letter in re.split("(\s+)", sentence):
        if letter in fromMorse:
            # print(letter + ":  " + int(letter))
            outString.append(fromMorse[letter])
        # ignore anything we don't expect
        else:
            continue
    return "".join(outString)


# dictionary for english characters --> morse characters
toMorse = {
    'a' : '.- ',
    'b' : '-... ',
    'c' : '-.-. ',
    'd' : '-.. ',
    'e' : '. ',
    'f' : '..-. ',
    'g' : '--. ',
    'h' : '.... ',
    'i' : '.. ',
    'j' : '.--- ',
    'k' : '-.- ',
    'l' : '.-.. ',
    'm' : '-- ',
    'n' : '-. ',
    'o' : '--- ',
    'p' : '.--. ',
    'q' : '--.- ',
    'r' : '.-. ',
    's' : '... ',
    't' : '- ',
    'u' : '..- ',
    'v' : '...- ',
    'w' : '.-- ',
    'x' : '-..- ',
    'y' : '-.-- ',
    'z' : '--.. ',
    '1' : '.---- ',
    '2' : '..--- ',
    '3' : '...-- ',
    '4' : '....- ',
    '5' : '..... ',
    '6' : '-.... ',
    '7' : '--... ',
    '8' : '---.. ',
    '9' : '----. ',
    '0' : '----- ',
    '.' : '\n',
    ' ' : ' '
}

# dictionary for morse characters --> english characters
fromMorse = {
    '.-'    :  'a',
    '-...'  :  'b',
    '-.-.'  :  'c',
    '-..'   :  'd',
    '.'     :  'e',
    '..-.'  :  'f',
    '--.'   :  'g',
    '....'  :  'h',
    '..'    :  'i',
    '.---'  :  'j',
    '-.-'   :  'k',
    '.-..'  :  'l',
    '--'    :  'm',
    '-.'    :  'n',
    '---'   :  'o',
    '.--.'  :  'p',
    '--.-'  :  'q',
    '.-.'   :  'r',
    '...'   :  's',
    '-'     :  't',
    '..-'   :  'u',
    '...-'  :  'v',
    '.--'   :  'w',
    '-..-'  :  'x',
    '-.--'  :  'y',
    '--..'  :  'z',
    '.----' :  '1',
    '..---' :  '2',
    '...--' :  '3',
    '....-' :  '4',
    '.....' :  '5',
    '-....' :  '6',
    '--...' :  '7',
    '---..' :  '8',
    '----.' :  '9',
    '-----' :  '0',
    '.-.-.-':  '.',
    ''      :  '. ',
    '--..--':  ',',
    '  '    :  ' ',
    '/'     :  ' '
}

if __name__ == '__main__':
    main()