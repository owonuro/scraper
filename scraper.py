#scraper
import urllib, requests
from bs4 import BeautifulSoup
import logging as log
from datetime import datetime
import shelve

log.basicConfig(level=log.DEBUG, format='%(asctime)s > %(levelno)s %(message)s')

#this is the function to scrape the sites.
def dyk(url):
    diduno = []
    res = requests.get(url=url)
    if res.status_code != 200:
        print('Conection: Not successful!')
    soup =BeautifulSoup(res.content, 'html.parser')
    dyk1 =soup.find_all('ul')
    for ul in dyk1:
    #log.debug(ul)
        li1 = ul.find_all('li')
        for li in li1:
            if li != None:
                if li.text.startswith('...'):
                    diduno.append(li.text)
    return diduno



urlm = 'https://en.wikipedia.org/wiki/Portal:Mathematics'
urlte = 'https://en.wikipedia.org/wiki/Portal:Technology'
urlh ='https://en.wikipedia.org/wiki/Portal:History'
urlb = 'https://en.wikipedia.org/wiki/Portal:Biography'
urlg = 'https://en.wikipedia.org/wiki/Portal:Geography'
urls = 'https://en.wikipedia.org/wiki/Portal:Society'
urlsc ='https://en.wikipedia.org/wiki/Portal:Science'

sites =(urlm, urlh, urlte, urlb, urlg, urls, urlsc)
today = datetime.now().weekday()

savedata = shelve.open('scrap')
check=list(savedata.keys())
if len(check) ==0:
    data ={}
    data.setdefault('sday',today)
    data.setdefault('sdata',[])
    sdata=data['sdata']
    count =0
    sdata.append('DID YOU KNOW')
    diduno2 =dyk(sites[today])
    for dyk2 in diduno2:
        count +=1
        sdata.append(f'{count}> {dyk2}')
    sdata.append(f'\nSource: {sites[today]}')
    savedata['data']=data
    for data in data['sdata']:
             print(data)

    
else:
    data=savedata['data']
    if data['sday'] == today:
        for data in data['sdata']:
            print(data)
    else:
        data = {}
        data.setdefault('sday',today)
        data.setdefault('sdata',[])
        sdata=data['sdata']
        count =0
        sdata.append('DID YOU KNOW')
        diduno2 =dyk(sites[today])
        for dyk2 in diduno2:
            count +=1
            sdata.append(f'{count}> {dyk2}')
        sdata.append(f'\nSource: {sites[today]}')
        savedata['data']=data
        for data in data['sdata']:
            print(data)
savedata.close()
