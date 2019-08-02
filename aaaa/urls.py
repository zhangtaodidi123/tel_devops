from django.contrib import admin
from django.urls import path,re_path,include
from  aaaa import  urls
from  aaaa import views


urlpatterns = [
    path('index/',views.index),
    path('welcome',views.welcome),
    re_path('index/member-list.html/',views.list),
    re_path('index/zhexian.html/',views.zhexian),
    re_path('index/guize.html/',views.guize),
    re_path('index/jenkins.html',views.jenkins),
    re_path('index/host.html',views.host),
    re_path('member-list',views.list),
    re_path('member-add.html',views.guize1add),
    path('search_name/',views.search_name),
    path('xwdt_search/',views.xwdt_search),
    path('xwdt1_search/',views.xwdt1_search),
    re_path('index/export_all_excel',views.excel_export),
    re_path('xwdt1_search/export_all_excel',views.excel_export1),
    path('add/',views.add),
    path('add1/',views.add1),
    path('login/',views.login),
    path('/index/undefined',views.weizhi),
    path('index/undefined',views.weizhi),

]
