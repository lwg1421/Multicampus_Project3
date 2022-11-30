from django.urls import path

from mysite import views

app_name = 'mysite'

urlpatterns = [
    path('', views.index, name='index'), 
    path('blog/', views.blog, name="blog"),
    path('blog/<int:pk>/',views.posting, name="posting"),
    path('blog/new_post/', views.new_post, name="new_post"),
    path('blog/extract/', views.extract),
    path('blog/food_list/', views.food_list, name="food_list"),
    path('blog/agree/', views.agree, name='agree'),
    path('blog/map/', views.map, name='map'),
    path('blog/predict/', views.predict_model, name='predict_model'),
]
