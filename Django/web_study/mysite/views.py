from django.shortcuts import render, get_object_or_404, redirect
from mysite.models import Question, Post
from django.utils import timezone
from django.db import connection

import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras import models, layers
from tensorflow.keras.models import load_model
import cv2
import numpy as np


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
                postname=request.POST.get('postname'),
                contents=request.POST.get('contents'),
                mainphoto= request.FILES['mainphoto'],
            )
        else:
            new_article=Post.objects.create(
                postname=request.POST.get('postname'),
                contents=request.POST.get('contents'),
                mainphoto= request.FILES['mainphoto'],
            )
        return redirect('/blog/food_list/')
    return render(request, 'mysite/new_post.html')


def extract(request):
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
                'postname' : data[1],
                'contents' : data[2],
                'mainphoto' : data[3]
            }
            arr.append(row)         

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'mysite/extract.html', {'arr':arr[-1]})

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
                'postname' : data[1],
                'contents' : data[2],
                'mainphoto' : data[3]
            }
            arr.append(row)  

        ptlink = arr[-1]["mainphoto"]

        model = load_model('C:/multi_project_3/Django/web_study/VGG16_BatchNor.h5') # 모델명
        
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
        if result == 1:
            a = '기쁨'
        elif result == 0:
            a = '화남'
        elif result == 3:
            a = '슬픔'
        else:
            a = '몰라'



    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'mysite/food_list.html', {'arr':arr[-1],'percent':percent,'a':a})




def agree(request):
    return render(request,'mysite/agree.html')

def map(request):
    return render(request,'mysite/map.html')



def predict_model(request):
    model = load_model('C:/multi_project_3/Django/web_study/VGG16_BatchNor.h5') # 모델명

    roi = cv2.imread('C:/image/KakaoTalk_20221129_165040387.png') # 파일 경로

    w, h = 250, 250
    roi = cv2.resize(roi, (w,h), interpolation = cv2.INTER_AREA)
    roi = roi.astype('float') / 255.0
    # roi = img_to_array(roi)
    roi = np.expand_dims(roi, axis=0)
    # img = img.reshape(1,w,h,3)

    Prediction = model.predict(roi)

    Prediction[0]   #감정별 백분율 (화남 0, 기쁨 1, 중립 2, 슬픔3)

    result = np.argmax(Prediction)#백분율이 제일 높은 값
    if result == 1:
        a = '기쁨'
    elif result == 0:
        a = '화남'
    elif result == 3:
        a = '슬픔'
    else:
        a = '몰라'
    
    return render(request, 'mysite/emotion.html', {'a':a})



def model():
    model = load_model('C:/multi_project_3/Django/web_study/VGG16_BatchNor.h5') # 모델명

    roi = cv2.imread('C:/image/KakaoTalk_20221129_165040387.png') # 파일 경로

    w, h = 250, 250
    roi = cv2.resize(roi, (w,h), interpolation = cv2.INTER_AREA)
    roi = roi.astype('float') / 255.0
    # roi = img_to_array(roi)
    roi = np.expand_dims(roi, axis=0)
    # img = img.reshape(1,w,h,3)

    Prediction = model.predict(roi)

    Prediction[0]   #감정별 백분율 (화남 0, 기쁨 1, 중립 2, 슬픔3)

    result = np.argmax(Prediction)#백분율이 제일 높은 값
    if result == 1:
        a = '기쁨'
    elif result == 0:
        a = '화남'
    elif result == 3:
        a = '슬픔'
    else:
        a = '몰라'


