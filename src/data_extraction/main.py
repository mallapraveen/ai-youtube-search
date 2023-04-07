import pandas as pd
import os
from pathlib import Path

from extracting_text import extracting_text_from_audio
from youtube_info import videos_info

from data_extraction import logger
from utilities.time_wrapper import timeit


@timeit
def data_extract():
    # Creating audio path for storing audio files
    audio_path = "./audio_files"
    os.makedirs(audio_path, exist_ok=True)
    logger.info(f"Audio Path : {audio_path}")

    # Creating data path for storing data files
    data_path = "./data_files"
    os.makedirs(data_path, exist_ok=True)
    logger.info(f"Data Path : {data_path}")
    url = "https://www.youtube.com/watch?v=J4Wdy0Wc_xQ&list=PLblh5JKOoLUIE96dI3U7oxHaCAbZgfhHk"

    # created empty dataframe to store
    data_set = pd.DataFrame(
        columns=["title", "url", "id", "start", "end", "duration", "text"]
    )
    data_set.to_csv(Path(data_path + "/data_set.csv"), sep=",", index=False)
    logger.info("Created empty dataframe")
    # Extracting playlist info
    info = videos_info(url, audio_path)
    extracting_text_from_audio(info, audio_path, data_path)


if __name__ == "__main__":
    data_extract()
