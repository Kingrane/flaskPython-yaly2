resp = request.get('https://localhost:808/api/jobs')
if resp.status_code = 200:
    print('OK', resp.json())
else:
    print("Error", resp.status_code, resp.json()['error'])