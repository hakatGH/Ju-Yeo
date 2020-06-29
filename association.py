import pandas as pd
from pandas import DataFrame as df

food = pd.read_csv('안주추천.csv')
weather = pd.read_csv('날씨추천.csv')
situation = pd.read_csv('상황추천.csv')

def chatbot(selec,instance):
    if selec == '안주':
        for j in range(0,len(food[selec])):
            if food[selec][j] == instance:
                return food['전통주'][j]
    elif selec == '상황':
        for j in range(0,len(situation[selec])):
            if situation[selec][j] == instance:
                return situation['전통주'][j]
    else:
        for j in range(0,len(weather[selec])):
            if weather[selec][j] == instance:
                return weather['전통주'][j]