import pandas as pd

dataframe = pd.DataFrame({'DOB': {0: '04/11/2020', 1: '13/03/2021', 2: '26/01/2020', 3: '26/02/2020'}})
print(dataframe)
dataframe['DOB'] = pd.to_datetime(dataframe.DOB) 
print(dataframe)
dataframe = dataframe.sort_values(by='DOB', ascending = True)
print(dataframe)
dataframe['DOB'] = dataframe['DOB'].dt.strftime('%d/%m/%Y')
print(dataframe)