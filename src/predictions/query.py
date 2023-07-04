from faiss import read_index
from pathlib import Path
from embeddings import gen_embeddings
import pandas as pd

def searching_query(query,index):

    D, I =index.search(query,5)
    
    return I

if __name__=="__main__":

    data_path=Path.cwd().parents[1]/'data_files'/'videos_info'/'playlist_info'/'Dataset.csv'
    index_path=Path.cwd().parents[1]/'data_files'/'videos_info'/'playlist_info'/'Dataset.index'
    index=read_index(str(index_path))
    

    xq= ['what is bootstrap']
    xq_embd=gen_embeddings(xq)
    gen_list=searching_query(xq_embd,index)

    print('searching done')

    df=pd.read_csv(data_path)
    lines=df['text']
    preds=[f'{i}: {lines[i]}' for i in gen_list[0]]

    print(preds)

    urls=[df['url'][i]+'?t='+str(df['start'][i]) for i in gen_list[0]]
    print(urls)

