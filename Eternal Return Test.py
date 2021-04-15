import pandas as pd
import re

data_char = pd.read_excel('Eternal Return Stats 03082021 - Char.xlsx', engine='openpyxl')
data_weapon = pd.read_excel('Eternal Return Stats 03082021 - Weapons.xlsx', engine = 'openpyxl')
data_weapon2 = pd.read_excel('Eternal Return Stats 03082021 - Weapons2.xlsx', engine = 'openpyxl')
data_armor = pd.read_excel('Eternal Return Stats 03082021 - Armor.xlsx', engine = 'openpyxl')

print(data_char.loc[40:60,'Unnamed: 2'])

data_char.loc[2:42, 'Unnamed: 2'] = data_char.loc[2:42, 'Unnamed: 2'].astype(float)
data_char.loc[2:42, 'Unnamed: 2'] = data_char.loc[2:42, 'Unnamed: 2']/100
data_char.loc[49:, 'Unnamed: 2'] = data_char.loc[49:, 'Unnamed: 2'].astype(float)
data_char.loc[49:, 'Unnamed: 2'] = data_char.loc[49:, 'Unnamed: 2']/100

data_char.loc[2:42, 'Unnamed: 3'] = data_char.loc[2:42, 'Unnamed: 3'].astype(float)
data_char.loc[49:, 'Unnamed: 3'] = data_char.loc[49:, 'Unnamed: 3'].astype(float)
data_char.loc[2:42, 'Unnamed: 3'] = data_char.loc[2:42, 'Unnamed: 3']/100
data_char.loc[49:, 'Unnamed: 3'] = data_char.loc[49:, 'Unnamed: 3']/100

data_char.loc[2:42, 'Unnamed: 7'] = data_char.loc[2:42, 'Unnamed: 7'].astype(float)
data_char.loc[2:42, 'Unnamed: 7'] = data_char.loc[2:42, 'Unnamed: 7']/100
data_char.loc[49:, 'Unnamed: 7'] = data_char.loc[49:, 'Unnamed: 7'].astype(float)
data_char.loc[49:, 'Unnamed: 7'] = data_char.loc[49:, 'Unnamed: 7']/100

data_char.loc[2:42, 'Unnamed: 8'] = data_char.loc[2:42, 'Unnamed: 8'].astype(float)
data_char.loc[49:, 'Unnamed: 8'] = data_char.loc[49:, 'Unnamed: 8'].astype(float)
data_char.loc[2:42, 'Unnamed: 8'] = data_char.loc[2:42, 'Unnamed: 8']/100
data_char.loc[49:, 'Unnamed: 8'] = data_char.loc[49:, 'Unnamed: 8']/100

data_char.loc[2:42, 'Unnamed: 12'] = data_char.loc[2:42, 'Unnamed: 12'].astype(float)
data_char.loc[49:, 'Unnamed: 12'] = data_char.loc[49:, 'Unnamed: 12'].astype(float)
data_char.loc[2:42, 'Unnamed: 12'] = data_char.loc[2:42, 'Unnamed: 12']/100
data_char.loc[49:, 'Unnamed: 12'] = data_char.loc[49:, 'Unnamed: 12']/100

data_char.loc[2:42, 'Unnamed: 13'] = data_char.loc[2:42, 'Unnamed: 13'].astype(float)
data_char.loc[49:, 'Unnamed: 13'] = data_char.loc[49:, 'Unnamed: 13'].astype(float)
data_char.loc[2:42, 'Unnamed: 13'] = data_char.loc[2:42, 'Unnamed: 13']/100
data_char.loc[49:, 'Unnamed: 13'] = data_char.loc[49:, 'Unnamed: 13']/100

data_char = data_char.drop(labels=[43,44,45])
data_char = data_char.reset_index()

data_char_all = data_char.drop(data_char.index[43:88])
data_char_top = data_char.drop(data_char.index[0:43])

print(data_char_all.loc[40:50, ('All Ranks', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 12', 'Unnamed: 13')])
print(data_char_top.loc[1:45, ('All Ranks', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 12', 'Unnamed: 13')])
