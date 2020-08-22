import re
greet= """


        ___ ___   ____  ___           _      ____  ____           ____   ____  ___ ___    ___
        |   T   T /    T|   \         | T    l    j|    \         /    T /    T|   T   T  /  _]
        | _   _ |Y  o  ||    \  _____ | |     |  T |  o  ) _____ Y   __jY  o  || _   _ | /  [_
        |  \_/  ||     ||  D  Y|     || l___  |  | |     T|     ||  T  ||     ||  \_/  |Y    _]
        |   |   ||  _  ||     |l_____j|     T |  | |  O  |l_____j|  l_ ||  _  ||   |   ||   [_
        |   |   ||  |  ||     |       |     | j  l |     |       |     ||  |  ||   |   ||     T
        l___j___jl__j__jl_____j       l_____j|____jl_____j       l___,_jl__j__jl___j___jl_____j
        ---------------------------------------------------------------------------------------
        Mad Libs is a phrasal template word game where one player prompts others for a list of
        words to substitute for blanks in a story before reading aloud.

"""

print(greet)

def readFile():
    with open('./assets/story.txt') as file:
       contents = file.read()
       print(contents)
    return contents

def inputs(file):
    madlibs=[]
    grammer=[]
    regex =r"({\w+ ?\w+'? ?\w+ ?\w+'?\w ?([0-9]-[0-9]+)?})+"
    grammer += re.findall(regex, file)
    for i in grammer:
        madlibs.append(i[0].translate({ord(i): None for i in '{}'}))
    return madlibs

def write(contents,inputs,madlibs):

    regex = r"({\w+ ?\w+'? ?\w+ ?\w+'?\w ?([0-9]-[0-9]+)?})+"

    for i in madlibs:
        replace_words = (re.sub(regex,'%s', contents))
    return replace_words% tuple(inputs)

if __name__ == "__main__":
    x = readFile()
    inputs(x)
    write(madlibs)





