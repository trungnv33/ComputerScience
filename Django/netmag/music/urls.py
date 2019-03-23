from django.urls import path,include
from . import views
urlpatterns=  [
    #/music/
    path(r'',views.index,name = 'index'),
    #/music/712
    path("<int:album_id>/",views.detail,name = 'detail'),
    path("<int:album_id>/favorite/",views.favorite,name = 'favorite')
]