import audio_to_text ,extracting_text,video_info
from pathlib import Path
import pandas as pd
import time 
import logging

#Setting the log data pth
log_path = Path.cwd()/ 'log_data.log'
if log_path.exists()==False:
    log_path.touch

#Setting configuration for logging
logging.basicConfig(level = logging.DEBUG,
                    filename=log_path,
                    format= "[%(asctime)s: %(levelname)s]: %(message)s")
logging.info("Data Extraction Started")

start = time.time()
#Creating audio path for storing audio files
audio_path = Path.cwd() / 'audio_files'
if audio_path.exists() == False:
    audio_path.mkdir()
logging.info(f"Audio Path : {audio_path}")

#Creating data path for storing data files
data_path = Path.cwd() / 'data_files'
if data_path.exists() == False:
    data_path.mkdir()
logging.info(f"Data Path : {data_path}")
url = 'https://www.youtube.com/watch?v=J4Wdy0Wc_xQ&list=PLblh5JKOoLUIE96dI3U7oxHaCAbZgfhHk'

#created empty dataframe to store
data_set = pd.DataFrame(columns=['title','url','id','start','end','duration','text'])
data_set.to_csv(str(data_path / "data_set.csv"),sep = ',',index=False)
logging.info("Created empty dataframe")
#Extracting playlist info
info = video_info.videos_info(url,audio_path)
extracting_text.Extracting_text_from_audio(info,audio_path,data_path)

elapsed_time = (time.time() - start) / 60  
print(f"Elapsed time: {elapsed_time:.2f} minutes")
logging.info(f"Elapsed time: {elapsed_time:.2f} minutes")