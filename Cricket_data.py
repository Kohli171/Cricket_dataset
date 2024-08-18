# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qlXflZApi3LR3OEZfYEAfIa6lm4Eo3Dv
"""

import pandas as pd

df=pd.read_csv('cricket_test_match.csv')

df

#rename Multiple columns in a list

df=df.rename(columns= {'NO':'Not_Outs','HS':'Highest_Inns_score','BF':'Balls_Faced','SR':'Strike_Rate','Mat':'Matches'})

df

df.head()

#Check Null values

df.isnull().any()

#drop duplicates

df.duplicated()

#split up span into start and end date + career lenth

df.head()

df['Span'].str.split(pat = '-')

df['Rookie_Year'] = df['Span'].str.split(pat = '-').str[0]

df['Final_Year'] = df['Span'].str.split(pat = '-').str[1]

df.head()

#drop span columns

df.drop(['Span'], axis=1)

# Question -> Split up the country  from the player

df['Player'].str.split(pat = '(')

df['Country']=df['Player'].str.split(pat='(').str[1]

df['Country']=df['Country'].str.split(pat=')').str[0]

df['Country']

df['Player']

df.head()



df.dtypes

df['Highest_Inns_score'].str.split(pat='*').str[0]

df['Highest_Inns_score']=df['Highest_Inns_score'].str.split(pat='*').str[0]

df['Highest_Inns_score']

df['Highest_Inns_score'].astype('int')

df['Highest_Inns_score']=df['Highest_Inns_score'].astype('int')

df.dtypes

df=df.astype({'Rookie_Year':'int','Final_Year':'int'})

df.dtypes

# Question -> Build out career length column

df['career_length']=df['Final_Year']-df['Rookie_Year']

df['career_length']

#Question ->What is the average career length

df['career_length'].mean()

#Question->  Avg Batting strike rate for cricketers who played over 10 years

df[df['career_length']>10]['Strike_Rate'].mean()

#Question ->Cricketrs played before 1960

df[df['Rookie_Year']<1960]['Player'].count()

#Question Max highest Inn score by country

df.groupby('Country')['Highest_Inns_score'].max()

#Question  Hundreds. fifties and ducks average by country

df.groupby('Country')[['100','50','0']].mean()
