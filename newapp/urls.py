from django.urls import path
from . import views

urlpatterns=[
    path('home', views.fnhome, name='home'),
    path('emea/', views.fnemea, name='emea'),
    path('login', views.fnlogin, name='login'),
    path('create', views.fncreate, name='create'),
    path('forgot', views.fnforgot, name='forgot'),
    path('product',views.fnproduct,name='product'),
    path('baabtra',views.fnbaabtra,name='baabtra'),
    path('course',views.fncourse,name='course'),
    path('contact',views.fncontact,name='contact'),
    path('boot',views.fnboot,name='boot'),
    path('master',views.fnmaster,name='master'),
    path('index',views.fnindex,name='index'),
    path('contus',views.fncontus,name='contact us'),
    path('about',views.fnabout,name='about'),
    path('java',views.fnjava,name='java'),
    path('cp',views.fncp,name='cp'),
    path('cal',views.fncal,name='cal'),
    path('django',views.fndjango,name='django'),
    path('new',views.fnnew,name='new'),
    path('form',views.fnform,name='form'),
    path('del',views.fndel,name='del'),
    path('display',views.display,name='display'),
    path('logout',views.logout,name='logout'),

    # path('submitform',views.submitform,name='submitform'),

  
   




    
]