import pandas as pd
from pathlib import Path

from embeddings import gen_embeddings
from vectorDB_Faiss import faiss_db
from faiss import write_index

def creating_index(dataframe,path):

    faiss_class=faiss_db(384)
    
    
    embds=gen_embeddings(dataframe['text'])
    print('embeddings generated')

    faiss_class.storing_vectors(embds)
    print('Stored successfully')

    write_index(faiss_class.index,str(path))

    return embds




if __name__=='__main__':
    data_path=Path.cwd().parents[1]/'data_files'/'videos_info'/'playlist_info'/'Dataset.csv'
    index_path=Path.cwd().parents[1]/'data_files'/'videos_info'/'playlist_info'/'Dataset.index'

    df=pd.read_csv(data_path)
    print('Data set read completed')

    final_embds=creating_index(df,index_path)

    df2=pd.concat([df,pd.DataFrame(final_embds)],axis=1)
    print(df2.shape)

    df2.to_csv(data_path)
    
    








    