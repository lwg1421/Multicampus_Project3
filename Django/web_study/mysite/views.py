from django.shortcuts import render, get_object_or_404, redirect
from mysite.models import Question, Post
from django.utils import timezone
from django.db import connection





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

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'mysite/food_list.html', {'arr':arr[-1]})


def agree(request):
    return render(request,'mysite/agree.html')

def map(request):
    return render(request,'mysite/map.html')