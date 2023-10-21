import os,random
import os, sys, re, requests, bs4, time, random, json, string

from bs4 import BeautifulSoup
import os,sys,time,json,random,re,string,platform,base64,uuid

from bs4 import BeautifulSoup as sop

from bs4 import BeautifulSoup

import requests as ress

from datetime import date

from datetime import datetime

from time import sleep

from os import system as s

from time import sleep as waktu
from datetime import datetime

##----------[ PEH ]----------###
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
GREEN ='\x1b[38;5;46m'
RED = '\x1b[38;5;46m'
new = '\x1b[38;5;46m'
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
R = '{RED}' 
G = '{GREEN}' 
Y = '\033[1;33m' 
Q = '\033[1;37m'
T = '\033[1;34m'
x = '\33[m' 
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
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
###----------[ ANSII COLOR STYLE ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
N = '\x1b[0m'	# WARNA MATI
PT = '\x1b[1;97m' # PUTIH TEBAL
MT = '\x1b[1;91m' # MERAH TEBAL
HT = '\x1b[1;92m' # HIJAU TEBAL
KT = '\x1b[1;93m' # KUNING TEBAL
BT = '\x1b[1;94m' # BIRU TEBAL
UT = '\x1b[1;95m' # UNGU TEBAL
OT = '\x1b[1;96m' # BIRU MUDA TEBAL
D5 ='\33[0;41m'
###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
ORANGE = '\033[1;35m'
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
N = '\x1b[0m'	# WARNA MATI
PT = '\x1b[1;97m' # PUTIH TEBAL
MT = '\x1b[1;91m' # MERAH TEBAL
HT = '\x1b[1;92m' # HIJAU TEBAL
KT = '\x1b[1;93m' # KUNING TEBAL
BT = '\x1b[1;94m' # BIRU TEBAL
UT = '\x1b[1;95m' # UNGU TEBAL
OT = '\x1b[1;96m' # BIRU MUDA TEBAL
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as panel
from rich.panel import Panel as nel
from rich.progress import track
from time import sleep
from rich import print as cetak
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.panel import Panel
from rich.markdown import Markdown as mark
from rich.columns import Columns
from rich.columns import Columns as col
from rich.tree import Tree
from rich import print as rprint
from rich import print as prints
from rich import pretty
#from rich.console import Console
from rich.console import Console as sol
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.text import Text as tekz

#################################
# SHAWPON SP SHAWPON
#################################
import os,sys,time,json,random,re,string,platform,base64,uuid

from bs4 import BeautifulSoup as sop

from bs4 import BeautifulSoup

import requests as ress

from datetime import date

from datetime import datetime

from time import sleep

from os import system as s

from time import sleep as waktu


### SERVER METRO ###

A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
###----------[ ANSII COLOR STYLE ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
N = '\x1b[0m'	# WARNA MATI
PT = '\x1b[1;97m' # PUTIH TEBAL
MT = '\x1b[1;91m' # MERAH TEBAL
HT = '\x1b[1;92m' # HIJAU TEBAL
KT = '\x1b[1;93m' # KUNING TEBAL
BT = '\x1b[1;94m' # BIRU TEBAL
UT = '\x1b[1;95m' # UNGU TEBAL
OT = '\x1b[1;96m' # BIRU MUDA TEBAL
D5 ='\33[0;41m'
###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
ORANGE = '\033[1;35m'
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
N = '\x1b[0m'	# WARNA MATI
PT = '\x1b[1;97m' # PUTIH TEBAL
MT = '\x1b[1;91m' # MERAH TEBAL
HT = '\x1b[1;92m' # HIJAU TEBAL
KT = '\x1b[1;93m' # KUNING TEBAL
BT = '\x1b[1;94m' # BIRU TEBAL
UT = '\x1b[1;95m' # UNGU TEBAL
OT = '\x1b[1;96m' # BIRU MUDA TEBAL

###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
SPBD_RECORD = '\033[1;91m'

spbd_W = '\033[1;97m'

SP_BDGROUP = '\033[1;32m' 

SP_BD_YT = '\033[1;33m'

SPBD_BLUG = '\033[1;34m'
P = '\x1b[1;97m' # PUTIH
faff = 'x1b[38;5;46m'
M = '\x1b[1;91m' # MERAH
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI

A = '\x1b[1;90m' # WARNA ABU ABU

BN = '\x1b[1;107m' # BELAKANG PUTIH

BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT

BP = '\x1b[1;105m' # BELAKANG PINK

BB = '\x1b[1;104m' # BELAKANG BIRU

BK = '\x1b[1;103m' # BELAKANG KUNING

BH = '\x1b[1;102m' # BELAKANG HIJAU

BM = '\x1b[1;101m' # BELAJANG MERAH

BA = '\x1b[1;100m' # BELAKANG ABU ABU
SPBD_ID = '\033[1;35m'
facebook = random.choice([SPBD_ID,SP_BD_YT,SPBD_RECORD,O,A,K])
OK_ID = random.choice([SPBD_ID,SP_BD_YT,SPBD_RECORD])

BN = '\x1b[1;107m' 

BBL = '\x1b[1;106m' 

BP = '\x1b[1;105m' 

BB = '\x1b[1;104m' 

BK = '\x1b[1;103m' 

BH = '\x1b[1;102m' 

BM = '\x1b[1;101m' 

BA = '\x1b[1;100m' 
RED = '\033[1;91m'

WHITE = '\033[1;97m'
SPBD_ID = '\033[1;35m'
SPBD = '\033[1;32m' #

YELLOW = '\033[1;33m'

BLUE = '\033[1;34m'

ORANGE = '\033[1;35m'

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI

A = '\x1b[1;90m' # WARNA ABU ABU

BN = '\x1b[1;107m' # BELAKANG PUTIH

BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT

BP = '\x1b[1;105m' # BELAKANG PINK

BB = '\x1b[1;104m' # BELAKANG BIRU

BK = '\x1b[1;103m' # BELAKANG KUNING

BH = '\x1b[1;102m' # BELAKANG HIJAU

BM = '\x1b[1;101m' # BELAJANG MERAH

BA = '\x1b[1;100m' # BELAKANG ABU ABU

###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
SPBD_RECORD = '\033[1;91m'

spbd_W = '\033[1;97m'

SP_BDGROUP = '\033[1;32m' 

SP_BD_YT = '\033[1;33m'

SPBD_BLUG = '\033[1;34m'
P = '\x1b[1;97m' # PUTIH
faff = 'x1b[38;5;46m'
M = '\x1b[1;91m' # MERAH
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI

A = '\x1b[1;90m' # WARNA ABU ABU

BN = '\x1b[1;107m' # BELAKANG PUTIH

BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT

BP = '\x1b[1;105m' # BELAKANG PINK

BB = '\x1b[1;104m' # BELAKANG BIRU

BK = '\x1b[1;103m' # BELAKANG KUNING

BH = '\x1b[1;102m' # BELAKANG HIJAU

BM = '\x1b[1;101m' # BELAJANG MERAH

BA = '\x1b[1;100m' # BELAKANG ABU ABU
SPBD_ID = '\033[1;35m'
facebook = random.choice([SPBD_ID,SP_BD_YT,SPBD_RECORD,O,A,K])
OK_ID = random.choice([SPBD_ID,SP_BD_YT,SPBD_RECORD])

BN = '\x1b[1;107m' 

BBL = '\x1b[1;106m' 

BP = '\x1b[1;105m' 

BB = '\x1b[1;104m' 

BK = '\x1b[1;103m' 

BH = '\x1b[1;102m' 

BM = '\x1b[1;101m' 

BA = '\x1b[1;100m' 
RED = '\033[1;91m'

WHITE = '\033[1;97m'
SPBD_ID = '\033[1;35m'
SPBD = '\033[1;32m' #

YELLOW = '\033[1;33m'

BLUE = '\033[1;34m'

ORANGE = '\033[1;35m'
now = datetime.now()

dt_string = now.strftime("%H:%M")

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

today = date.today() 
P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI

A = '\x1b[1;90m' # WARNA ABU ABU

BN = '\x1b[1;107m' # BELAKANG PUTIH

BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT

BP = '\x1b[1;105m' # BELAKANG PINK

BB = '\x1b[1;104m' # BELAKANG BIRU

BK = '\x1b[1;103m' # BELAKANG KUNING

BH = '\x1b[1;102m' # BELAKANG HIJAU

BM = '\x1b[1;101m' # BELAJANG MERAH

BA = '\x1b[1;100m' # BELAKANG ABU ABU
os.system('clear')
ugen1=[]
ugen2=[]
ugen3=[]
ugen4=[]
ugenX=[]
rug=[]
fMal=[]
#-------------logo-----------------#
from rich.table import Table as me

from rich.console import Console as sol

from bs4 import BeautifulSoup as sop

from concurrent.futures import ThreadPoolExecutor as tred

from rich.console import Group as gp

from rich.panel import Panel as nel

import base64

from rich.markdown import Markdown as mark

from rich.columns import Columns as col

from rich import pretty

from rich.text import Text as tekz

pretty.install()
CON=sol()
def print(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.001)
logo = ("""\x1b[1;94m┌\033[0;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[1;94m┐
\033[0;92m│\x1b[1;93m    _____ _____        ____  _____ \033[0;92m          │
\033[0;92m│\x1b[1;93m   / ____|  __ \      |  _ \|  __ \ \033[0;92m         │
\033[0;92m│\x1b[1;93m  | (___ | |__) |_____| |_) | |  | |\033[0;92m         │
\033[0;92m│\x1b[1;93m   \___ \|  ___/______|  _ <| |  | |\033[0;92m         │
\033[0;92m│\x1b[1;93m   ____) | |          | |_) | |__| |\033[0;92m         │
\033[0;92m│\x1b[1;93m  |_____/|_|          |____/|_____/ \033[0;92m         │
\x1b[1;94m└\033[0;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[1;94m┘
\x1b[1;94m┌\033[0;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[1;94m┐
\033[0;92m│\33[0;41m              BANGLADESHI TEAM               \033[0;92m│
\x1b[1;94m└\033[0;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[1;94m┘\n""")
Shawponx = input(f'\x1b[38;5;46m╰─> \x1b[1;95m𝙔𝙊𝙐𝗥 𝙉𝘼𝙈𝙀 {x}> \033[93m')
def GF():
	wel=f'# {Shawponx} YOUR GIRLFRINDS ID COPY KORY FB LITE E SEARCH KORO'
	
	cik2=mark(wel ,style='green')

	sol().print(cik2)
	print(f'{x}')
	print(f'{Shawponx} your girlfriend Id {YELLOW}{GIRL}')
GIRL=random.choice(['https://www.facebook.com/profile.php?id=100082180161925',
'https://www.facebook.com/profile.php?id=100075241720582',
'https://www.facebook.com/profile.php?id=100078727602108',
'https://www.facebook.com/profile.php?id=100069008023528',
'https://www.facebook.com/profile.php?id=100061412564815',
'https://www.facebook.com/virtuallydeadami',
'https://www.facebook.com/profile.php?id=61552071455991',
'https://www.facebook.com/profile.php?id=61551243772504',
'https://www.facebook.com/profile.php?id=61551230663555',
'https://www.facebook.com/shadiya.akter.184881',
'https://www.facebook.com/profile.php?id=100094659433254',
'https://www.facebook.com/profile.php?id=100090022217467',
'https://www.facebook.com/profile.php?id=100095199548021',
'https://www.facebook.com/profile.php?id=100094474761592',
'https://www.facebook.com/profile.php?id=100094773259597',
'https://www.facebook.com/profile.php?id=100094416015847',
'https://www.facebook.com/profile.php?id=100094235266029',
'https://www.facebook.com/profile.php?id=100091470273236',
'https://www.facebook.com/profile.php?id=100094713792349',
'https://www.facebook.com/profile.php?id=100090022217467',
'https://www.facebook.com/profile.php?id=100070772840003',
'https://www.facebook.com/profile.php?id=100076207006669',
'https://www.facebook.com/profile.php?id=100094261406496',
'https://www.facebook.com/profile.php?id=100094054817703',
'https://www.facebook.com/profile.php?id=100085899825498',
'https://www.facebook.com/profile.php?id=61550530378641',
'https://www.facebook.com/profile.php?id=61550495246136',
'https://www.facebook.com/lipikaxr',
'https://www.facebook.com/profile.php?id=100094924091516',
'https://www.facebook.com/profile.php?id=100094909347953',
'https://www.facebook.com/profile.php?id=100095341630877',
'https://www.facebook.com/profile.php?id=100090939925080',
'https://www.facebook.com/anurupa.2022',
'https://www.facebook.com/profile.php?id=100088068836595',
'https://www.facebook.com/profile.php?id=100093691474488',
'https://www.facebook.com/profile.php?id=100093464484050',
'https://www.facebook.com/profile.php?id=100094003810213',
'https://www.facebook.com/profile.php?id=100094754044437',
'https://www.facebook.com/profile.php?id=100084012092532',
'https://www.facebook.com/profile.php?id=100093292137593',
'https://www.facebook.com/profile.php?id=100094465284653',
'https://www.facebook.com/profile.php?id=61550031182261',
'https://www.facebook.com/profile.php?id=100095179839597',
'https://www.facebook.com/profile.php?id=100094456762122',
'https://www.facebook.com/profile.php?id=100092176804903',
'https://www.facebook.com/profile.php?id=100084794002012',
'https://www.facebook.com/profile.php?id=100094908997897',
'https://www.facebook.com/profile.php?id=100094488024819',
'https://www.facebook.com/profile.php?id=100094547589682',
'https://www.facebook.com/profile.php?id=100094063866163',
'https://www.facebook.com/profile.php?id=100094562860535',
'https://www.facebook.com/profile.php?id=61550622321017',
'https://www.facebook.com/profile.php?id=61550010308256',
'https://www.facebook.com/profile.php?id=61551221250696',
'https://www.facebook.com/profile.php?id=100094732804046',
'https://www.facebook.com/profile.php?id=100086969974456',
'https://www.facebook.com/profile.php?id=100085083327592',
'https://www.facebook.com/profile.php?id=100092842971475',
'https://www.facebook.com/profile.php?id=100083313745295',
'https://www.facebook.com/profile.php?id=100094565023579',
'https://www.facebook.com/Nipa.Org',
'https://www.facebook.com/profile.php?id=100087938715429',
'https://www.facebook.com/profile.php?id=100082336277783',
'https://www.facebook.com/profile.php?id=61551583720962',
'https://www.facebook.com/profile.php?id=61551546669614',
'https://www.facebook.com/profile.php?id=100081664636636',
'https://www.facebook.com/profile.php?id=100090270020304',
'https://www.facebook.com/profile.php?id=100091355529036',
'https://www.facebook.com/profile.php?id=100094815240277',
'https://www.facebook.com/profile.php?id=100008527547221',
'https://www.facebook.com/profile.php?id=100085287698523',
'https://www.facebook.com/profile.php?id=100092281023847',
'https://www.facebook.com/profile.php?id=100072179725779',
'https://www.facebook.com/alexsoripislam.khan',
'https://www.facebook.com/afsana.parvin.5686',
'https://www.facebook.com/profile.php?id=100095081166694' 
'https://www.facebook.com/profile.php?id=100095327286202',
'https://www.facebook.com/profile.php?id=100095473659455',
'https://www.facebook.com/profile.php?id=100095385241893',
'https://www.facebook.com/profile.php?id=100094681815212',
'https://www.facebook.com/profile.php?id=100081558310896',
'https://www.facebook.com/profile.php?id=100087231274899',
'https://www.facebook.com/israt.jahannur.984786',
'https://www.facebook.com/profile.php?id=100089918412099',
'https://www.facebook.com/profile.php?id=100092293065740',
'https://www.facebook.com/profile.php?id=100092467414234',
'https://www.facebook.com/profile.php?id=100094337468246',
'https://www.facebook.com/profile.php?id=100095062252684',
'https://www.facebook.com/profile.php?id=100093856305381',
'https://www.facebook.com/profile.php?id=61550075949269',
'https://www.facebook.com/profile.php?id=100091288706976',
'https://www.facebook.com/profile.php?id=61550988911551',
'https://www.facebook.com/profile.php?id=100093103662620',
'https://www.facebook.com/profile.php?id=100081347259576',
'https://www.facebook.com/profile.php?id=100059466514426',
'https://www.facebook.com/profile.php?id=100071517937274',
'https://www.facebook.com/profile.php?id=100093855995047',
'https://www.facebook.com/profile.php?id=100089237965710',
'https://www.facebook.com/profile.php?id=61550899595526',
'https://www.facebook.com/profile.php?id=100092563045635',
'https://www.facebook.com/profile.php?id=100079309157825',
'https://www.facebook.com/profile.php?id=100078660561921',
'https://www.facebook.com/profile.php?id=100093415030055',])
def BF():
	wel=f'# {Shawponx} YOUR BOY FRINDS ID COPY KORY FB LITE E SEARCH KORO'
	
	cik2=mark(wel ,style='green')

	sol().print(cik2)
	print(f'{x}')
	print(f'{Shawponx} your boyfriend Id {YELLOW}{BOY}')

BOY=random.choice(['https://www.facebook.com/sakep.mohbal.9',
'https://www.facebook.com/profile.php?id=100090686956092',
'https://www.facebook.com/fahim.vau.3760430',
'https://www.facebook.com/profile.php?id=100079576827093',
'https://www.facebook.com/profile.php?id=100095163572185',
'https://www.facebook.com/profile.php?id=100086782401457',
'https://www.facebook.com/profile.php?id=61550008732204',
'https://www.facebook.com/profile.php?id=100070978084322',
'https://www.facebook.com/profile.php?id=100094869401242',
'https://www.facebook.com/profile.php?id=100094626105269',
'https://www.facebook.com/profile.php?id=100093435353558',
'https://www.facebook.com/original.Typeboss.ur.father',
'https://www.facebook.com/profile.php?id=61552258362040',
'https://www.facebook.com/profile.php?id=61552074467302',
'https://www.facebook.com/salekmahmudofficial',
'https://www.facebook.com/desinerraihan',
'https://www.facebook.com/copy.link.erorr404',
'https://www.facebook.com/D3V1L.N4Y1M',
'https://www.facebook.com/DH.Alamin.Hasan01',
'https://www.facebook.com/Tutul.King.Ok.Bro',
'https://www.facebook.com/profile.php?id=100082129824201',
'https://www.facebook.com/profile.php?id=100082317137320',
'https://www.facebook.com/profile.php?id=10008365097585OK',
'https://www.facebook.com/REYAL.KING.ARIYAN.YOUR.ABBU.OK',
'https://www.facebook.com/profile.php?id=100078790283274' 
'https://www.facebook.com/profile.php?id=100078968621002',
'https://www.facebook.com/Zahin.Shossain',
'https://www.facebook.com/mdnhurhossain.hossain',
'https://www.facebook.com/mesami.6T9',
'https://www.facebook.com/ap.ananda.7906',
'https://www.facebook.com/X4JU69',
'https://www.facebook.com/ItZ.Ridoy.2k16',
'https://www.facebook.com/ridoy.official.buysell',
'https://www.facebook.com/xexiridoy2.0',
'https://www.facebook.com/ridoyahammedshanto',
'https://www.facebook.com/M1NHAJ.M1LL10N',
'https://www.facebook.com/nepalimon.013',
'https://www.facebook.com/emam.emam.90663',
'https://www.facebook.com/yeasien.ahmed.1',
'https://www.facebook.com/profile.php?id=100092209298LAGI',
'https://www.facebook.com/TODR.ABBU.LAGI',
'https://www.facebook.com/profile.php?id=61550768904398',
'https://www.facebook.com/profile.php?id=100094140836422',])
os.system('clear')
os.system("xdg-open https://facebook.com/groups/black.spammar.bd/")
class Main:
		os.system('clear')
		print(logo)
		print (f'\033[1;36m[1] [A] MAKE A GIRLFRIEND')
		print (f'\033[1;36m[2] [B] MAKE A BOY FRIEND')
		print (f'\033[1;36m[3] [C] ADMIN ID')
		print (f'\033[1;36m[4] [D] EXIT\n')
		Shawpon = input(f'\033[1;36mCHOOSE ☞︎︎︎:{x} ')
		if Shawpon in ["01","1","A","a"]:
			GF()
		if Shawpon in ["02","2","B","b"]:		
			BF()			
		if Shawpon in ["03","3","C","c"]:
			os.system("xdg-open https://www.facebook.com/original.Typeboss.ur.father")			
		if Shawpon in ["04","4","D","d"]:
			exit()
		else:
			exit()
Main()