import yt_dlp
import video_info ,audio_to_text


def Extracting_text_from_audio(video_info):
    directory = "audio_files"
    parent_dir = "C:/Users/NHI360/Desktop/ml-youtube-search/src/data_extraction/"
    path = parent_dir+directory
    print(path)
    #options to download only audio of youtube video
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': path+'/%(title)s.%(ext)s',
    }
    ydl = yt_dlp.YoutubeDL(ydl_opts)
    result = []
    urls=[]
    titles=[]
    ids=[]
    for video in video_info:
      url = video['webpage_url']
      title = video['title']
      id = video['id']
      ydl.download([url])
      filename = ydl.prepare_filename(video)
      filename = filename.replace('webm','mp3')
      print(filename)
      result.append(audio_to_text.transcribe(filename))
      urls.append(url)
      titles.append(title)
      ids.append(id)
      break
    print(result)
    return result

url = 'https://www.youtube.com/watch?v=J4Wdy0Wc_xQ&list=PLblh5JKOoLUIE96dI3U7oxHaCAbZgfhHk'
info = video_info.videos_info(url)
print(len(info))
res = Extracting_text_from_audio(info)
