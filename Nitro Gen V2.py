import requests
import time
import os
import uuid

# DO NOT GIVE TO ANYONE

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

    data = {"partnerUserId": str(uuid.uuid4())}

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()

        token = response.json().get('token')
        if token:
            filename = os.path.join(os.path.dirname(__file__), 'token.txt')
            codes += 1
            with open(filename, 'a') as file:
                file.write('https://discord.com/billing/partner-promotions/1180231712274387115/' + token + '\n')
            print(f'Token written to {filename} CODES GEN: {codes}')
        else:
            print('Token not found in the response JSON.')
    except requests.RequestException as e:
        print(f'Request failed: {e}')
        print(f'Response content: {response.content}')

    time.sleep(0.5)
