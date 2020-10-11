import time
import boto3
import boto3
import requests
#import json
from Analysis import TextAnalysis
import SECRETtokens
from SECRETtokens import url

def addFile():
    addURL = "http://voiceai.io.s3." + SECRETtokens.areas.area + ".amazonaws.com/"
    s3 = boto3.resource('s3')
    resp = s3.meta.client.upload_file('Transcription/audio/', SECRETtokens.areas.area, '')
    print(resp.status_code)

def transcribe_file(job_name, file_uri, transcribe_client):
    transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': file_uri},
        MediaFormat='mp3',
        LanguageCode='en-US',
    )

    max_tries = 60
    while max_tries > 0:
        max_tries -= 1
        job = transcribe_client.get_transcription_job(TranscriptionJobName=job_name)
        job_status = job['TranscriptionJob']['TranscriptionJobStatus']
        if job_status in ['COMPLETED', 'FAILED']:
            print(f"Job {job_name} is {job_status}.")
            if job_status == 'COMPLETED':
                print("Transcript downloaded...")
                Download(f"\t{job['TranscriptionJob']['Transcript']['TranscriptFileUri']}", job_name)
            break
        else:
            print(f"Waiting for {job_name}. Current status is {job_status}.")
        time.sleep(10)

def Download(url, job):
    r = requests.get(url, allow_redirects=True)
    open('Transcription/JSON/' + job + '.json', 'wb').write(r.content)
    TextAnalysis.Transcript(job)

