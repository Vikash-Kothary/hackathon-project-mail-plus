from bs4 import BeautifulSoup
from selenium import webdriver
from threading import Thread
import requests, time, datetime

class Email():
    def __init__(self):
        pass

class Scrape():
    def __init__(self, url):
        self.url = url
        
        res = requests.get(self.url)
        res.raise_for_status()

        self.soup = BeautifulSoup(res.text, "html.parser")

    def login(self):
        soup.find(id="Email")
     
    def run(self):
        pass
        #Tread(target = hack.getTickets)
                        
        #while datetime.datetime.now() < dateStart:
        #    time.sleep(1)
        #fillForm()

    def fillForm(self, url):
        browser = webdriver.Firefox()
        browser.get(url)
    
if (__name__ == '__main__'):
    gmail = Scrape("https://mail.google.com/")
    gmail.run()
