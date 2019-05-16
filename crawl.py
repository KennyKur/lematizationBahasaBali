import requests
from bs4 import BeautifulSoup
def web(page,WebUrl):
    lists = []
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        # print(s)
        for link in s.findAll('a'):
            tet = link.get('title')
            # print(tet)
            tet_2 = link.get('href')
            # print(tet_2)
            lists.append(tet_2)
    return lists

hasil = web(1,'https://dictionary.basabali.org/Dictionary')

with open('links.txt', 'w') as f:
    for item in hasil:
        f.write("%s\n" % item)

