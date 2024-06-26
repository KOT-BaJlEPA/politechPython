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
        writeLineToFile(str(random.randint(-5,5)), os.path.join(dir, fileName))
    listLines = getLinesFromFile(os.path.join(dir, fileName))
    counter = 0
    listAverageGeometricModul = []
    description = ''
    for el in listLines:
        elInt =  int(el)
        if elInt<0:
            counter = counter + 1
            listAverageGeometricModul.append(abs(elInt))
            if len(description) > 0:
                description = description + f' *|{el}|'
            else:
                description = description + f'|{el}|'
    averageGeometricModul = 1
    for i in listAverageGeometricModul:
        averageGeometricModul = averageGeometricModul * i
    averageGeometricModul = pow(averageGeometricModul, (1/counter))
    print(f'From {len(listLines)} numbers {counter} are less then 0. And average geometric value to modul is {counter} root of({description}) = {averageGeometricModul}')


currentDir = os.getcwd()
dirSource = os.path.join(currentDir, 'source4')
fileName = 'test4.txt'
mainFunc(dirSource, fileName)