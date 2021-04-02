from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.olx.pl/oferty/q-electrovoice/').content
soup=BeautifulSoup(html_text,'lxml')


#mess=soup.find('a',class_ ='thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink')

atags = soup.find_all('a',href =True)
links = [atag['href'] for atag in atags]


for x in range(len(links)):
    print (links[x],sep="\n")





#print(links,sep="\n")
