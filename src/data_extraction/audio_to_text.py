import whisper
import ffmpeg
import os

def transcribe(audio_url):
    if not os.path.exists(audio_url):
        print(f"File not found at path: {audio_url}")
    else:
        print("File is there")
    model = whisper.load_model("tiny")
    result = model.transcribe(audio_url,fp16=False)
    print("audio Success")
    return result
