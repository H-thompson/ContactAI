import os
import AWSAPI
import boto3

def main():
    transcribe_client = boto3.client('transcribe', 'ap-northeast-2', aws_access_key_id="AKIAIP3WIQMCRKXPGSOQ", aws_secret_access_key="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")
    file = 'QA-01.mp3'
    file_uri = 'https://s3.ap-northeast-2.amazonaws.com/voiceai.io/RAW_AUDIO/' + file
    job = file.replace(".mp3","")
    AWSAPI.transcribe_file(job, file_uri, transcribe_client)

if __name__ == '__main__':
    main()
