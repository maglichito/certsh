import getopt, sys
import argparse
import colorama
from colorama import Fore, Back, Style
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


# Checking if argument -t/--target is passed
parser = argparse.ArgumentParser(prog='base_maker',
                                 description=f'{Fore.LIGHTRED_EX}CERTSH - Automated procces of finding subdomains on crt.sh',
                                 epilog=f'{Fore.YELLOW}Example: python3 certsh.py -t www.example.com',
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-t','--target',required=True)
args = parser.parse_args()

#Target
target = args.target

# Getting Chrome as a browser
option = Options()
option.headless = True
browser = webdriver.Firefox(executable_path="./geckodriver",options=option)

# URL
u = 'https://crt.sh/'

# Opening browser and getting to url
browser.get(u)

argv = sys.argv[1:]
def search():
    search_box = browser.find_element_by_xpath("//form/input[@type='text']")
    search_box.send_keys(target)
    search_box.submit()
    xpath = "/html/body/table[2]/tbody/tr/td/table/tbody/tr/td[5]"
    rows = browser.find_elements_by_xpath(xpath)
    print(rows)
    for row in rows[1:]:
        print(row.text)
search()