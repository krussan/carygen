'''
Created on Dec 10, 2017

@author: krussan
'''
import urllib2
from bs4 import BeautifulSoup

class CaryGenResult(object):

    def __init__(self):
        pass   
    
class CaryGenWeb(object):
    '''
    classdocs
    '''

    BASE_URL='https://bilweb.se/sok/{}/{}?type=1&offset=0&limit=10000'

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def scrape(self):
        result = []
        
        print('searching for {} :: {}'.format(self.brand, self.model))
        page = urllib2.urlopen(self.BASE_URL.format(self.brand, self.model))
        soup = BeautifulSoup(page, "lxml")
        
        cards = soup.find_all("div", class_="Card-content")
        
        for r in cards:
            cg = CaryGenResult()
            cg.link = r.find("a", class_= "go_to_detail").get("href")
            cg.price = r.find("p", class_="Card-mainPrice").get_text()
            cg.firm = r.find("span", class_="Card-firm").get_text()
            cg.milage = -1
            cg.year = -1
            cg.city = ""
            
            data = r.find("dl", class_="Card-carData")
            
            if (data is not None):
                dd_milage = data.find("dd")
                
                if (dd_milage is not None):
                    cg.milage = dd_milage.get_text().strip()
                    
                dd_year = dd_milage.find("dd")
                
                if (dd_year is not None):
                    cg.year = dd_year.get_text()
                
            else:
                # this is probably where the data is comma separated
                cardData = r.find("div", class_="Card-carData").get_text().strip()
                dd = cardData.split(",")
                
                if (len(dd) > 0):
                    cg.year = dd[0].strip()
                    
                if (len(dd) > 1):                    
                    cg.milage = dd[1].strip()
                
                if (len(dd) > 2):
                    cg.city = dd[2].strip()
                
            print(u"{};{};{};{};{}".format(cg.link, cg.price, cg.year, cg.milage, cg.city))
            
            result.append(cg)
            
        return result