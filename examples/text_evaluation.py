import requests

def words_count(text):
    words = text.split()
    return (len(words) - 2)

def get_score(model_id, text):
    payload = {'model_id':model_id, 'text':text}
    
    resp = requests.post('http://skolkovo.cbrai.ru/api/v1/score', json=payload)

    if resp.status_code == 200:
        return resp.json()['score']
    else:
        print(f"Error acquired: {resp.status_code}, {resp.text}")
        return 'Error'

text = 'Some text here'
wc = words_count(text)
ARIscore = get_score('ARIEstimator', text)
Alinascore = get_score('AlinaEstimator', text)

# save to json file if necessary
from pathlib import Path
import uuid
import json

results_file = Path(f"results.json")
try:
    with open(results_file, 'r', encoding='utf-8') as jsf:
        data = json.load(jsf)
        jsf.close()
except:
    data = {}

rnd_uid = str(uuid.uuid4())
res_data = {
    "guid" : rnd_uid,
    'ARIEstimator' : ARIscore,
    'AlinaEstimator' : Alinascore,
    'words_count': wc
}

with open(results_file, 'a', encoding='utf-8') as jsf:
    data = json.dump(data, jsf)