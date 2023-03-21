import whisper
def transcribe(audio_url):
    model = whisper.load_model("tiny")
    result = model.transcribe(audio_url,fp16=False)
    print("audio Success")
    print(result.keys())
    return result
