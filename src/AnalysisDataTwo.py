import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('_mpl-gallery')

def getData():
    return pd.read_csv('files/titanic.csv')

def graphOne(data):
    graphicData = data.groupby(['Pclass', 'Sex'])['PassengerId'].count().unstack()
    fig, ax = plt.subplots()
    ax.barh(graphicData.index.values, graphicData['male'], label='Men')
    ax.barh(graphicData.index.values, graphicData['female'], left=graphicData['male'], label='Women')
    ax.set_title('Relationship between men and women by social class')
    ax.set_xlabel('Number of passengers')
    ax.set_ylabel('Social class')
    ax.legend()
    plt.show()

def run():
    print('Task 3 - practical component - simulated practices')
    data = getData()
    graphOne(data)
    

if __name__ == '__main__':
    run()
