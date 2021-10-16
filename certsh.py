import getopt, sys
import argparse
import colorama
from colorama import Fore, Back, Style
import selenium
from selenium import webdriver   
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import warnings

# Do not want to print warnings
warnings.filterwarnings('ignore')

logo = str(f'''{Fore.GREEN}
OOOOOOOOZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$7$$$7$7777~
OOOOOOOOZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$7$$$7$7777~
OOOOOOOZOZ...,ZZZZZ=......~ZZZZ. ...IZZZ$........I$$$$$...,$$$$$.$$$$7$7.7$7777~
OOOOOOO........ZZZ... .....ZZZ........Z$=.... ...~$$$........$$$.7$$$77~.7$7777~
OOOOZZ...OZZZZZZZZ..ZZZZZZZZZ..ZZZZZ$..Z$$$Z. $$$$$$..$$$$$$$$$?.=$$$77..7$7777~
OOOOOO..ZZZZZZZZZZ..ZZZZZZZZZ..ZZZZZZ..Z$$$$..$$$$$$...$$$$$$$$?.,$$$7$..7$7777~
OOOOZ...ZZZZZZZZZZ.......ZZZZ..ZZZZZ...Z$$$$..$$$$$$$... .=$$$$?.........7$7777~
OOOOO...ZZZZZZZZZZ..,,,:ZZZZZ........:$$$$$Z..$$$$$$$$$$$....$$?.:$$$7$..7$7777~
OOOOOO..ZZZZZZZZZZ..ZZZZZZZZZ..Z$Z..=ZZ$$$$Z..Z$$$$$$$$$$$$..$$?.=$$$77..7$7777~
OOOOOO...OOZZZOZZZ..ZZZZZZZZZ..ZZZZ..,Z$$$$Z. $$$$$$?$$$$$$..$$I.?$$$7$,.7$7777~
OOOOOOO.........ZZ.........ZZ..ZZZZZ...$$$$$. $$$$$$........$$$$.7$$$77~.777777~
OOOOOOOOZOI,=OZZZZZO+:~=+IZZZZ$$ZZZZZ?:$$$$$$:$$$$$$$$$=~I7$$$$$?$$$$7$7?777777~
OOOOOOOOZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$7$$$7$7777~''')

# Checking if argument -t/--target is passed
parser = argparse.ArgumentParser(prog='base_maker',
                                 description=logo,
                                 epilog=f'{Fore.YELLOW}Example: python certsh.py -t www.example.com',
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-t','--target',required=True)
args = parser.parse_args()

print(logo)
print(f"\n")
#Target
target = args.target

# Getting Chrome as a browser
option = webdriver.ChromeOptions()
option.add_argument('headless')
browser = webdriver.Chrome('./chromedriver',options=option)

# URL
u = 'https://crt.sh/'

# Opening browser and getting to url
browser.get(u)

# Bot doing the thing ;)
def search():
    search_box = browser.find_element_by_xpath("//form/input[@type='text']")
    search_box.send_keys(target)
    search_box.submit()
    xpath = "/html/body/table[2]/tbody/tr/td/table/tbody/tr/td[5]"
    rows = browser.find_elements_by_xpath(xpath)
    for row in rows[1:]:
        print(f"{Fore.RED}"+str(row.text))
search()