#!/usr/bin/env python
'''
@author: Lilian Weng (lilian.wengweng@gmail.com)
'''
from bs4 import BeautifulSoup
from constants import *
from time import gmtime, strftime
import urllib2
import sys
import re
import random
import time
import smtplib

from Bag import Bag, BagSet

import smtplib
from email.mime.text import MIMEText

def send_email(new_bag_str):
    text = URL_NM_SALE_BAG + "\n" + \
            strftime("%Y-%m-%d %H:%M:%S", gmtime()) + \
            new_bag_str
    msg = MIMEText(text)

    msg['Subject'] = "NM new handbag sales"
    msg['From'] = FROM_EMAIL
    msg['To'] = ','.join(TO_EMAILS)

    s = smtplib.SMTP(SMTP_HOST)
    s.sendmail(FROM_EMAIL, TO_EMAILS, msg.as_string())
    s.quit()


def parse_a_page(url):
    bags = BagSet()
    try:
        response = urllib2.urlopen(url)
        html_source = response.read()
        soup = BeautifulSoup(html_source)
        divs = soup.findAll('div', attrs={'class': 'details'})
        for div in divs:
            div_str = str(div)
            div_str = div_str.replace('\n', '')
            div_str = re.sub('\s+', ' ', div_str)
            bags.add( Bag(div_str) )
    except:
        print '[ERROR]', sys.exc_info()

    return bags


if __name__ == '__main__':
    last_bags = BagSet()
    new_bags = BagSet()
    fout = open("nm_sale_handbags.dat", "a")
    while True:
        cur_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        cur_bags = parse_a_page(URL_NM_SALE_BAG)
        for b in cur_bags.bags:
            if not last_bags.exist(b):
                new_bags.add(b)

        if len(new_bags.bags) > 0:
            print cur_time, 'Send email!'
            # Set up the email here
            send_email( str(new_bags) )
            print >> fout, new_bags
        else:
            print cur_time, 'No new bag!'

        # Sleep for a while
        sleep_sec = random.randint(int(DURATION*4/5), DURATION)
        # sleep_sec = DURATION
        time.sleep(sleep_sec)

        new_bags = BagSet()
        last_bags = cur_bags


