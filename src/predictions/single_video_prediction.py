from faiss import read_index
from pathlib import Path
from embeddings import gen_embeddings
import pandas as pd
from data_extraction.youtube_info import playlist_info
from pred_main import creating_index
def searching_query(query,index):
    D, I =index.search(query,5)
    return I

if __name__=="__main__":
    url = 'https://www.youtube.com/watch?v=2m7Pgl-84F8&ab_channel=KrishNaik'
    video_info = playlist_info(url)
    video_name = video_info["title"]
    data_path=Path.cwd()/'data_files'/'videos_info'/'video_info'/ str(video_name)
    index_path=Path.cwd()/'data_files'/'videos_info'/'video_info'/str(video_name+'.index')
    
    df = pd.read_csv(data_path)
    final_embds=creating_index(df,index_path)
    df2=pd.concat([df,pd.DataFrame(final_embds)],axis=1)
    print(df2.shape)
    df2.to_csv(data_path)
    
    index=read_index(str(index_path))  

    xq= ['what is Generative AI?']
    xq_embd=gen_embeddings(xq)
    gen_list=searching_query(xq_embd,index)

    print('searching done')


    df=pd.read_csv(data_path)
    lines=df['text']
    preds=[f'{lines[i]}' for i in gen_list[0]]

    print(preds)

    urls=[df['url'][i]+'?t='+str(int(df['start'][i])) for i in gen_list[0]]
    print(urls)

