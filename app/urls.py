from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('user/update',views.update,name='update'),
    path('user/<str:name>',views.user,name='user'),
    path('user',views.user1,name='user1'),
]
