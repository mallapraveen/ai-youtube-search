import pandas as pd
import os
import json
from pathlib import Path
import yt_dlp
from extract_youtube_info import extracting_data_from_playlist
from youtube_info import playlist_info
from sentence_transformers import SentenceTransformer
from data_extraction import logger
from utilities.time_wrapper import timeit
import audio_to_text
import time
@timeit
def download_audio(url, audio_path):
    # Setting ydl_options
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": str(audio_path + "/" + "%(title)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "extractaudio": True,
        "audioformat": "mp3",
    }

    ydl = yt_dlp.YoutubeDL(ydl_opts)
    ydl.download([url])
    logger.info(f"Downloaded video")

@timeit
def create_dataframe(video_info, seg):
    # Creating dataframe
    df = pd.DataFrame(seg, columns=["start", "end", "text", "id"])
    df["id"] = video_info["id"]
    df["title"] = video_info["title"]
    df["url"] = video_info["webpage_url"]
    df["start"].astype("float32")
    df["end"].astype("float32")
    df = df.reindex(columns=["title", "url", "id", "start", "end", "text"])
    df = df.groupby(df.index // 5).agg(
        {
            "title": "first",
            "url": "first",
            "id": "first",
            "start": "first",
            "end": "last",
            "text": lambda x: "".join(x),
        }
    )
    df["duration"] = df["end"] - df["start"]
    df = df.reindex(
        columns=["title", "url", "id", "start", "end", "duration", "text"]
    )
    df["duration"] = df["end"] - df["start"]
    return df

@timeit
def save_dataframe(df, data_path):
    df.to_csv(data_path, mode="a")

@timeit
def main():
    url = 'https://www.youtube.com/watch?v=2m7Pgl-84F8&ab_channel=KrishNaik'
    video_info = playlist_info(url)
    video_name = video_info["title"]
    audio_path = f"./audio_files/audio/{video_name}"
    data_path = f"./data_files/videos_info/video_info/{video_name}"

    download_audio(video_info["original_url"], audio_path)
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": str(audio_path + "/" + "%(title)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "extractaudio": True,
        "audioformat": "mp3",
    }

    ydl = yt_dlp.YoutubeDL(ydl_opts)
    filename = ydl.prepare_filename(video_info)
    filename = (
        filename.replace(".webm", ".mp3")
        .replace(".mp4", ".mp3")
        .replace(".mkv", ".mp3")
    )
    result = audio_to_text.transcribe(filename)
    seg = result['segments']
    df = create_dataframe(video_info, seg)
    save_dataframe(df, data_path)

   

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    actual_time = end-start
    print(actual_time)
    logger.info("actual time : {} secs".format(actual_time))
