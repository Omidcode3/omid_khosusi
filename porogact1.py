# omid_khosusi

from bs4 import BeautifulSoup
import pandas as pd
import requests
import json
import re


e=requests.get("https://divar.ir/s/yazd/laptop-notebook-macbook")
y=BeautifulSoup(e.text ,"html.parser")
data=y.find("div",attrs={" class":"kt-post-card__description"})
data2=BeautifulSoup(y.text, "html.parser")
all_type=re.findall(".(.*)نو",y.text)
all_Price=re.findall("(.*)تومان",y.text)
for omid in all_type:
    print(omid)

db={"Laptop" : all_Price}
khoruje=pd.DataFrame(db)
nwashtan=pd.ExcelWriter('test.xlsx')
khoruje.to_excel(nwashtan,"sheet-tast")

#nwashtan.save()
for mmd in all_Price:
    print(mmd)
