import pandas as pd
from pathlib import Path

from embeddings import gen_embeddings
from vectorDB_Faiss import faiss_db



if __name__=='__main__':
    data_path=Path.cwd().parents[1]/'data_files'/'videos_info'/'playlist_info'/'Dataset.csv'

    df=pd.read_csv(data_path)
    print('Data set read completed')

    faiss_class=faiss_db(384)
    
    if faiss_class.index.ntotal!=df.shape[0]:
        embds=gen_embeddings(df['text'])
        print('embeddings generated')

        faiss_class.storing_vectors(embds)
        print('Stored successfully')
    
    xq= ['what is bootstrap']
    xq_embd=gen_embeddings(xq)
    gen_list=faiss_class.searching_vectors(xq_embd)
    print('searching done')

    lines=df['text']
    preds=[f'{i}: {lines[i]}' for i in gen_list[0]]

    print(preds)

    urls=[df['url'][i]+'?t='+str(df['start'][i]) for i in gen_list[0]]
    print(urls)









    