import yt_dlp
import video_info ,audio_to_text
import pandas as pd
from pathlib import Path
import logging

#Setting the log data pth
log_path = Path.cwd()/ 'log_data.log'
if log_path.exists()==False:
    log_path.touch

#Setting configuration for logging
logging.basicConfig(level = logging.DEBUG,
                    filename=log_path,
                    format= "[%(asctime)s: %(levelname)s]: %(message)s")
    
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
      logging.info(f"Downloaded video {i+1}")
      filename = ydl.prepare_filename(video)
      filename = filename.replace('webm','mp3')
      result = audio_to_text.transcribe(filename)
      seg = result['segments']
      df = pd.DataFrame(seg, columns=['start', 'end', 'text','id'])
      df['id'] = video['id']
      df['title'] = video['title']
      df['url'] = video['webpage_url']
      df['start'].astype('float32')
      df['end'].astype('float32')
      df = df.reindex(columns=['title','url','id','start','end','text'])
      data_set = pd.read_csv(str(data_path / "data_set.csv"))
      res= df.groupby(df.index//5).agg({'title':'first','url':'first','id':'first','start':'first','end':'last','text' : lambda x:''.join(x)})
      res['duration'] = res['end']-res['start']
      res = res.reindex(columns=['title','url','id','start','end','duration','text'])
      data_set = pd.concat([data_set,res],axis=0)
      data_set.to_csv(str(data_path / "data_set.csv"),sep = ',',index=False)
    logging.info("Completed")