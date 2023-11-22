import requests
from bs4 import BeautifulSoup
import openpyxl


def extrage_informatii_vesti(url,limita=5):
    raspuns=requests.get(url)

    if raspuns.status_code==200:
         soup=BeautifulSoup(raspuns.text,"html.parser")
         noutati_nume=soup.find_all("a",class_="title titleAndHeadings svelte-13ozom4    small")
         noutati_ora=soup.find_all("div",class_="date metaFont svelte-itueop")


         informatii_noutati= []
         index=0


         for noutate_nume,noutate_ora in zip(noutati_nume,noutati_ora):
            nume=noutate_nume.get_text(strip=True)
            pret=noutate_ora.find("span").get_text(strip=True)
            informatii_noutati.append({"nume":nume,"pret":pret})
            index+=1


         if index>=limita:
                return informatii_noutati
            
         return informatii_noutati
    else:
        print("Cererea HTTP a esuat. Cod de stare:", raspuns.status_code)
        return None
    

url="https://adevarul.ro/stiri-locale/bacau"   

vesti=extrage_informatii_vesti(url,limita=5)

for i in vesti:
    nout=i["nume"]
    #ora=format(round(float(i["pret"])*100))
    print("NUme produs:",nout)
   # print("Pret:",ora)
    print()