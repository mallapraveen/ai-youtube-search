import yt_dlp
import video_info ,audio_to_text
import os
import pandas as pd


def Extracting_text_from_audio(video_info):
    directory = "audio_files"
    parent_dir = "C:/Users/NHI360/Desktop/ml-youtube-search/src/data_extraction/"
    path = parent_dir+directory
    print(path)
    #os.environ['FFMPEG_PATH'] = 'C:/Users/NHI360/Downloads/ffmpeg-2023-03-20-git-57afccc0ef-full_build/ffmpeg-2023-03-20-git-57afccc0ef-full_build/bin/ffmpeg'
    #options to download only audio of youtube video
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': path+'/%(title)s.%(ext)s',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        }],
        'extractaudio': True,
        'audioformat': 'mp3',
        
    }
    ydl = yt_dlp.YoutubeDL(ydl_opts)
    data = pd.DataFrame(columns=['title','url','id','start','end','text'])
    #Extracting text
    for video in video_info:
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
      data = pd.concat([data,df],axis=0,ignore_index=True)
      print(data)
    return data





