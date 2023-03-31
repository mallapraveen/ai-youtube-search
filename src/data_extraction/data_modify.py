import pandas as pd
from pathlib import Path
import csv

def combine_rows(df):
  df1=pd.DataFrame()
  s=0
  i=0
  while i<len(df)-1:
    j=i
    k=df.loc[j,'duration']
    text=df.loc[j,'text']
    start=df.loc[j,'start']
    while k+df.loc[j+1,'duration']<25 and j+1<len(df)-1:
      text=text+df.loc[j+1,'text']
      k+=df.loc[j+1,'duration']
      j+=1
    
    df1.loc[s,'url']=df.loc[i,'url']
    df1.loc[s,'id']=df.loc[i,'id']
    df1.loc[s,'title']=df.loc[i,'title']
    df1.loc[s,'start']=start
    df1.loc[s,'end']=start+k
    df1.loc[s,'duration']=k
    df1.loc[s,'text']=text
    s+=1
    i=j+1

  return df1

def combine_datasets(path):
  result=pd.DataFrame()
  files = Path(path).rglob('*')
  for file in files:
    with open(str(file), 'r') as f:
      r=csv.reader(f)
      data=[]
      for row in r:
        data.append(row)

    df=pd.DataFrame(data[1:],columns=data[0])
    df['start']=df['start'].astype(float)
    df['end']=df['end'].astype(float)
    df['duration']=df['end']-df['start']
    df_r=combine_rows(df)
    result=pd.concat([result,df_r],axis=0)
  
  result.reset_index(drop=True,inplace=True)
  return result

    



