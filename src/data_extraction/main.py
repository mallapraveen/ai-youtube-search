import pandas as pd
import os
import json
from pathlib import Path

from extract_youtube_info import extracting_data_from_playlist
from youtube_info import playlist_info

from data_extraction import logger
from utilities.time_wrapper import timeit


@timeit
def extract_playlist_data(url):
    # Extracting playlist info
    info = playlist_info(url)

    playlist_name = info[0]["playlist_title"]

    # Creating audio path for storing platlist audio files
    audio_path = f"./audio_files/playlist_audio/{playlist_name}"

start = time.time()
#Creating audio path for storing audio files
audio_path = Path.cwd() / 'audio_files'
if audio_path.exists() == False:
    audio_path.mkdir()
logging.info(f"Audio Path : {audio_path}")


if __name__ == "__main__":
    url = "https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF"
    extract_playlist_data(url)
