'''
Created on Dec 10, 2017

@author: krussan
'''
import urllib2
from bs4 import BeautifulSoup

class CaryGenWeb(object):
    '''
    classdocs
    '''

    BASE_URL='https://bilweb.se/sok/{}/{}?type=1'

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def scrape(self):
        print('searching for {} :: {}'.format(self.brand, self.model))
        page = urllib2.urlopen(self.BASE_URL.format(self.brand, self.model))
        soup = BeautifulSoup(page, "lxml")
        
        result = soup.find_all("div", class_="Card-content")
        
        for r in result:
            cg = CaryGenResult()
            cg.link = r.find("a", class_= "go_to_detail").get("href")
            