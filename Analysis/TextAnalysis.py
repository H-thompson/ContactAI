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

    with open("Analysis/swearWords.csv") as swearfile:
        reader = csv.reader(swearfile)
        swears = list(reader)

    scr = script.split()

    for word in swears[0]:
        if scr.count(word) > 0:
            negative += 1
            points -= negative
        else:
            continue

    with open("Analysis/positiveExpressions.csv") as goodFile:
        reader = csv.reader(goodFile)
        good = list(reader)

    for word in good[0]:
        if word in scr:
            positive += 1
            points += positive
        else:
            continue

    print('TOTAL POINTS: ' + str(points))