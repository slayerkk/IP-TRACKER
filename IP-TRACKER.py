from urllib.request import urlopen
import sys, os
os.system('clear')
#cores
vermelho = '\033[41m'
verde = '\033[42m'
nulo = '\033[0m'
verde1 = '\033[32m'
vermelho1 = '\033[31m'
azul = '\033[0;30;34m'
rosa = '\033[0;30;35m'
amarelo = '\033[33m'


print(f'''
{vermelho1} __     ______  {nulo}   {amarelo} ______   ______     ______     ______     __  __     ______     ______   {nulo} {vermelho1}─▄▀─▄▀{nulo}
{vermelho1}/\ \   /\  == \ {nulo}   {amarelo}/\__  _\ /\  == \   /\  __ \   /\  ___\   /\ \/ /    /\  ___\   /\  == \  {nulo} {vermelho1}──▀──▀{nulo}
{vermelho1}\ \ \  \ \  _-/ {nulo}   {amarelo}\/_/\ \/ \ \  __<   \ \  __ \  \ \ \____  \ \  _"-.  \ \  __\   \ \  __<  {nulo} {amarelo}█▀▀▀▀▀█▄{nulo}
{vermelho1} \ \_\  \ \_\   {nulo}   {amarelo}   \ \_\  \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\{nulo} {amarelo}█░░░░░█─█{nulo} 
{vermelho1}  \/_/   \/_/   {nulo}   {amarelo}    \/_/   \/_/ /_/   \/_/\/_/   \/_____/   \/_/\/_/   \/_____/   \/_/ /_/{nulo} {amarelo}▀▄▄▄▄▄▀▀ {nulo}''')

try:
    ip = input(f'''{amarelo}┌──({vermelho1}IP{azul}㉿{amarelo}TRACKER!{amarelo})-[{vermelho1}~{amarelo}]
└─> ''')

    if ip:
        url = f"http://ip-api.com/json/{ip}"

    request = urlopen(url)
    data = request.read().decode()

    data = eval(data)
    for i in data:
        print(f'{i} == {data[i]}')
except Exception as ex:
    print(f'Error: {ex}')