import pandas as pd


hi_file_name = './hawaii-covid-data.csv'
df_raw = pd.read_csv(hi_file_name)

print('='*50)
print(df_raw.head())
print(type(df_raw))

print('='*50)
print(df_raw.info())

df_raw['date'] = pd.to_datetime(df_raw['submission_date'], format='%m/%d/%Y')

print('='*50)
print(df_raw.info())

print('='*50)
print(df_raw.head())

print('='*50)
print(df_raw['date'].dt.year.unique())

#df_raw에 2021년도 하와이 인구(population)를 대입(저장)!!!!
