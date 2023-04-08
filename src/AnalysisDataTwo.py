import pandas as pd
import AnalysisDataTwoGraphs as graphics

global data

def getData():
    global data
    data = pd.read_csv('files/titanic.csv')

def prepareData():
    global data
    meanAges = round(data['Age'].mean())
    data['Age'] = data['Age'].fillna(meanAges)
    data['Cabin'] = data['Cabin'].fillna('NS')
    data['Embarked'] = data['Embarked'].fillna('N')

def createGraphics():
    global data
    graphics.graphTwo(data)

def run():
    print('Task 3 - practical component - simulated practices')
    getData()
    prepareData()
    createGraphics()

if __name__ == '__main__':
    run()
