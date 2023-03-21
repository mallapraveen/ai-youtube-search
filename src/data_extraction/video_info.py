import yt_dlp
import os
url = 'https://www.youtube.com/watch?v=J4Wdy0Wc_xQ&list=PLblh5JKOoLUIE96dI3U7oxHaCAbZgfhHk'

def videos_info(url:str)->list:
    '''
    
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
    '''
    result = []
    urls=[]
    titles=[]
    ids=[]
    for video in playlist_entries:
        url = video['webpage_url']
        title = video['title']
        id = video['id']
        print(url)
        ydl.download([url])
        print("Downloaded file")
        filename = ydl.prepare_filename(video)
        filename = filename.replace('webm','mp3')
        print(filename)
        result.append(audio_to_text.transcribe(filename))
        urls.append(url)
        titles.append(title)
        ids.append(id)
        break
    '''
    return playlist_entries


