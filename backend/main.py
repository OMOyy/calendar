import requests

login_url = 'https://192.168.251.238:10003/?launchApp=SYNO.SDS.Office.Sheet.Application&launchParam=link%3D734604527119937718#tid=5'
excel_url = 'https://192.168.251.238:10003/oo/r/734604527119937718#tid=5'

payload = {
    'username': '039509',
    'password': 'Passion05'
}

with requests.Session() as session:
    session.post(login_url, data=payload)
    response = session.get(excel_url)

with open('output.xlsx', 'wb') as f:
    f.write(response.content)