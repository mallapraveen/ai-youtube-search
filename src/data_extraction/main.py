import audio_to_text ,extracting_text,video_info
from pathlib import Path
import pandas as pd
import time 
import csv

start = time.time()
#Creating audio path for storing audio files
audio_path = Path.cwd().parent / 'audio_files'
if audio_path.exists() == True:
    print("Already exists")
else:
    audio_path.mkdir()
print(f"Audio Path : {audio_path}")

#Creating data path for storing data files
data_path = Path.cwd().parent / 'data_files'
if data_path.exists() == True:
    print("Already exists")
else:
    data_path.mkdir()
print(f"Data Path : {data_path}")
url = 'https://www.youtube.com/watch?v=J4Wdy0Wc_xQ&list=PLblh5JKOoLUIE96dI3U7oxHaCAbZgfhHk'

info = video_info.videos_info(url,audio_path)
df=extracting_text.Extracting_text_from_audio(info,audio_path)

df.to_csv(str(data_path / "modified_data.csv"),sep = ',',index=False)

elapsed_time = (time.time() - start) / 60  
print(f"Elapsed time: {elapsed_time:.2f} minutes")