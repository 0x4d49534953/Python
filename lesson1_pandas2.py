import pandas as pd

df = pd.DataFrame({
     'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
     'population': [17.04, 143.5, 9.5, 45.5],
     'square': [2724902, 17125191, 207600, 603628]
 })


df['density']= (df['population'] * 1000000) / df['square']
df.rename(columns = {'population':'Население', 'square':'площадь'}, inplace = True)
