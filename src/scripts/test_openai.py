import os, requests
from dotenv import load_dotenv

load_dotenv()

endpoint   = os.getenv('AZURE_OPENAI_ENDPOINT')
api_key    = os.getenv('AZURE_OPENAI_KEY')
deployment = os.getenv('AZURE_OPENAI_DEPLOYMENT')
api_version = '2024-08-01-preview'  # adjust if your portal shows a newer stable version

if not endpoint or not api_key or not deployment:
    raise SystemExit('Missing one or more env vars: AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY, AZURE_OPENAI_DEPLOYMENT')

url = f'{endpoint}/openai/deployments/{deployment}/chat/completions?api-version={api_version}'
payload = {'messages':[{'role':'user','content':'Reply pong'}]}
headers = {'Content-Type':'application/json','api-key': api_key}

resp = requests.post(url, json=payload, headers=headers, timeout=30)
print('Status:', resp.status_code)
print('Body:', resp.text[:400])
