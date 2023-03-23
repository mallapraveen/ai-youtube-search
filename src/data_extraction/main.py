import audio_to_text ,extracting_text,video_info
from pathlib import Path
import time 

start = time.time()
#Creating audio path for storing audio files
audio_path = Path.cwd() / 'src' / 'data_extraction' / 'audio_files'
if audio_path.exists() == True:
    print("Already exists")
else:
    audio_path.mkdir()
print(f"Audio Path : {audio_path}")

#Crating data path for storing data files
data_path = Path.cwd() / 'src' / 'data_extraction' / 'data_files'
if data_path.exists() == True:
    print("Already exists")
else:
    data_path.mkdir()
print(f"Data Path : {data_path}")
url = 'https://www.youtube.com/watch?v=J4Wdy0Wc_xQ&list=PLblh5JKOoLUIE96dI3U7oxHaCAbZgfhHk'

info = video_info.videos_info(url,audio_path)
extracting_text.Extracting_text_from_audio(info,audio_path,data_path)
print(f"time : {time.time()-start:5f}  secs")