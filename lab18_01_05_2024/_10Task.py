import os
import random

def creatDir(dir): # function for create directory
    if not os.path.isdir(dir):
        os.mkdir(dir)
        print('directory is created')
    else:
        print('directory already exists')


def writeLineToFile(whatToWrite, pathWithFileName): # function for write line
    with open(pathWithFileName, 'a') as fileObj:
        fileObj.write(whatToWrite + '\n')

def getLinesFromFile(pathWithFileName): # if successful returned list lines
    listLines = []
    try:
        with open(pathWithFileName, 'r') as fileObj:
            fullText = fileObj.read().strip()
    except FileNotFoundError:
        print('File not found')
    else:
        listLines = fullText.split('\n')
    finally:
        if len(listLines)>0:
            print('file reader successful')
            return listLines
        else:
            print('an error occurred while reading the file. The file is either empty or not found.')


def mainFunc(dir, fileName):
    creatDir(dir)
    for i in range(13): # write data to file
        writeLineToFile(str(random.randint(1,13)), os.path.join(dir, fileName))
    listLines = getLinesFromFile(os.path.join(dir, fileName))
    counter = 0
    description = ''
    for i in range(len(listLines)):
        elInt = int(listLines[i])
        if (elInt % (i+1)) == 0:
            counter = counter + 1
            description = description + f' {listLines[i]} % {i+1} = 0 \n'
    print(f'From {len(listLines)} numbers {counter} are without the remainder of the division. \n  {description} ')


currentDir = os.getcwd()
dirSource = os.path.join(currentDir, 'source10')
fileName = 'test10.txt'
mainFunc(dirSource, fileName)