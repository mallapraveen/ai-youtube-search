import yt_dlp
import os

def videos_info(url:str)->list:
    '''
       Extracting complete information about the playlist
       
       Parameters:
       -----------
          url: str
            The youtube plalist url from user
       
       returns:
       --------
       playlist_entries: list
          contains all the information about the playlist.That includes:- 
            ['id', 'title', 'formats', 'thumbnails', 'thumbnail', 'description',
           'uploader', 'uploader_id', 'uploader_url', 'channel_id', 'channel_url',
           'duration', 'view_count', 'average_rating', 'age_limit', 'webpage_url',
           'categories', 'tags', 'playable_in_embed', 'live_status',
           'release_timestamp', '_format_sort_fields', 'automatic_captions',
           'subtitles', 'comment_count', 'chapters', 'like_count', 'channel',
           'channel_follower_count', 'upload_date', 'availability', 'original_url',
           'webpage_url_basename', 'webpage_url_domain', 'extractor',
           'extractor_key', 'playlist_count', 'playlist', 'playlist_id',
           'playlist_title', 'playlist_uploader', 'playlist_uploader_id',
           'n_entries', 'playlist_index', '__last_playlist_index',
           'playlist_autonumber', 'display_id', 'fulltitle', 'duration_string',
           'is_live', 'was_live', 'requested_subtitles', '_has_drm', 'asr',
           'filesize', 'format_id', 'format_note', 'source_preference', 'fps',
           'audio_channels', 'height', 'quality', 'has_drm', 'tbr', 'url', 'width',
           'language', 'language_preference', 'preference', 'ext', 'vcodec',
           'acodec', 'dynamic_range', 'abr', 'protocol', 'fragments', 'container',
           'resolution', 'aspect_ratio', 'http_headers', 'audio_ext', 'video_ext',
           'format']
    '''
    
    #Creating directory to store audio files
    directory = "audio_files"
    parent_dir = "C:/Users/NHI360/Desktop/ml-youtube-search/src/data_extraction/"
    path = parent_dir+directory
    
    #checking the path existence is OS
    if os.path.exists(path):
        print("It already exists")
    else:
        path = os.path.join(parent_dir, directory)
        os.makedirs(path, mode = 0o777, exist_ok = False)
        print("Directory '% s' created" % directory)

    print(path)
    
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
    #Extracting the playlist data
    playlist_info = ydl.extract_info(url, download=False)
    #For the information about videos in playlist
    playlist_entries = playlist_info.get('entries',None)
    print("Extracted playlist info successfully")
    return playlist_entries


