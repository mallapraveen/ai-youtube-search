import whisper
import ffmpeg
import os

def transcribe(audio_url:str)->str:
    '''
         Extracting text from the audio.
         
      Parameters:
      -----------
        audio_url: str
         The audio file location in the particular directory
       
      returns:
      --------
         result: str
            The extracted Text from audio in the form of string
    
    
    '''
    model = whisper.load_model("tiny")
    result = model.transcribe(audio_url,fp16=False)
    print("audio Success")
    return result
