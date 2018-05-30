import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()

def answer_one():
    return df['Gold'].argmax()
answer_one()

def answer_two():
    diff = df['Gold']-df['Gold.1']
    return diff.argmax()
answer_two()

def answer_three():
# without this first copying operation you get a "variable referenced before assignment" error, which occurs because 
# the variable I'm reassigning in the first step already exists. Overcame this by creating a copy of the array. 
    df_copy = df.copy()
    df_copy = df_copy[(df_copy['Gold']> 0) & (df_copy['Gold.1']>0)]
    diff = (df_copy['Gold']-df_copy['Gold.1'])/(df_copy['Gold.2'])
    return diff.argmax()
answer_three()
