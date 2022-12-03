from django.shortcuts import render, get_object_or_404, redirect
from mysite.models import Question, Post, MenuScoreAll
from django.utils import timezone
from django.db import connection
import pymysql
import random

# 딥러닝
import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras import models, layers
from tensorflow.keras.models import load_model
import cv2
import numpy as np

# 날씨
import requests
import re
from bs4 import BeautifulSoup as bs
import pandas as pd

# 계절
import datetime


def weather(request):
    html = requests.get('https://weather.naver.com/today/09680630?cpName=KMA')
    soup = bs(html.text, 'html.parser') 

    a = soup.find('span', {'class':'weather'}).get_text()

    return render(request, 'mysite/weather.html', {'a':a})

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'mysite/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'mysite/question_detail.html', context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('mysite:detail', question_id=question.id)


# Create your views here.
def index(request):
    return render(request,'mysite/index.html')

# blog.html 페이지를 부르는 blog 함수
# blog.html 페이지를 부르는 blog 함수
def blog(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'mysite/blog.html', {'postlist':postlist})

def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'mysite/posting.html', {'post':post})

def new_post(request):
    if request.method == 'POST':
        if request.POST.get('mainphoto'):
            new_article=Post.objects.create(
                # postname=request.POST.get('postname'),
                # contents=request.POST.get('contents'),
                mainphoto= request.FILES['mainphoto'],
            )
        else:
            new_article=Post.objects.create(
                # postname=request.POST.get('postname'),
                # contents=request.POST.get('contents'),
                mainphoto= request.FILES['mainphoto'],
            )
        return redirect('/blog/food_list/')
    return render(request, 'mysite/new_post.html')


def test(request):
    a=request.get_full_path
    if request.method == 'GET':
        if request.GET.get('angry'):
            a = request.get_full_path
        elif request.GET.get('happy'):
            a = request.get_full_path
        else:
            a = request.get_full_path
    return render(request, 'mysite/test.html', {'a':a})



def molar(request):
    if request.method == 'POST':
        if request.POST.get('angry'):
            a1 = 'angry'
        elif request.POST.get('happy'):
            a1 = 'happy'
        else:
            a1 = 'sad'
        
    return render(request, 'mysite/food_list1.html')


def food_list1(request):
    if request.method == 'POST':
        if request.POST.get('angry'):
            a1 = 'angry'
        elif request.POST.get('happy'):
            a1 = 'happy'
        else:
            a1 = 'sad'

    cursor = connection.cursor()

    strSql = "SELECT * FROM mysite_post"
    result = cursor.execute(strSql)
    datas = cursor.fetchall()

    connection.commit()
    connection.close()


    arr = []
    for data in datas:
        row = {
            'id' : data[0],
            'mainphoto' : data[3]
        }
        arr.append(row)  

    ptlink = arr[-1]["mainphoto"]
    #'C:/multi_project_3/DL_Model/VGG16_BatchNor.h5'
    model = load_model('C:/multi_project_3/DL_Model/VGG16_BatchNor.h5') # 모델명
        
    roi = cv2.imread('media/{}'.format(ptlink)) # 파일 경로
    #roi = cv2.imread('media/{}'.format(arr[-1].mainphoto)) # 파일 경로
    
    w, h = 250, 250
    roi = cv2.resize(roi, (w,h), interpolation = cv2.INTER_AREA)
    roi = roi.astype('float') / 255.0
    # roi = img_to_array(roi)
    roi = np.expand_dims(roi, axis=0)
    # img = img.reshape(1,w,h,3)

    Prediction = model.predict(roi)

    #Prediction[0]   #감정별 백분율 (화남 0, 기쁨 1, 중립 2, 슬픔3)


    # percent = Prediction[0][np.argmax(Prediction)]

    result = np.argmax(Prediction)#백분율이 제일 높은 값
    

    html = requests.get('https://weather.naver.com/today/09680630?cpName=KMA')
    soup = bs(html.text, 'html.parser') 

    
    data1 = soup.find('span', {'class':'weather'}).get_text()
    if data1 == '비':
        b = '_rain'
    elif data1 == '눈':
        b = '_snow'
    else:
        b = ''
        
    
    now = datetime.datetime.now()
    if now.month == [3, 4, 5]:
        c = '_spring'
    elif now.month == [6, 7, 8]:
        c = '_summer'
    elif now.month == [9, 10, 11]:
        c = '_fall'
    else:
        c = '_winter'
        
    
    final = a1+b+c

    
    cursor2 = connection.cursor()

    strSql2 = f"SELECT * FROM menu_score_all GROUP BY restaurant ORDER BY {final} DESC limit 5"
    result2 = cursor2.execute(strSql2)
    datas2 = cursor2.fetchall()

    connection.commit()
    connection.close()

    arr2 = []
    for data in datas2:
        row2 = {
            'menu' : data[0],
            'restaurant' : data[1]
        }
        arr2.append(row2)    
    
    menu1 = arr2[0]["menu"]     
    restaurant1 = arr2[0]["restaurant"]
    menu2 = arr2[1]["menu"]     
    restaurant2 = arr2[1]["restaurant"]
    menu3 = arr2[2]["menu"]     
    restaurant3 = arr2[2]["restaurant"]
    menu4 = arr2[3]["menu"]     
    restaurant4 = arr2[3]["restaurant"]
    menu5 = arr2[4]["menu"]     
    restaurant5 = arr2[4]["restaurant"]


    return render(request, 'mysite/food_list1.html', {'arr':arr[-1], 'a1':a1, 'final':final, 'menu1':menu1, 'restaurant1':restaurant1,'menu2':menu2, 'restaurant2':restaurant2,'menu3':menu3, 'restaurant3':restaurant3,'menu4':menu4, 'restaurant4':restaurant4,'menu5':menu5, 'restaurant5':restaurant5 })

    
def food_list(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM mysite_post"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()


        arr = []
        for data in datas:
            row = {
                'id' : data[0],
                'mainphoto' : data[3]
            }
            arr.append(row)  

        ptlink = arr[-1]["mainphoto"]
        
        model = load_model('C:/multi_project_3/DL_Model/VGG16_BatchNor.h5') # 모델명
        
        roi = cv2.imread('media/{}'.format(ptlink)) # 파일 경로
        #roi = cv2.imread('media/{}'.format(arr[-1].mainphoto)) # 파일 경로
        
        w, h = 250, 250
        roi = cv2.resize(roi, (w,h), interpolation = cv2.INTER_AREA)
        roi = roi.astype('float') / 255.0
        # roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)
        # img = img.reshape(1,w,h,3)

        Prediction = model.predict(roi)

        #Prediction[0]   #감정별 백분율 (화남 0, 기쁨 1, 중립 2, 슬픔3)


        percent = Prediction[0][np.argmax(Prediction)]

        result = np.argmax(Prediction)#백분율이 제일 높은 값
        
        if result == 0:
            a = 'angry'
        elif result == 1:
            a = 'happy'
        elif result == 3:
            a = 'sad'
        else:
            return render(request, 'mysite/molar.html')
            


        html = requests.get('https://weather.naver.com/today/09680630?cpName=KMA')
        soup = bs(html.text, 'html.parser') 

        
        data1 = soup.find('span', {'class':'weather'}).get_text()
        if data1 == '비':
            b = '_rain'
        elif data1 == '눈':
            b = '_snow'
        else:
            b = ''
            
        
        now = datetime.datetime.now()
        if now.month == [3, 4, 5]:
            c = '_spring'
            season = "봄"
        elif now.month == [6, 7, 8]:
            c = '_summer'
            season = "여름"
        elif now.month == [9, 10, 11]:
            c = '_fall'
            seadon = "가을"
        else:
            c = '_winter'
            season = "겨울"
        
        final = a+c+b

        
        conn = pymysql.connect(host='localhost',
                       user='root',
                       password='0610',
                       db='new_1128',
                       charset='utf8')

        sql_column = """SELECT  COLUMN_NAME
        FROM    INFORMATION_SCHEMA.COLUMNS
        WHERE   TABLE_NAME = 'menu_score_all';"""


        with conn:
            with conn.cursor() as cur:
                cur.execute(sql_column)
                result_column = cur.fetchall()

        conn = pymysql.connect(host='localhost',
                       user='root',
                       password='0610',
                       db='new_1128',
                       charset='utf8')

        sql = "SELECT * FROM menu_score_all"

        with conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                result = cur.fetchall()
                df = pd.DataFrame(result, columns = result_column)
                

        # 조건에 따라 결정된 컬럼을 기준으로 내림차순 정렬
        df_sort = df.sort_values(('happy_fall',),ascending=False)

        # 내림차순 정렬된 df에서 메뉴명, 레스토랑명, 조건가중치열만 추출
        df_three_col = pd.DataFrame(df_sort[[("menu",),("restaurant",),("happy_fall",)]])

        df_three_col.columns = ["menu", "restaurant", "happy_fall"]

        df_three_col.reset_index(drop=True, inplace=True)


        # 가중치로 정렬했을때 상위 다섯개 레스토랑명 추출

        restaurant_list = []


        for restaurant_name in range(100):
            restaurant_list.append(df_three_col.iloc[restaurant_name,1])

        restaurant_list1 = []
        for i in range(len(restaurant_list)):
            if restaurant_list[0] != restaurant_list[i]:
                restaurant_list1.append(restaurant_list[i])
        restaurant_list2 = []
        for i in range(len(restaurant_list1)):
            if restaurant_list1[0] != restaurant_list1[i]:
                restaurant_list2.append(restaurant_list1[i])
        restaurant_list3 = []
        for i in range(len(restaurant_list2)):
            if restaurant_list2[0] != restaurant_list2[i]:
                restaurant_list3.append(restaurant_list2[i])

        restaurant_list4 = []
        for i in range(len(restaurant_list3)):
            if restaurant_list3[0] != restaurant_list3[i]:
                restaurant_list4.append(restaurant_list3[i])

        restaurant_5 = []
        restaurant_5.append(restaurant_list[0])
        restaurant_5.append(restaurant_list1[0])
        restaurant_5.append(restaurant_list2[0])
        restaurant_5.append(restaurant_list3[0])
        restaurant_5.append(restaurant_list4[0])


        # 다섯개 식당별로 데이터프레임 생성
        # 가중치 값으로 정렬된 상태로 담김
        restaurant_menu_df_1 = df_three_col.loc[df_three_col["restaurant"]==restaurant_5[0]]
        restaurant_menu_df_2 = df_three_col.loc[df_three_col["restaurant"]==restaurant_5[1]]
        restaurant_menu_df_3 = df_three_col.loc[df_three_col["restaurant"]==restaurant_5[2]]
        restaurant_menu_df_4 = df_three_col.loc[df_three_col["restaurant"]==restaurant_5[3]]
        restaurant_menu_df_5 = df_three_col.loc[df_three_col["restaurant"]==restaurant_5[4]]

        # 각 데이터프레임에서 가장 큰 가중치 값 산출
        restaurant_menu_df_1_large_score = restaurant_menu_df_1.iloc[0,2]
        restaurant_menu_df_2_large_score = restaurant_menu_df_2.iloc[0,2]
        restaurant_menu_df_3_large_score = restaurant_menu_df_3.iloc[0,2]
        restaurant_menu_df_4_large_score = restaurant_menu_df_4.iloc[0,2]
        restaurant_menu_df_5_large_score = restaurant_menu_df_5.iloc[0,2]

        # 각 식당별로 가장 높으면서 동일한 가중치를 가진 메뉴들을 담을 덩어리 생성
        restaurant_menu_df_1_list = list(restaurant_menu_df_1.loc[restaurant_menu_df_1["happy_fall"]==restaurant_menu_df_1_large_score]["menu"])
        restaurant_menu_df_2_list = list(restaurant_menu_df_2.loc[restaurant_menu_df_2["happy_fall"]==restaurant_menu_df_2_large_score]["menu"])
        restaurant_menu_df_3_list = list(restaurant_menu_df_3.loc[restaurant_menu_df_3["happy_fall"]==restaurant_menu_df_3_large_score]["menu"])
        restaurant_menu_df_4_list = list(restaurant_menu_df_4.loc[restaurant_menu_df_4["happy_fall"]==restaurant_menu_df_4_large_score]["menu"])
        restaurant_menu_df_5_list = list(restaurant_menu_df_5.loc[restaurant_menu_df_5["happy_fall"]==restaurant_menu_df_5_large_score]["menu"])


        menu1 = random.choice(restaurant_menu_df_1_list)
        menu2 = random.choice(restaurant_menu_df_2_list)
        menu3 = random.choice(restaurant_menu_df_3_list)
        menu4 = random.choice(restaurant_menu_df_4_list)
        menu5 = random.choice(restaurant_menu_df_5_list)

        restaurant1 = df_three_col.loc[df_three_col["menu"]==menu1]["restaurant"].values[0]
        restaurant2 = df_three_col.loc[df_three_col["menu"]==menu2]["restaurant"].values[0]
        restaurant3 = df_three_col.loc[df_three_col["menu"]==menu3]["restaurant"].values[0]
        restaurant4 = df_three_col.loc[df_three_col["menu"]==menu4]["restaurant"].values[0]
        restaurant5 = df_three_col.loc[df_three_col["menu"]==menu5]["restaurant"].values[0]

        d= []
        e= []
        f=[]

        d.append(menu1)
        d.append(menu2)
        d.append(menu3)
        d.append(menu4)
        d.append(menu5)           
        e.append(restaurant1)
        e.append(restaurant2)
        e.append(restaurant3)
        e.append(restaurant4)
        e.append(restaurant5)
        for i in range(1,len(d)+1):
                i =+i
                f.append(i)
        folist = zip(f, d, e)


    except:
        connection.rollback()
        print("Failed selecting in DB")
    

    return render(request, 'mysite/food_list.html', {'arr':arr[-1],"season":season,'percent':percent,'a':a,'b':b,'c':c, 'd':d, 'e':e, 'folist': folist, 'final':final})

#지도 불러오기 함수
#고투웍
def gotowork(request):
    return render(request,'mysite/고투웍map.html')
#구내식당
def gunae(request):
    return render(request,'mysite/구내식당map.html')
#롤링파스타
def rol(request):
    return render(request,'mysite/롤링파스타map.html')
#돌배기집
def dol(request):
    return render(request,'mysite/돌배기집map.html')
#리춘식당
def lee(request):
    return render(request,'mysite/리춘시장map.html')
#막이오름
def mak(request):
    return render(request,'mysite/막이오름map.html')
#미정국수
def mij(request):
    return render(request,'mysite/미정국수map.html')
#백스비빔밥
def bac1(request):
    return render(request,'mysite/백S비빔밥map.html')
#백스비어
def bac2(request):
    return render(request,'mysite/백스비어map.html')
#백철판
def bac3(request):
    return render(request,'mysite/백철판0410map.html')
#본가
def bon(request):
    return render(request,'mysite/본가map.html')
#분식9단
def bun(request):
    return render(request,'mysite/분식9단map.html')
#빽다방
def bac4(request):
    return render(request,'mysite/빽다방map.html')
#빽보이 피자
def bac5(request):
    return render(request,'mysite/빽보이피자map.html')
#새마을 식당
def sae(request):
    return render(request,'mysite/새마을식당map.html')
#성성식당
def sun(request):
    return render(request,'mysite/성성식당map.html')
#역전우동
def yuk(request):
    return render(request,'mysite/역전우동0410map.html')
#연돈볼카츠
def yeo(request):
    return render(request,'mysite/연돈볼카츠map.html')
#원조쌈밥집
def one(request):
    return render(request,'mysite/원조쌈밥집map.html')
#인생설렁탕
def ins(request):
    return render(request,'mysite/인생설렁탕map.html')
#제순식당
def jes(request):
    return render(request,'mysite/제순식당map.html')
#한신포차
def han(request):
    return render(request,'mysite/한신포차map.html')
#홍콩반점
def hon(request):
    return render(request,'mysite/홍콩반점0410map.html')


def agree(request):
    return render(request,'mysite/agree.html')

def map(request):
    return render(request,'mysite/map.html')

