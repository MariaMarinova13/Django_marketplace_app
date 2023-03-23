from django.urls import path
from main import views



urlpatterns = [
    path('', views.homepage, name='home'),
    path('home/', views.homepage, name='home'),
    path('market/', views.itemspage, name='items'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('register/', views.registerpage, name='register'),
    path('my_items/', views.dashboard, name='my_items'),
    path('market/<id>', views.detail, name='detail'),
    path('new', views.new, name='new'),
    path('<id>/delete/', views.delete, name='delete'),
    path('<id>/edit/', views.edit, name='edit'),
    path('browse/', views.browse, name='browse'),

]