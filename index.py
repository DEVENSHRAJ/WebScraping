from bs4 import BeautifulSoup
import requests
import pdfkit


html_doc=open("E:\devensh\project wroks\python projects\web scaping beautiful soup\site html text.txt")
soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup.title)
#print(soup.contents)
pg_count=0
for link in soup.find_all('a'):
    #print(link,end="")
    fullstring = link.get('href')
    substring = "www.amd.gov.in"
    if fullstring != None and substring in fullstring:
        url=link.get('href')
        url=url.replace("\n","")
    #'''
        reqs = requests.get(url)
        # using the BeaitifulSoup module
        soup = BeautifulSoup(reqs.text, 'html.parser')
        # displaying the title
        # print("Title of the website is : ")

        for title in soup.find_all('title')[0]:  #hi
            #tit=repr(title.get_text())                #to get raw string
            tit=title.get_text()[3:-3].replace(":","")+".pdf"
            #print(type(tit))

            try:
                pg_count += 1
                print(pg_count)
                print(tit)
                pdfkit.from_url(url,str(pg_count)+"_"+tit)
            except:
                pass
            #finally:    #used or not not problem
            #    pass
    if pg_count==22:   #number of pages you want
        break
    #'''