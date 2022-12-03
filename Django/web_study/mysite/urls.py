from django.urls import path

from mysite import views

app_name = 'mysite'

urlpatterns = [
    path('', views.index, name='index'), 
    path('blog/', views.blog, name="blog"),
    path('blog/<int:pk>/',views.posting, name="posting"),
    path('blog/new_post/', views.new_post, name="new_post"),
    path('blog/food_list/', views.food_list, name="food_list"),
    path('blog/food_list1/', views.food_list1, name="food_list1"),
    path('blog/agree/', views.agree, name='agree'),
    path('blog/map/', views.map, name='map'),

    path('blog/weather/', views.weather, name='weather'),
    path('blog/molar/', views.molar, name='molar'),
    path('blog/test/', views.test, name='test'),

    #메뉴
    path('blog/map/', views.map, name='map'),
    path('blog/map/gotowork', views.gotowork, name='gotowork'),
    path('blog/map/gotowork', views.gunae, name='gunae'),
    path('blog/map/rol', views.rol, name='rol'),
    path('blog/map/dol', views.dol, name='dol'),
    path('blog/map/lee', views.lee, name='lee'),
    path('blog/map/mak', views.mak, name='mak'),
    path('blog/map/mij', views.mij, name='mij'),
    path('blog/map/bac1', views.bac1, name='bac1'),
    path('blog/map/bac2', views.bac2, name='bac2'),
    path('blog/map/bac3', views.bac3, name='bac3'),
    path('blog/map/bon', views.bon, name='bon'),
    path('blog/map/bun', views.bun, name='bun'),
    path('blog/map/bac4', views.bac4, name='bac4'),
    path('blog/map/bac5', views.bac5, name='bac5'),
    path('blog/map/sae', views.sae, name='sae'),
    path('blog/map/sun', views.sun, name='sun'),
    path('blog/map/yuk', views.yuk, name='yuk'),
    path('blog/map/yeo', views.yeo, name='yeo'),
    path('blog/map/one', views.one, name='one'),
    path('blog/map/ins', views.ins, name='ins'),
    path('blog/map/jes', views.jes, name='jes'),
    path('blog/map/han', views.han, name='han'),
    path('blog/map/hon', views.hon, name='hon'),
    
    # path('blog/predict/', views.predict_model, name='predict_model'),
    path('blog/weather/', views.weather, name='weather'),

]