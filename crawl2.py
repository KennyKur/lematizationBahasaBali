import requests, re
from bs4 import BeautifulSoup

def web(base_url,word):
    soup = BeautifulSoup(requests.get(base_url+word).content,"html.parser")
    # print(soup)
    text = [t.text for t in soup.select('p strong.selflink')]
    if(len(text) == 0):
        text = [t.text for t in soup.select('#related-forms p a')]

    if (len(text) == 0):
        text.append(word.replace('/','')+'None')
    return text[0]


with open('kata_dasar.txt', 'w') as f:
    kata_dasar = []
    lineList = [line.rstrip('\n') for line in open('links.txt')]
    for i in lineList:
        hasil = web('https://dictionary.basabali.org',i)
        print(hasil.lower())
        # print(i,' => ',hasil.lower())
        f.write("%s\n" % hasil.lower())
