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
    for i in range(12): # write data to file
        writeLineToFile(str(random.randint(1,9)), os.path.join(dir, fileName))
    listLines = getLinesFromFile(os.path.join(dir, fileName))
    counter = 0
    listAverageGeometricSquareOdd = []
    description = ''
    for el in listLines:
        elInt =  int(el)
        if elInt % 2 != 0:
            counter = counter + 1
            listAverageGeometricSquareOdd.append(elInt**2)
            if len(description) > 0:
                description = description + f' *{el}\u00b2 '
            else:
                description = description + f'{el}\u00b2 '
    averageGeometricSquareOdd = 1
    for i in listAverageGeometricSquareOdd:
        averageGeometricSquareOdd = averageGeometricSquareOdd * i
    averageGeometricSquareOdd = pow(averageGeometricSquareOdd, (1/counter))
    print(f'From {len(listLines)} numbers {counter} are odd numbers. And average geometric value to square is {counter} root of ({description}) = {averageGeometricSquareOdd}')


currentDir = os.getcwd()
dirSource = os.path.join(currentDir, 'source5')
fileName = 'test5.txt'
mainFunc(dirSource, fileName)