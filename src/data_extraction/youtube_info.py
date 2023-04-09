import yt_dlp
import os
from data_extraction import logger
from pathlib import Path


def playlist_info(url: str) -> list:
  """
  Extracting complete information about the playlist

  Parameters:
  -----------
      url: str
        The youtube plalist url from user

  returns:
  --------
  playlist_entries: list contains all the information about the playlist.
  """

  ydl = yt_dlp.YoutubeDL()
  # Extracting the playlist data
  playlist = ydl.extract_info(url, download=False)
  # For the information about videos in playlist
  playlist_entries = playlist.get("entries", None)
  logger.info("Extracted playlist information")
  return playlist_entries
