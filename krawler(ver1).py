import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import openpyxl
import csv
import os
from selenium import webdriver

#전역변수설정(음식담기)
fs =[]
bk1=[]
bk2=[]
bk3=[]
bk4=[]
bk5=[]
bk6=[]
mk1=[]

#역전우동 메뉴
url2 = "https://udon0410.com/menu/#undefined"
res2 = requests.get(url2)
res2.raise_for_status()

soup2 = bs(res2.text, 'html.parser')
b = soup2.find_all("h2")

for j in b:
    t = []
    print(j.text)
    t.append(j.text)
    fs.append(t)
with open('yk.csv',"w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['역전우동'])
    writer.writerows(fs)
f.close
    
# 뺵다방 메뉴
#뺵다방 메뉴 크롤링
#신메뉴 크롤링
url3 = "https://paikdabang.com/menu/menu_new/"
#커피메뉴 크롤링
url4 = "https://paikdabang.com/menu/menu_coffee/"
#음료 메뉴 크롤링
url5 = "https://paikdabang.com/menu/menu_drink"
#아이스크림/디저트 메뉴크롤링
url6 = "https://paikdabang.com/menu/menu_dessert/"
#빡스치노 크롤링
url7 = "https://paikdabang.com/menu/menu_ccino/"

res3 = requests.get(url3)
res3.raise_for_status()

soup3 = bs(res3.text.strip(), "html.parser")
d = soup3.select("p.menu_tit")
for e in d:
    a = []
    print(e.text)
    a.append(e.text)
    bk1.append(a)
#파일저장    
with open('bk1.csv',"w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['뺵다방신'])
    writer.writerows(bk1)
f.close


res4 = requests.get(url4)
res4.raise_for_status()

soup4 = bs(res4.text.strip(), "html.parser")
f = soup4.select("p.menu_tit")
for g in f:
    t=[]
    print(g.text)
    t.append(g.text)
    bk2.append(t)
with open('bk2.csv',"w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['뺵다방커피'])
    writer.writerows(bk2)
    f.close

res5 = requests.get(url5)
res5.raise_for_status()    
soup5 = bs(res5.text.strip(), "html.parser")
h = soup5.select("p.menu_tit")
for j in h:
    t=[]
    print(j.text)
    t.append(j.text)
    bk3.append(j)
    with open('bk3.csv',"w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['뺵다방음료'])
        writer.writerows(bk3)
        f.close
    
res6 = requests.get(url6)
res6.raise_for_status()    
soup6 = bs(res6.text.strip(), "html.parser")
k = soup6.select("p.menu_tit")
for l in k:
    t=[]
    print(l.text)
    t.append(l.text)
    bk4.append(t)
    with open('bk4.csv',"w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['빽다방디져트'])
        writer.writerows(bk4)
        f.close
    

res7 = requests.get(url7)
res7.raise_for_status()    
soup7 = bs(res7.text.strip(), "html.parser")
o = soup7.select("p.menu_tit")
for l in o:
    t=[]
    print(l.text)
    t.append(l.text)   
    bk5.append(t)
    with open('bk5.csv',"w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['빽다방빡스치노'])
        writer.writerows(bk5)
        f.close

# #빽다방 크롤링 완료

#막이오름 크롤링
url8 = "https://www.theborn.co.kr/theborn_brand/%eb%a7%89%ec%9d%b4%ec%98%a4%eb%a6%84/#menu_list"
res8 = requests.get(url8)
res8.raise_for_status()
soup8 = bs(res8.text.strip(), 'html.parser')
q = soup8.select("div.name>p")
for l in q :
    t=[]
    print(l.text)
    t.append(l.text)
    mk1.append(t)
    with open('mk.csv',"w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['막이오름'])
        writer.writerows(mk1)
        f.close


#롤링파스타 dataframe 생성

roling = pd.DataFrame(
    {
        'pasta':['봉골레파스타','매운우삼겹오일파스타','알리오 올리오','스테이크크림파스타','해물크림파스타',
                 '매운 크림 파스타','로제크림쉬림프파스타','로제크림쉬림프파스타','까르보나라','빼쉐파스타',
                 '매운 우삼겹토마토 파스타','바질페스토 크림파스타','트러플 크림 파스타','해물 토마토 파스타',
                 '토마토 파스타'],
        'steak&Gnocchi':['포크스테이크','바지락감바스','갈릭스틱','올리브브레드','찹스테이크','버섯크림뇨끼',
                         0,0,0,0,0,0,0,0,0],
        'pizza&salad':['쉬림프베이컨피자','고르곤졸라피자','마르게리따 피자','크림치즈샐러드','그린샐러드',
                       '그릴닭가슴살샐러드','더블 매쉬드 샐러드',0,0,0,0,0,0,0,0],
        'Doria&pilaf':['우사겹도리아','쉬림프필라프','스테이크필라프','우삼겹필라프',0,0,0,0,0,0,0,0,0,0,0],
        
    }
)

#홍콩반점 메뉴판(그림파일형태라 리스트로 저장)
면류 = pd.Series(['자장면(곱)','고추짜장(곱)','짬뽕(곱)','고추짬뽕(곱)','쟁반짜장','볶음짬뽕','냉짬뽕'])
밥류 = pd.Series(['짜장밥','공기밥','짬뽕밥','고추짬뽕밥'])
튀김류 = pd.Series(['탕수육(소,중,대)','깐풍기(소,중,대)'])
기타 = pd.Series(['해물육교자','군만두','홍콩꽃빵','군만두'])


#새마을식당 
식사류 = pd.Series(['7분 돼지김치','제육볶음','불백','용암','된장바지락찌개','냉김치말이국수','멸치국수',
                 '치즈폭탄계란찜'])

s1 = pd.concat([식사류],axis=1)
s1.columns=['새마을식당']

hk = pd.concat([면류,밥류,튀김류,기타], axis=1)
hk.columns=['면류','밥류','튀김류','기타']

print(hk)


roling.to_csv("rp.csv",encoding='utf-8-sig')
hk.to_csv("hk3.csv",encoding='utf-8-sig')
s1.to_csv("s1.csv",encoding='utf-8-sig')



#파일 합치기
#디렉토리내의 파일확인

df = os.listdir('g:/kwl')
print(df)

#csv파일 변수화
a1 = "g:/kwl/bk2.csv"
a2 = "g:/kwl/bk3.csv"
a3 = "g:/kwl/bk4.csv"
a4 = "g:/kwl/bk5.csv"
a5 = "g:/kwl/rp.csv"
a6 = "g:/kwl/hk3.csv"
a7 = "g:/kwl/s1.csv"
a8 = "g:/kwl/yk.csv"
a9 = "g:/kwl/mk.csv"

#파일 합치기
# for i in range(1,10):
#     df2 = pd.concat(map(pd.read_csv,[a[i]]),ignore_index=True)
df2 = pd.concat(map(pd.read_csv,[a1, a2, a3,a4,a5,a6,a7,a8]),ignore_index=True)
print(df2)
df2.to_csv("krawler(완2).csv", encoding='utf-8-sig')

# data = pd.DataFrame()
# for i in df:
#     PATH = "G:/kwl/"+i
#     add = pd.read_csv(PATH, header=None)
#     data = pd.concat([data,add])
#     print(data.shape) #병합확인