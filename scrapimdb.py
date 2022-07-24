def imdb(filmname):
 import requests
 from bs4 import BeautifulSoup,SoupStrainer
 name=filmname
 url='https://www.imdb.com/find?q='+str(name)+'&ref_=nv_sr_sm'
 session_object = requests.Session()
 html_text=session_object.get(url).text
 w1=SoupStrainer('table',{'class': 'findList'})
 soup=BeautifulSoup(html_text,'lxml',parse_only=w1)
 link=soup.find('td',class_="result_text").a['href']
 revurl='https://www.imdb.com'+str(link)+'reviews'
 print(revurl)
 html_text=requests.get(revurl).text
 soup=BeautifulSoup(html_text,'lxml')
 reviews=soup.find_all('div','show-more__control')

 with open('test.txt','a') as f:
   for review in reviews:
     reviewtext=review.text
     reviewtext=reviewtext.replace("\n","")
     f.write(f"{reviewtext}")
     f.write("\n")
