import yt_dlp
import video_info ,audio_to_text
import os
import pandas as pd


def Extracting_text_from_audio(video_info:list,audio_path:str,data_path:str):
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
      print(df)
      df.to_csv(str(data_path / f"video_{i+1}.csv"),sep = ',',index=False)
      print(df)
      print(str(data_path / f"{video['title']}.csv"))




