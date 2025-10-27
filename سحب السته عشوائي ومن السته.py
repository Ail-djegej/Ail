from requests import post as pp, get as gg
import random
import re
import json
from uuid import uuid4
import time
import sys
import base64
import requests
import os
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import string

# تعريف الألوان
B = "\033[1;30m"
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
Bl = "\033[1;34m"
P = "\033[1;35m"
C = "\033[1;36m"
N = "\033[1;37m"
A = '\033[2;34m'
C = '\033[1;34m'
E = '\033[1;33m'
J = "\033[1;31m"
I = '\033[1;32m'
G = '\033[1;97m'
H = "\x1b[38;5;208m"
ggc = '\x1b[38;5;208m'
X = '\033[1;33m' #اصفر
J22='\x1b[38;5;209m'
J21='\x1b[38;5;204m'
J2='\x1b[38;5;203m'
J1='\x1b[38;5;202m'
a7 = '\x1b[38;5;13m'  # وردي
a9 = '\x1b[1;37m'  # أبيض
Z = '\033[1;31m'  # أحمر
Y = '\033[1;33m'  # أصفر
F = '\033[2;32m'  # أخضر
A = '\033[2;34m'  # أزرق
C = '\033[2;35m'  # وردي
X = '\033[1;33m'  # أصفر قوي
M = '\x1b[1;37m'  # أبيض
R = '\033[1;31m'  # أحمر قوي
G = '\033[1;32m'  # أخضر قوي
B = '\x1b[38;5;208m'  # برتقالي
bee = "\033[1;38;5;223m"
peach      = "\033[1;38;5;216m"
la = "\033[1;38;5;183m"
turquoise  = "\033[1;38;5;80m"   # تركواز
rose  = "\033[1;38;5;211m"  # وردي ناعم
mint   = "\033[1;38;5;121m"  # نعناعي
B = '\x1b[38;5;208m'
a19 = '\x1b[38;5;88m'  # أحمر داكن
a4 = '\x1b[1;33m'  # أصفر
a3 = '\x1b[1;32m'  # أخضر
Z = '\033[1;31m' #احمر
a9 = '\x1b[1;37m'  # أبيض
a4 = '\x1b[1;33m'  # أصفر
a3 = '\x1b[1;32m'  # أخضر
nnn = random.choice([bee,peach,la,turquoise,rose,mint,Z,B,R])
print(nnn)
M = '\x1b[1;37m'
b = random.randint(5, 208)
bo = f'\x1b[38;5;{b}m'
j = random.randint(5, 208)
jo = f'\x1b[38;5;{j}m'

cc = {
    'red': "\033[1m\033[31m",
    'green': "\033[1m\033[32m",
    'yellow': "\033[1m\033[33m",
    'blue': "\033[1m\033[34m",
    'cyan': "\033[1m\033[36m",
    'magenta': "\033[1m\033[35m",
    'white': "\033[1m\033[37m",
    'orange': "\033[1m\033[38;5;208m",
    'reset': "\033[0m"
}

# تعريف المتغيرات العامة
hits, bad, bad2, gig, p1, bv = 0, 0, 0, 0, 0, 0
sessionid = ""
k = None
listoo = []
uid = 0
ExI = str(uuid4()).replace('-', '')
iop = (f"""\x1b[1;37m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\x1b[38;5;208m A l i \x1b[1;37m ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \x1b[38;5;205m{nnn}

          █████╗          ██╗             ██╗
         ██╔══██╗         ██║             ██║
         ███████║         ██║             ██║
         ██╔══██║         ██║             ██║
         ██║  ██║         ██║             ███████╗
         ╚═╝  ╚═╝         ╚═╝             ╚══════╝
 \033[1;33m          ¸.•´¯•.¸¸\033[2;32m IN-NO-SE-Fr-V11\033[1;33m ¸.•´¯•.¸¸
    \033[2;32m           Tle : @p_nvp • @AZ_20_30
              \033[1;38;5;121m         A l i -V11

\x1b[1;37m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\x1b[38;5;208m A l i \x1b[1;37m ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \x1b[38;5;205m
""")
def fs(id):
    global p1, sessionid
    url = f'https://i.instagram.com/api/v1/friendships/{id}/followers/?count=100&search_surface=follow_list_pag'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': f'mid=Y3bGYwALAAHNwaKANMB8QCsRu7VA; ig_did=092BD3C7-0BB2-414B-9F43-3170EAED8778; ig_nrcb=1; shbid=1685054; shbts=1675191368.6684434090; rur=CLN; ig_direct_region_hint=ATN; csrftoken=gLlFX76z8qqwDgmh8ZIp3uFhAeX4zKdO; ds_user_id=921803283; sessionid={sessionid}',
        'Sec-Ch-Prefers-Color-Scheme': 'dark',
        'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        'Sec-Ch-Ua-Full-Version-List': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.201", "Microsoft Edge";v="114.0.1823.67"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
        'X-Asbd-Id': '129477',
        'X-Csrftoken': 'gLlFX76z8qqwDgmh8ZIp3uFhAeX4zKdO',
        'X-Ig-App-Id': '936619743392459',
        'X-Ig-Www-Claim': 'hmac.AR0g7ECdkTdrXy37TE9AoSnMndccWbB1cqrccYOZSLfcb8sd',
        'X-Requested-With': 'XMLHttpRequest',
    }
    r = requests.get(url, headers=headers)
    if '{"message":"","spam":true,"status":"fail"}' in r.text:
        print('block')
        return

    try:
        for i in r.json()['users']:
            p1 += 1
            userL = i['username']
            sys.stdout.write('\r' + G + str(p1) + f'{bo}  </>  {G}' + userL + '\r')
            with open('username.txt', 'a') as f:
                f.write(userL + '\n')
    except:
        pass

    if 'HI' in listoo:
        try:
            m_id = r.json()['next_max_id']
            for i in range(9999):
                r = requests.get(f'https://i.instagram.com/api/v1/friendships/{id}/followers/?count=100&max_id=' + m_id + '&search_surface=follow_list_page', headers=headers)
                if '{"message":"","spam":true,"status":"fail"}' in r.text:
                    print('block')
                    break

                try:
                    for i in r.json()['users']:
                        p1 += 1
                        userL = i["username"]
                        sys.stdout.write('\r' + G + str(p1) + f'{bo}  </>  {G}' + userL + '\r')
                        with open('username.txt', 'a') as f:                            f.write(userL + '\n')
                    try:
                        m_id = r.json()['next_max_id']
                    except:
                        break
                except:
                    if 'challenge' in r.text:
                        break
                    else:
                        continue
        except:
            pass

def fg(id):
    global p1, sessionid
    url = f'https://i.instagram.com/api/v1/friendships/{id}/following/?count=200'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': f'mid=Y3bGYwALAAHNwaKANMB8QCsRu7VA; ig_did=092BD3C7-0BB2-414B-9F43-3170EAED8778; ig_nrcb=1; shbid=1685054; shbts=1675191368.6684434090; rur=CLN; ig_direct_region_hint=ATN; csrftoken=gLlFX76z8qqwDgmh8ZIp3uFhAeX4zKdO; ds_user_id=921803283; sessionid={sessionid}',
        'Sec-Ch-Prefers-Color-Scheme': 'dark',
        'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        'Sec-Ch-Ua-Full-Version-List': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.201", "Microsoft Edge";v="114.0.1823.67"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
        'X-Asbd-Id': '129477',
        'X-Csrftoken': 'gLlFX76z8qqwDgmh8ZIp3uFhAeX4zKdO',
        'X-Ig-App-Id': '936619743392459',
        'X-Ig-Www-Claim': 'hmac.AR0g7ECdkTdrXy37TE9AoSnMndccWbB1cqrccYOZSLfcb8sd',
        'X-Requested-With': 'XMLHttpRequest',
    }
    r = requests.get(url, headers=headers)

    if '{"message":"","spam":true,"status":"fail"}' in r.text:
        print('block')
        return

    try:
        for i in r.json()['users']:
            p1 += 1
            userL = i['username']
            sys.stdout.write('\r' + G + str(p1) + f'{bo}  </>  {G}' + userL + '\r')
            with open('username.txt', 'a') as f:
                f.write(userL + '\n')
    except:
        pass

    if 'HI' in listoo:
        try:
            m_id = r.json()['next_max_id']
            for i in range(9999):
                r = requests.get(f'https://i.instagram.com/api/v1/friendships/{id}/following/?count=200&max_id=' + m_id, headers=headers)
                if '{"message":"","spam":true,"status":"fail"}' in r.text:
                    print('block')
                    break

                try:
                    for i in r.json()['users']:
                        p1 += 1
                        userL = i["username"]
                        sys.stdout.write('\r' + G + str(p1) + f'{bo}  </>  {G}' + userL + '\r')
                        with open('username.txt', 'a') as f:                            f.write(userL + '\n')
                    try:
                        m_id = r.json()['next_max_id']
                    except:
                        break
                except:
                    if 'challenge' in r.text:
                        break
                    else:
                        continue
        except:
            pass

def delet_list():
    banner()
    try:
        txt = "username.txt"
        if os.path.exists(txt):
            os.remove(txt)
            print(f'\n - {R}𝐃𝐞𝐥𝐞𝐭𝐞𝐝')
        else:
            print(f'\n - {R}𝐅𝐢𝐥𝐞 𝐝𝐨𝐞𝐬 𝐧𝐨𝐭 𝐞𝐱𝐢𝐬𝐭')
    except Exception as e:
        print(e)

def qqq():
    global bv, uid
    memo = random.randint(100, 300)
    O = f'\x1b[38;5;{memo}m'
    while True:
        try:
            data = {
                "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
                "variables": json.dumps({
                    "id": int(random.randrange(10000, uid)), "render_surface": "PROFILE"}),
                "doc_id": "25618261841150840"
            }
            response = requests.post('https://www.instagram.com/api/graphql', headers={"X-FB-LSD": data["lsd"]}, data=data)
            username = response.json()['data']['user']['username']
            bv += 1
            sys.stdout.write('\r' + G + str(bv) + f'  {rose}number- {O} × {B}Email {G}' + username + '\r')

            with open('username.txt', 'a') as f:
                f.write(username + '\n')
        except:
            pass

def banner():
        print(iop)

def main():
    global uid, ExI

    banner()

    ExI = str(uuid4()).replace('-', '')

    print(f'''

''')

    ethan = int('1')

    if ethan == 9587:
        os.system('clear')
        delet_list()
    elif ethan == 1:
        os.system('clear')
        banner()
        print(f'''

{A}1{bo}- {N}Random Lsta

{A}2{bo}- {N}Lsta FROM USER

  ''')
        end = int(input(f'\n{A}ᴄʜᴏᴏѕᴇ ɴᴜᴍʙᴇʀ   :  {N} '))
        if end == 1:
            os.system('clear')
            banner()

            print(f'- {B} 2011, 2012, 2013, 2014, 2015, 2022 ')
            num = int(input(f'- {J}Choose to withdraw Lsta  : {G}'))
            os.system('clear')
            banner()
            if num == 2011:
                uid = 18957417
            elif num == 2012:
                uid = 257924624
            elif num == 2013:
                uid = 361365132
            elif num == 2014:
                uid = 1682665388
            elif num == 2015:
                uid = 2682665388
            elif num == 2022:
                uid = 8682665388
            else:
                print("Invalid date")
                return

            print(f"{G}The six are being Lsra")
            for _ in range(5):
                Thread(target=qqq).start()

        elif end == 2:
            os.system('clear')
            banner()
            listoo = ['HI']
            print('')
            username = str(input(f'{J}Account username {A} : {G}    '))
            password = str(input(f'{J}Account password  {A} : {G}    '))
            print('')

            url = 'https://www.instagram.com/accounts/login/ajax/'
            data = {'username': f'{username}',
                    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
                    'queryParams': '{}',
                    'optIntoOneTap': 'false'}

            headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                'content-length': '275',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'csrftoken=DqBQgbH1p7xEAaettRA0nmApvVJTi1mR; ig_did=C3F0FA00-E82D-41C4-99E9-19345C41EEF2; mid=X8DW0gALAAEmlgpqxmIc4sSTEXE3; ig_nrcb=1',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
                'x-csrftoken': 'DqBQgbH1p7xEAaettRA0nmApvVJTi1mR',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': '0',
                'x-instagram-ajax': 'bc3d5af829ea',
                'x-requested-with': 'XMLHttpRequest'
            }

            k = requests.post(url, headers=headers, data=data)
            if 'authenticated":true' in k.text or 'userId' in k.text:
                sessionid = k.cookies.get('sessionid', '')
                print(f"{G}Login successful!")
            else:
                print(f'{R}𝐁𝐀𝐃 𝐋𝐎𝐆𝐈𝐍')
                return

            user = str(input(f'{J}ᴜѕᴇʀɴᴀᴍᴇ ᴏғ ᴛʜᴇ ʟɪꜱᴛ  {A} : {G}'))
            listoo = ['HI']

            headers = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
                'Cookie': f'mid=Y3bGYwALAAHNwaKANMB8QCsRu7VA; ig_did=092BD3C7-0BB2-414B-9F43-3170EAED8778; ig_nrcb=1; shbid=1685054; shbts=1675191368.6684434090; rur=CLN; ig_direct_region_hint=ATN; csrftoken=gLlFX76z8qqwDgmh8ZIp3uFhAeX4zKdO; ds_user_id=921803283; sessionid={sessionid}',
                'Sec-Ch-Prefers-Color-Scheme': 'dark',
                'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
                'Sec-Ch-Ua-Full-Version-List': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.201", "Microsoft Edge";v="114.0.1823.67"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
                'X-Asbd-Id': '129477',
                'X-Csrftoken': 'gLlFX76z8qqwDgmh8ZIp3uFhAeX4zKdO',
                'X-Ig-App-Id': '936619743392459',
                'X-Ig-Www-Claim': 'hmac.AR0g7ECdkTdrXy37TE9AoSnMndccWbB1cqrccYOZSLfcb8sd',
                'X-Requested-With': 'XMLHttpRequest',
            }

            try:
                rs_id = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={user}", headers=headers)
                jsn3 = rs_id.json()['data']['user']
                id_tr = jsn3['id']
                print('')
                os.system('clear')
                banner()
                print('')
                print(f'''
  {A}1{J}~{C} pull From Following
  {A}2{J} ~{C}pull From followers
        ''')

                o = str(input(f"{J}Choose : {C}"))
                if o == '1':
                    os.system('clear')
                    banner()
                    fg(id_tr)
                elif o == '2':
                    os.system('clear')
                    banner()
                    fs(id_tr)
                else:
                    print('    error   ')
            except:
                print("Error getting user info")

if __name__ == "__main__":
    main()