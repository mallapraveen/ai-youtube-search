import audio_to_text ,extracting_text,video_info

url = 'https://www.youtube.com/watch?v=J4Wdy0Wc_xQ&list=PLblh5JKOoLUIE96dI3U7oxHaCAbZgfhHk'

info = video_info.videos_info(url)
data = extracting_text.Extracting_text_from_audio(info)
print(data)