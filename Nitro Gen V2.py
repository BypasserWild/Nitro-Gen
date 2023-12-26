import requests
import time
import os

goob = True

codes = 0

while goob:
    url = 'https://api.discord.gx.games/v1/direct-fulfillment'
    headers = {
        'authority': 'api.discord.gx.games',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.opera.com',
        'referer': 'https://www.opera.com/',
        'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0',
    }
    data = '{"partnerUserId":"7515461c1e289882182c44ed6c884b5bd1c2e8ce61e93b14c1ca5d7d53c3d84b"}'
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        try:
            token = response.json()['token']
            filename = os.path.join(os.path.dirname(__file__), 'token.txt')
            codes = codes + 1
            with open(filename, 'a') as file:
                file.write('https://discord.com/billing/partner-promotions/1180231712274387115/' + token + '\n')
            print(f'Token written to {filename} CODES GEN : {codes}')
        except KeyError:
            print('Token not found in the response JSON.')
    else:
        print(f'Request failed with status code {response.status_code}')
        print(response.text)

    time.sleep(0.5)
