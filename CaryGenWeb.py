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


    def __init__(self, brand,model):
        '''
        Constructor
        '''
        self.brand = brand
        self.model = model
        
    def scrape(self):
        print('searching for %s :: %s' (self.brand,self.model))
        