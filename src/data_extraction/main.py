import audio_to_text ,extracting_text,video_info
from pathlib import Path
import pandas as pd
import time 
<<<<<<< Updated upstream
import csv
=======
import logging
>>>>>>> Stashed changes

log_path = Path.cwd()/ 'log_data.log'
if log_path.exists()==False:
    log_path.touch
logging.basicConfig(level = logging.DEBUG,
                    filename=log_path,
                    format= "[%(asctime)s: %(levelname)s]: %(message)s")
logging.info("Data Extraction Started")
start = time.time()
<<<<<<< Updated upstream
#Creating audio path for storing audio files
audio_path = Path.cwd().parent / 'audio_files'
if audio_path.exists() == True:
    print("Already exists")
else:
=======
logging.info("Creating audio path for storing audio files")
audio_path = Path.cwd() / 'audio_files'
if audio_path.exists() == False:
>>>>>>> Stashed changes
    audio_path.mkdir()
logging.info(f"Audio Path : {audio_path}")

<<<<<<< Updated upstream
#Creating data path for storing data files
data_path = Path.cwd().parent / 'data_files'
if data_path.exists() == True:
    print("Already exists")
else:
=======

logging.info("Creating data path for storing data files")
data_path = Path.cwd()/ 'data_files'
if data_path.exists() == False:
>>>>>>> Stashed changes
    data_path.mkdir()
logging.info(f"Data Path : {data_path}")
url = 'https://www.youtube.com/watch?v=J4Wdy0Wc_xQ&list=PLblh5JKOoLUIE96dI3U7oxHaCAbZgfhHk'

info = video_info.videos_info(url,audio_path)
df=extracting_text.Extracting_text_from_audio(info,audio_path)

<<<<<<< Updated upstream
df.to_csv(str(data_path / "modified_data.csv"),sep = ',',index=False)
=======
# df=data_modify.combine_datasets(data_path)

# modify_path=Path.cwd()
# df.to_csv(str(modify_path / "modified_data.csv"),sep = ',',index=False)
>>>>>>> Stashed changes

elapsed_time = (time.time() - start) / 60  
print(f"Elapsed time: {elapsed_time:.2f} minutes")