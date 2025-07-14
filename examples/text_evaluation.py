import requests

def words_count(text):
    words = text.split()
    return (len(words))

def get_score(model_id, text, auth_token):
    payload = {'model_id':model_id, 'text':text}
    headers = {'Authorization': auth_token}

    resp = requests.post('http://skolkovo.cbrai.ru/api/v1/score', json=payload, headers=headers)

    if resp.status_code == 200:
        return resp.json()['score']
    else:
        print(f"Error acquired: {resp.status_code}, {resp.text}")
        return 'Error'

text = 'some text here'
token = 'here will be the auth token that you will receive from the project curators'

wc = words_count(text)
ARIscore = get_score('ARIEstimator', text, token)
Alinascore = get_score('AlinaEstimator', text, token)

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
res_data = {rnd_uid : {'guid':rnd_uid, 'ARIEstimator' : ARIscore, 'AlinaEstimator' : Alinascore,'words_count': wc}}
if len(data) == 0:
    ndata = res_data
else:
    ndata = data | res_data

with open(results_file, 'w', encoding='utf-8') as jsf:
    json.dump(ndata, jsf)
