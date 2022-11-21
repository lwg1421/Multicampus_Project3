import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import csv

#url 전역변수 선언
#커피메뉴 크롤링
url1 = "https://paikdabang.com/menu/menu_coffee/"
#음료 메뉴 크롤링
url2 = "https://paikdabang.com/menu/menu_drink"
#아이스크림/디저트 메뉴크롤링
url3 = "https://paikdabang.com/menu/menu_dessert/"
#빡스치노 크롤링
url4 = "https://paikdabang.com/menu/menu_ccino/"

# 크롤링 함수(url:해당url, c는 div class, p는 저장할위치+파일명)
def hp(url,c,p):
    menu = []
    res = requests.get(url)
    res.raise_for_status()
    soup = bs(res.text.strip(), "html.parser")
    
    d = soup.select(c)
    for e in d:
        a = []
        print(e.text)
        a.append(e.text)
        menu.append(a)
        with open(p,"w", encoding="utf-8-sig", newline="") as f:
         writer = csv.writer(f)
        #  writer.writerow(['역전우동'])
         writer.writerows(menu)
         f.close
    return print(menu)
#크롤링 함수 끝

# df 변환함수 및 저장(path는 csv파일 불러올경로, col은 음식점이름, f는 저장할 파일경로)
def df(path,col,f):
    res_name3 =[]
    res_cate3 =[]
    df = pd.read_csv(path)
    #인덱스 리셋
    df.reset_index(inplace=True)
    #칼럼명 변경
    df.columns=[col,'메뉴판']
    #list 변환
    ef = list(df['메뉴판'])
    for q in range(len(ef)):
        res_name3.append(col)
        res_cate3.append('메뉴판')
    df2 = pd.DataFrame({"음식점명":res_name3, "메뉴명":ef})
    df2.to_csv(f, encoding="utf-8-sig")
    return print(ef)
#df 변환함수 끝

#사용예시
b = hp(url1,"p.menu_tit","g:/back1.csv")
c = df("g:/back1.csv", "back","g:/back4.csv")



    


