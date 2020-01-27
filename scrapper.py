from bs4 import BeautifulSoup 
import requests
from PIL import Image 
import os
from io import BytesIO


def Scrapper(search):
   
    params= {"q":search}
    dir_name=search.replace(" ","_",).lower()
  

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
        
    r=requests.get("https://www.bing.com/images/search",params =params)
    soup =  BeautifulSoup(r.text,"html.parser")
    links= soup.findAll("a",{"class":"thumb"})
    print(len(links))
    for item in links:
        try:
            img_obj= requests.get(item.attrs["href"])
            print("Getting",item.attrs["href"])
            title=item.attrs["href"].split("/")[-1]
            try:
                img=Image.open(BytesIO(img_obj.content))
                img.save("./"+dir_name+"/"+title,img.format)
            except:
                print("Cannot Save")
        except:
            print("Cannot Parse")


if __name__=='__main__':
    
    i=input('search for:')
    Scrapper(i)
