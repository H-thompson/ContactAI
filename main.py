import os
from Transcription import AWSAPI
import boto3
from Analysis import TextAnalysis
import SECRETtokens

def main():
    ID = SECRETtokens.tokens.aws_access_key_id
    KEY = SECRETtokens.tokens.aws_secret_access_key

    transcribe_client = boto3.client('transcribe', SECRETtokens.areas.area, aws_access_key_id= ID, aws_secret_access_key= KEY)
    file = 'QA-01.mp3'
    file_uri = SECRETtokens.url.bucket + file
    job = file.replace(".mp3","")

    try:
        AWSAPI.transcribe_file(job, file_uri, transcribe_client)
    except:
        TextAnalysis.Transcript(job)

if __name__ == '__main__':
    main()
