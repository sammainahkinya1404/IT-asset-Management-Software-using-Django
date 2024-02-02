from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns=[
        path('', views.home, name='home'),
        path('conts',views.conts,name='conts'),
        path('dash',views.dash,name='dash'),
        path('comp',views.comp,name='comp'),
        path('emp',views.emp,name='emp'),
        path('recs',views.recs,name='recs'),
        path('assets',views.assets,name='assets'),
        path('admin-login/', auth_views.LoginView.as_view(template_name='login.html'), name='admin-login'),
        path('aRep',views.aRep,name='aRep'),
        path('generate_report', views.generate_report, name='generate_report'),
        path('uRep',views.uRep,name='uRep'),
        path('generate_reportU', views.generate_reportU, name='generate_reportU'),
        path('cRep',views.cRep,name='cRep'),
        path('generate_reportCom', views.generate_reportCom, name='generate_reportCom'),
        path('catRep',views.catRep,name='catRep'),
        path('generate_reportCat', views.generate_reportCat, name='generate_reportCat'),






        
        

        

    
]