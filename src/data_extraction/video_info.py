import yt_dlp
import os

def videos_info(url:str)->list:
    '''
    In this module we are getting url as input string and we are initializing the options to download the audio of a youtube vedio. To get the audio in the desried 
    location we are setting up path of current working directory and a folder to store all the audio files. As of now this module can return only the playlist info
    playlist entries like 
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


