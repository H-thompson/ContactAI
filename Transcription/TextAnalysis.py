import os
import csv
import json
import time
import requests

def Transcript(job):
    with open('Transcription/JSON/' + job + '.json', 'r') as f:
        script_dict = json.load(f)
        s = script_dict['results']['transcripts'][0]['transcript']
        ScriptAnalysis(s)

def ScriptAnalysis(script):
    points = 0
    positive = 0
    negative = 0

    swears = []
    with open("Analysis/swearWords.csv") as swearfile:
        reader = csv.reader(swearfile)
        for row in reader:
            swears.append(row)

    scr = script.split()

    for word in swears:
        if word in scr:
            negative += 1
        else:
            if negative == 0:
                break
            else:
                negative -= 1
    points += negative


file = 'QA-01'

Transcript(file)