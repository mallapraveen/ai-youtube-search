def combine_rows1(df):
  i=0
  while i<len(df) and i+5<len(df):
    df.loc[i,'text']=''.join(df.loc[i:i+5,'text'])
    df.loc[i,'end']=df.loc[i+4,'end']
    df.drop(df.index[i+1:i+5],inplace=True)
    df.reset_index(drop=True,inplace=True)
    i+=1
  df.loc[i,'text']=''.join(df.loc[i:,'text'])
  df.loc[i,'end']=df.loc[len(df)-1,'end']
  df.drop(df.index[i+1:-1],inplace=True)
  df.reset_index(drop=True,inplace=True)
  return df



