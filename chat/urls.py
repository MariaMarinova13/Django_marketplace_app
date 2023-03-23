from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [

    path('<id>/', views.new_chat, name='new_chat'),
    path('', views.inbox, name='inbox'),
    path('detail_chat/<int:id>/', views.detail_chat, name='detail_chat'),
]