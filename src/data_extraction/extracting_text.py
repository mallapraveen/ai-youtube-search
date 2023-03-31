import yt_dlp
import video_info ,audio_to_text,data_modify
import os
import pandas as pd
import copy

def Extracting_text_from_audio(video_info:list,audio_path:str):
    '''
    Takes the video_info and extracts text from audio_to_text module and convertes it into dataframe
    
    Parameters:
    -----------
    video_info: list
       It contains all infromation about the playlist which have mentioned in the module video_info.
    audio_path : str
            audio path to store audio files
    data_path : str
        path to store dataframes
    Returns: None
    
    '''

    #options to download only audio of youtube video
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': str(audio_path /'%(title)s.%(ext)s'),
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        }],
        'extractaudio': True,
        'audioformat': 'mp3',
        
    }
    ydl = yt_dlp.YoutubeDL(ydl_opts)
    
    #Extracting text
    Final_dataset=pd.DataFrame()
    for i in range(len(video_info)):
      video = video_info[i]
      url = video['webpage_url']
      ydl.download([url])
      filename = ydl.prepare_filename(video)
      filename = filename.replace('webm','mp3')
      result = audio_to_text.transcribe(filename)
      seg = result['segments']
      df = pd.DataFrame(seg, columns=['start', 'end', 'text','id'])
      df['id'] = video['id']
      df['title'] = video['title']
      df['url'] = video['webpage_url']
      df = df.reindex(columns=['title','url','id','start','end','text'])


      h=copy.deepcopy(df)
      h['start'].astype('float32')
      h['end'].astype('float32')
      df1=data_modify.combine_rows1(h)
      Final_dataset = pd.concat([Final_dataset,df1],axis=0)
      Final_dataset.reset_index(drop=True,inplace=True)
      print(Final_dataset)

    Final_dataset['duration']=Final_dataset['end']-Final_dataset['start']
    return Final_dataset






