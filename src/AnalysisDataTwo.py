import pandas as pd
import AnalysisDataTwoGraphs as graphics

global data

def getOption():
    message = "Options \n"
    message += "1 - Relationship between men and women by social class \n"
    message += "2 - Passengers age histogram \n"
    message += "3 - Survival rate by age \n"
    message += "4 - Survivors and non-survivors by social class"
    print('Task 3 - practical component - simulated practices')
    print(message)
    option = input('Enter the option of the graph you want to see: ')
    return validateOption(option)

def validateOption(option):
    try:
        if not option.isnumeric():
            raise ValueError('Only numbers are allowed')
        return int(option)
    except ValueError as ve:
        print(ve)
        return False

def getData():
    global data
    data = pd.read_csv('files/titanic.csv')

def prepareData():
    global data
    meanAges = round(data['Age'].mean())
    data['Age'] = data['Age'].fillna(meanAges)
    data['Cabin'] = data['Cabin'].fillna('NS')
    data['Embarked'] = data['Embarked'].fillna('N')

def createGraphics(option):
    global data
    if option == 1:
        graphics.graphOne(data)
    elif option == 2:
        graphics.graphTwo(data)
    elif option == 3:
        graphics.graphThree(data)
    elif option == 4:
        graphics.graphFour(data)

def run():
    option = getOption()
    if option:
        getData()
        prepareData()
        createGraphics(option)

if __name__ == '__main__':
    run()
