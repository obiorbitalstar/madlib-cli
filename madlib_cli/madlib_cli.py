import re

def readFile():
    with open('./assets/story.txt') as file:
       contents = file.read()
       print(contents)
    return contents

madlibs=[]
def inputs(file):
    grammer=[]
    regex =(r"(?<={)[\w'<>' -]+(?=})")
    grammer += re.findall(regex, file)
    for i in grammer:
        madlibs.append(input(f'{i} '))
    return madlibs

def write(madlibs):
    with open('../assets/story.txt') as template:
        fileToAlter = template.read()
    for i in range(20):
        start = fileToAlter.find("{")
        end = fileToAlter.find("}") + 1
        fileToAlter = fileToAlter[:start] + madlibs[i] + fileToAlter[end:]
    print(fileToAlter)

if __name__ == "__main__":
    x = readFile()
    inputs(x)
    write(madlibs)





