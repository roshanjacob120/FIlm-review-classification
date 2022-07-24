def rotten(filmname):
 import requests
 from bs4 import BeautifulSoup,SoupStrainer
#scraping from rotten tomatoes
 
 filmname=filmname.replace(" ","_")
 website_url="https://www.rottentomatoes.com/m/"+str(filmname)+"/reviews?type=user"
 session_object = requests.Session()
 html_text=session_object.get(website_url).text
 w1=SoupStrainer('div',{'id': 'movieUserReviewsContent'})
 soup=BeautifulSoup(html_text,'lxml',parse_only=w1)
 reviews=soup.find_all('p',class_="audience-reviews__review")

 with open('test.txt','w') as f:
   for review in reviews:
     reviewtext=review.text
     reviewtext=reviewtext.replace("\n","")
     f.write(f"{reviewtext}")
     f.write("\n")



     

