import pandas as pd
'''
function motot is to combining 5 rows into 1row

Parameters:
-----------
    df: DataFrame
      raw data frame

Returns:
--------
  modified Data frame 



'''
def combine_rows1(df:pd.DataFrame)->pd.DataFrame:
  row=0
  while row<len(df) and row+5<len(df):
    df.loc[row,'text']=''.join(df.loc[row:row+5,'text'])
    df.loc[row,'end']=df.loc[row+4,'end']
    df.drop(df.index[row+1:row+5],inplace=True)
    df.reset_index(drop=True,inplace=True)
    row+=1
  df.loc[row,'text']=''.join(df.loc[row:,'text'])
  df.loc[row,'end']=df.loc[len(df)-1,'end']
  df.drop(df.index[row+1:-1],inplace=True)
  df.reset_index(drop=True,inplace=True)
  return df



