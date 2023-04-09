import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('_mpl-gallery')

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

def graphTwo(data):
    plt.hist(data['Age'], bins=10, color='green')
    plt.title('Passengers age histogram')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()

def graphThree(data):
    ageGroups = pd.cut(data['Age'], bins=range(0, 90, 10))
    survival = data.groupby(ageGroups)['Survived'].mean()
    plt.plot(survival.index.astype(str), survival.values, marker='o')
    plt.title('Survival rate by age')
    plt.xlabel('Age')
    plt.ylabel('Survival rate')
    plt.show()

def graphFour(data):
    survivalByClass = data.groupby(['Pclass', 'Survived'])['PassengerId'].count().unstack()
    fig, ax = plt.subplots()
    ax.bar([1, 2, 3], survivalByClass[1], width=0.35, label='Survivors')
    ax.bar([1+0.35, 2+0.35, 3+0.35], survivalByClass[0], width=0.35, label='No survivors')
    ax.set_xticks([1+0.35/2, 2+0.35/2, 3+0.35/2])
    ax.set_xticklabels(['First class', 'Second class', 'Third class'])
    ax.set_title('Survivors and non-survivors by social class')
    ax.set_ylabel('Number of people')
    ax.legend()
    plt.show()