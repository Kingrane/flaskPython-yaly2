import requests

resp = requests.get('https://localhost:808/api/jobs')
if resp.status_code == 200:
    print('OK', resp.json())
else:
    print("Error", resp.status_code, resp.json()['error'])


resp = requests.get('https://localhost:808/api/jobs/2222')
if resp.status_code == 200:
    print('OK', resp.json())
else:
    print("Error", resp.status_code, resp.json()['error'])


resp = requests.get('https://localhost:808/api/jobs/qweerwt')
if resp.status_code == 200:
    print('OK', resp.json())
else:
    print("Error", resp.status_code, resp.json()['error'])
