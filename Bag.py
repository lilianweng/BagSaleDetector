#!/usr/bin/env python
'''
Class: Bag
@author: Lilian Weng (lilian.wengweng@gmail.com)
'''
from bs4 import BeautifulSoup

class Bag(str):
    def __init__(self, div_str):
        soup = BeautifulSoup(div_str.lower())
        divs = soup.findAll('a', attrs={'class','recordtextlink'})
        self.brand = divs[0].get_text().strip()
        self.name = divs[1].get_text().strip()

        p_divs = soup.findAll('p', attrs={'class','priceadorn'})
        self.orig_price = p_divs[0].get_text().replace(' ','')
        self.cur_price = p_divs[1].get_text().replace(' ','')

        self.id = self.brand.replace(' ','-') + '-' + self.name.replace(' ','-')


    def __str__(self):
        s = "{0} ${1}, ${2}\n".format(
                self.id, 
                self.orig_price, 
                self.cur_price
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
        if not bag.id in self.bag_ids:
            return False
        else:
            return True

    def existAndAdd(self, bag):
        if not bag.id in self.bag_ids:
            self.add(bag)
            return False
        else:
            return True

    def __str__(self):
        s = ""
        for b in self.bags:
            s += str(b)
        return s

    def __bool__(self):
        if not self.bags:
            return False
        else:
            return True


    