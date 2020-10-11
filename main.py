import os
from Transcription import AWSAPI
import boto3
from Analysis import TextAnalysis
import SECRETtokens
# import uuid
# import sounddevice as sd

def main():
    ID = SECRETtokens.tokens.aws_access_key_id
    KEY = SECRETtokens.tokens.aws_secret_access_key

    # sd.default.samplerate = 44100
    # recording = sd.rec(channels=2, frames=44100)
    
    # sd.wait()
    
    # jobID = uuid.uuid1()
    
    # AWSAPI.addFile(jobID)
    
    jobID = "QA-01"
    
    transcribe_client = boto3.client('transcribe', SECRETtokens.areas.area, aws_access_key_id= ID, aws_secret_access_key= KEY)
    file = jobID
    file_uri = SECRETtokens.url.bucket + file
    job = str(jobID)

    try:
        AWSAPI.transcribe_file(job, file_uri, transcribe_client)
    except:
        TextAnalysis.Transcript(job)

if __name__ == '__main__':
    main()
