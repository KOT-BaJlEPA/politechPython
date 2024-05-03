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
    for i in range(15): # write data to file
        writeLineToFile(str(random.randint(-20,20)), os.path.join(dir, fileName))
    listLines = getLinesFromFile(os.path.join(dir, fileName))
    counter = 0
    multiplierM = 1
    description = ''
    for el in listLines:
        elInt =  int(el)
        if (abs(elInt)>=2) & (abs(elInt)<=7):
            counter = counter + 1
            multiplierM = multiplierM * elInt
            if len(description) > 0:
                description = description + f' *{el}'
            else:
                description = description + f'{el}'
    print(f'From {len(listLines)} numbers {counter} are include [2;7]. And multiplication {description} = {multiplierM}')


currentDir = os.getcwd()
dirSource = os.path.join(currentDir, 'source9')
fileName = 'test9.txt'
mainFunc(dirSource, fileName)