import whisper
from pathlib import Path
import logging

log_path = Path.cwd() / 'log_data.log'
if log_path.exists()==False:
   log_path.touch
logging.basicConfig(level = logging.DEBUG,
                    filename=log_path,
                    format= "[%(asctime)s: %(levelname)s]: %(message)s")
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
    logging.info("Transcribed the audio")
    return result
