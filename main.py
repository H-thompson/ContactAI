import os
import AWSAPI
import boto3

def main():
    transcribe_client = boto3.client('transcribe')
    file = 'QA-01.mp3'
    file_uri = 'https://s3.ap-northeast-2.amazonaws.com/voiceai.io/RAW_AUDIO/' + file
    transcribe_file(file, file_uri, transcribe_client)

if __name__ == '__main__':
    main()
