#!/usr/bin/env python
'''
Class: Bag
@author: Lilian Weng (lilian.wengweng@gmail.com)
'''
from bs4 import BeautifulSoup
from constants import *
import sys
import re

class Bag(str):
    def __init__(self, div_str):
        soup = BeautifulSoup(div_str.lower())

        divs = soup.findAll('a', attrs={'class':'recordtextlink'})
        self.brand = divs[0].get_text().strip()
        self.name = divs[1].get_text().strip()
        self.link = URL_NM + divs[0]['href']

        p_divs = soup.findAll('p', attrs={'class':'priceadorn'})

        self.orig_price = int(re.sub('[$|,]+', '', p_divs[0].get_text().split(':')[1]))
        self.cur_price = int(re.sub('[$|,]+', '', p_divs[1].get_text().split(':')[1]))
        self.discount = int((self.orig_price-self.cur_price)*100/self.orig_price)

        self.id = self.brand.replace(' ','-') + '-' + self.name.replace(' ','-')


    def __str__(self):
        s = "[{0}] {1}: ${2}->${3} ({4}%)\n{5}\n".format(
                self.brand.capitalize(), 
                self.name.capitalize(), 
                self.orig_price, 
                self.cur_price,
                int((self.orig_price-self.cur_price)*100/self.orig_price),
                self.link
            )
        return s


class BagSet():
    def __init__(self):
        self.bags = []
        self.bag_ids = set()

    def add(self, bag):
        if not bag.id in self.bag_ids:
            self.bags.append(bag)
            self.bag_ids.add(bag.id)

    def exist(self, bag):
        if bag.id in self.bag_ids:
            return True
        else:
            return False

    def __str__(self):
        s = ""
        sorted_bags = sorted(self.bags, key=lambda x:x.discount, reverse=True)
        for b in sorted_bags:
            s += str(b) + "\n"
        return s

    def __bool__(self):
        if not self.bags:
            return False
        else:
            return True


    
