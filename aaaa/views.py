from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.shortcuts import render,render_to_response,HttpResponse
from django.http import HttpResponseRedirect
from aaaa.models import User
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from datetime import datetime, timedelta
from .models import Jenkins_data



now_time = datetime.now()
utc_time = now_time - timedelta(hours=8)  # UTC只是比北京时间提前了8个小时
utc_time = utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")



'''登陆认证模块'''
def login(request):
    if request.method == "POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session["user"] = username
            response = HttpResponseRedirect("/index/")
            print("开始验证成功用户名和密码")
            return response

        else:
            return render(request,'login.html',{"error":"用户名密码错误"})
    return render(request,'login.html')


'''首页函数'''
@login_required
def index(request):
    # 取出目前数据库中的所有报警

    allalert = University.objects.get_queryset().order_by('id')

    return render(request,'index.html',{'allalert':allalert})



'''欢迎页面'''
@login_required
def welcome(request):
    username = User.objects.all()

    return render(request,'welcome.html',{"username":username,"utc_time":utc_time})



'''列表分页页面'''
@login_required
def list(request):
    article_list = University.objects.all()

    paginator = Paginator(article_list,10)  # show 2 articles per page

    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # 页码不是整数，返回第一页。
        articles = paginator.page(1)
        articles = paginator.page(paginator.num_pages)

    return render(request, 'member-list.html', {'articles': articles,'paginator':paginator})





'''jenkins函数'''
def jenkins(request):
    article_list = Jenkins_data.objects.all()
    paginator = Paginator(article_list,4)  # show 2 articles per page
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # 页码不是整数，返回第一页。
        articles = paginator.page(1)
        articles = paginator.page(paginator.num_pages)

    return render(request, 'jenkins.html', {'articles': articles,'paginator':paginator})


'''搜索功能'''
@login_required
def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'blog/errors.html', {'error_msg': error_msg})

    post_list = University.objects.filter(tel_log="张涛")
    return render(request, 'member-list.html', {'error_msg': error_msg,
                                               'post_list': post_list})

@login_required
def search_name(request):

    event_list = University.objects.filter(id='2')
    return render(request, "member-list.html", {"events": event_list})


@login_required
def xwdt_search(request):
    q=request.GET.get('q')
    error_msg= ''
    if not q:
        error_msg= '请输入关键词'
        return render(request,"member-list.html",{"error_msg":error_msg})
    post_list=University.objects.filter(hostname=q)
    return render(request, 'search-list.html', {'error_msg': error_msg,'post_list':post_list})

@login_required
def xwdt1_search(request):
    q=request.GET.get('q')
    print(q)
    error_msg= ''
    if not q:
        error_msg= '请输入关键词'
        return render(request,"jenkins.html",{"error_msg":error_msg})
    post_list=Jenkins_data.objects.filter(data=q)

    #6.22
    if post_list:
        # 创建工作薄
        ws = Workbook(encoding='utf-8')
        w = ws.add_sheet(u"数据报表第一页")
        w.write(0, 0, 'job_name')  # 第0行第一列写入内容
        w.write(0, 1, '发布总数')  # 第0行第一列写入内容
        w.write(0, 2, '生产成功数')  # 第0行第一列写入内容  行,列,value)

        w.write(0, 3, '生产回滚数')  # 第0行第一列写入内容
        w.write(0, 4, '生产失败数')  # 第0行第一列写入内容
        w.write(0, 5, '测试成功数')  # 第0行第一列写入内容

        w.write(0, 6, '测试失败数')  # 第0行第一列写入内容
        w.write(0, 7, '测试回滚数')  # 第0行第一列写入内容
        w.write(0, 8, '发布总成功数')  # 第0行第一列写入内容

        w.write(0, 9, '发布总失败数量')  # 第0行第一列写入内容
        w.write(0, 10, '发布总回滚数')  # 第0行第一列写入内容

        # 写入数据
        excel_row = 1
        for obj in post_list:
            job_name = obj.job_name
            fabu_zong = obj.fabu_all_count
            chengchan_sucuess = obj.prd_success
            chengchan_huigun = obj.prd_abort
            chengchan_faild = obj.prd_faill
            ceshi_sucuess = obj.fat_success
            ceshi_faildv = obj.fat_faill
            ceshi_huigun = obj.fat_abort
            sucess_count = obj.all_success
            fail_count = obj.all_faill
            huigun_count = obj.all_abort
            w.write(excel_row, 0, job_name)  # 第0行第一列写入内容
            w.write(excel_row, 1, fabu_zong)  # 第0行第一列写入内容
            w.write(excel_row, 2, chengchan_sucuess)  # 第0行第一列写入内容
            w.write(excel_row, 3, chengchan_huigun)  # 第0行第一列写入内容
            w.write(excel_row, 4, chengchan_faild)  # 第0行第一列写入内容
            w.write(excel_row, 5, ceshi_sucuess)  # 第0行第一列写入内容
            w.write(excel_row, 6, ceshi_faildv)  # 第0行第一列写入内容
            w.write(excel_row, 7, ceshi_huigun)  # 第0行第一列写入内容
            w.write(excel_row, 8, sucess_count)  # 第0行第一列写入内容
            w.write(excel_row, 9, fail_count)  # 第0行第一列写入内容
            w.write(excel_row, 10, huigun_count)  # 第0行第一列写入内容

            excel_row += 1
        # 检测文件是够存在
        # 方框中代码是保存本地文件使用，如不需要请删除该代码
        ###########################
        exist_file = os.path.exists("test11111111.xls")
        if exist_file:
            os.remove(r"test11111111.xls")
        ws.save("test11111111.xls")
        ############################

        sio = BytesIO()
        ws.save(sio)
        sio.seek(0)
        response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=test11111111.xls'
        response.write(sio.getvalue())
        return response


    return render(request, 'jenkins_search.html', {'error_msg': error_msg,'post_list':post_list})



@login_required
def jenkins_search(request):
    q=request.GET.get('q')
    error_msg= ''
    if not q:
        error_msg= '请输入关键词'
        return render(request,"member-list.html",{"error_msg":error_msg})
    post_list=University.objects.filter(data=q)
    return render(request, 'search-list.html', {'error_msg': error_msg,'post_list':post_list})

@login_required
def add(request):
    if request.method == 'GET':
        # 将数据库中的queren 修改为 111
        db_data = University.objects.all()
        print(db_data)
        quern = request.GET['a']

        hostname = str(quern).split()
        ipaddress = (hostname[0])
        tigger_name = hostname[1]
        print(ipaddress,tigger_name)

        University.objects.filter(hostname=ipaddress).update(queren="1")


    return render(request,'xiugai.html')




def zhexian(request):
    # week_data = Jenkins_data.objects.all().order_by("-id")[0:5]
    week_data1 = Jenkins_data.objects.values("data").order_by("-data")[0:5]
    week_data2 = Jenkins_data.objects.values("fabu_all_count").order_by("-data")[0:5]
    week_data3 = Jenkins_data.objects.values("all_success").order_by("-data")[0:5]
    week_data4 = Jenkins_data.objects.values("all_faill").order_by("-data")[0:5]
    week_data5 = Jenkins_data.objects.values("all_abort").order_by("-data")[0:5]

    for i in week_data3:
        print(i)

    return render(request,'zhexian.html',{"week_data1":week_data1,"week_data2":week_data2,"week_data3":week_data3,"week_data4":week_data4,"week_data5":week_data5})



'''报警规则板块函数'''
def guize(request):
    articles = alert_level.objects.all()

    return render(request,'guize.html',{"articles":articles})

def guize1add(request):
    return render(request,'member-add.html')

def add1(request):
    if request.method == 'GET':



        print('检测到方法为get')
        guanjianzi = request.GET['guanjianzi']
        queren = request.GET['level']

        obj =alert_level.objects.create(name=guanjianzi,level=queren)
        obj.save()

        print(queren,guanjianzi)
    return render(request,'xiugai.html')


import xlwt
from django.http import HttpResponse
from django.contrib.auth.models import User

# def excel(request):
#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="jenkins_data.xls"'
#     wb = xlwt.Workbook(encoding='utf-8')
#     ws = wb.add_sheet('jenkins_data')
#     row_num = 0
#     font_style = xlwt.XFStyle()
#     font_style.font.bold = True
#     columns = ['Username', 'First name', 'Last name', 'Email address', ]
#     for col_num in range(len(columns)):
#         ws.write(row_num, col_num, columns[col_num], font_style)
#     font_style = xlwt.XFStyle()
#     rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
#     for row in rows:
#         row_num += 1
#         for col_num in range(len(row)):
#             ws.write(row_num, col_num, row[col_num], font_style)
#     wb.save(response)
#     return response
#     # return render(request,'excel.html')


from django.http import HttpResponse
from xlwt import *
import os
from io import StringIO
from io import BytesIO
def excel_export(request):
    """
    导出excel表格
    """
    list_obj = Jenkins_data.objects.all().order_by("-id")
    if list_obj:
        # 创建工作薄
        ws = Workbook(encoding='utf-8')
        w = ws.add_sheet(u"数据报表第一页")
        w.write(0, 0, 'job_name')  # 第0行第一列写入内容
        w.write(0, 1, '发布总数')  # 第0行第一列写入内容
        w.write(0, 2, '生产成功数')  # 第0行第一列写入内容  行,列,value)

        w.write(0, 3, '生产回滚数')  # 第0行第一列写入内容
        w.write(0, 4, '生产失败数')  # 第0行第一列写入内容
        w.write(0, 5, '测试成功数')  # 第0行第一列写入内容

        w.write(0, 6, '测试失败数')  # 第0行第一列写入内容
        w.write(0, 7, '测试回滚数')  # 第0行第一列写入内容
        w.write(0, 8, '发布总成功数')  # 第0行第一列写入内容

        w.write(0, 9, '发布总失败数量')  # 第0行第一列写入内容
        w.write(0, 10, '发布总回滚数')  # 第0行第一列写入内容

        # 写入数据
        excel_row = 1
        for obj in list_obj:
            job_name = obj.job_name
            fabu_zong = obj.fabu_all_count
            chengchan_sucuess = obj.prd_success
            chengchan_huigun = obj.prd_abort
            chengchan_faild = obj.prd_faill
            ceshi_sucuess = obj.fat_success
            ceshi_faildv = obj.fat_faill
            ceshi_huigun = obj.fat_abort
            sucess_count = obj.all_success
            fail_count = obj.all_faill
            huigun_count = obj.all_abort
            w.write(excel_row, 0, job_name)  # 第0行第一列写入内容
            w.write(excel_row, 1, fabu_zong)  # 第0行第一列写入内容
            w.write(excel_row, 2, chengchan_sucuess)  # 第0行第一列写入内容
            w.write(excel_row, 3, chengchan_huigun)  # 第0行第一列写入内容
            w.write(excel_row, 4, chengchan_faild)  # 第0行第一列写入内容
            w.write(excel_row, 5, ceshi_sucuess)  # 第0行第一列写入内容
            w.write(excel_row, 6, ceshi_faildv)  # 第0行第一列写入内容
            w.write(excel_row, 7, ceshi_huigun)  # 第0行第一列写入内容
            w.write(excel_row, 8, sucess_count)  # 第0行第一列写入内容
            w.write(excel_row, 9, fail_count)  # 第0行第一列写入内容
            w.write(excel_row, 10, huigun_count)  # 第0行第一列写入内容

            excel_row += 1
        # 检测文件是够存在
        # 方框中代码是保存本地文件使用，如不需要请删除该代码
        ###########################
        exist_file = os.path.exists("test11111111.xls")
        if exist_file:
            os.remove(r"test11111111.xls")
        ws.save("test11111111.xls")
        ############################

        sio = BytesIO()
        ws.save(sio)
        sio.seek(0)
        response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=test11111111.xls'
        response.write(sio.getvalue())
        return response

def weizhi(request):
    return render(request,'index.html')


def excel_export1(request):
    """
    导出excel表格
    """
    q = request.GET.get('q')
    print("走到这里了")
    print(q)
    # list_obj = Jenkins_data.objects.all().order_by("-id")
    list_obj= Jenkins_data.objects.filter(data=q)
    return render(request,'index.html')
    # if list_obj:
    #     # 创建工作薄
    #     ws = Workbook(encoding='utf-8')
    #     w = ws.add_sheet(u"数据报表第一页")
    #     w.write(0, 0, 'job_name')  # 第0行第一列写入内容
    #     w.write(0, 1, '发布总数')  # 第0行第一列写入内容
    #     w.write(0, 2, '生产成功数')  # 第0行第一列写入内容  行,列,value)
    #
    #     w.write(0, 3, '生产回滚数')  # 第0行第一列写入内容
    #     w.write(0, 4, '生产失败数')  # 第0行第一列写入内容
    #     w.write(0, 5, '测试成功数')  # 第0行第一列写入内容
    #
    #     w.write(0, 6, '测试失败数')  # 第0行第一列写入内容
    #     w.write(0, 7, '测试回滚数')  # 第0行第一列写入内容
    #     w.write(0, 8, '发布总成功数')  # 第0行第一列写入内容
    #
    #     w.write(0, 9, '发布总失败数量')  # 第0行第一列写入内容
    #     w.write(0, 10, '发布总回滚数')  # 第0行第一列写入内容
    #
    #     # 写入数据
    #     excel_row = 1
    #     for obj in list_obj:
    #         job_name = obj.job_name
    #         fabu_zong = obj.fabu_all_count
    #         chengchan_sucuess = obj.prd_success
    #         chengchan_huigun = obj.prd_abort
    #         chengchan_faild = obj.prd_faill
    #         ceshi_sucuess = obj.fat_success
    #         ceshi_faildv = obj.fat_faill
    #         ceshi_huigun = obj.fat_abort
    #         sucess_count = obj.all_success
    #         fail_count = obj.all_faill
    #         huigun_count = obj.all_abort
    #         w.write(excel_row, 0, job_name)  # 第0行第一列写入内容
    #         w.write(excel_row, 1, fabu_zong)  # 第0行第一列写入内容
    #         w.write(excel_row, 2, chengchan_sucuess)  # 第0行第一列写入内容
    #         w.write(excel_row, 3, chengchan_huigun)  # 第0行第一列写入内容
    #         w.write(excel_row, 4, chengchan_faild)  # 第0行第一列写入内容
    #         w.write(excel_row, 5, ceshi_sucuess)  # 第0行第一列写入内容
    #         w.write(excel_row, 6, ceshi_faildv)  # 第0行第一列写入内容
    #         w.write(excel_row, 7, ceshi_huigun)  # 第0行第一列写入内容
    #         w.write(excel_row, 8, sucess_count)  # 第0行第一列写入内容
    #         w.write(excel_row, 9, fail_count)  # 第0行第一列写入内容
    #         w.write(excel_row, 10, huigun_count)  # 第0行第一列写入内容
    #
    #         excel_row += 1
    #     # 检测文件是够存在
    #     # 方框中代码是保存本地文件使用，如不需要请删除该代码
    #     ###########################
    #     exist_file = os.path.exists("test11111111.xls")
    #     if exist_file:
    #         os.remove(r"test11111111.xls")
    #     ws.save("test11111111.xls")
    #     ############################
    #
    #     sio = BytesIO()
    #     ws.save(sio)
    #     sio.seek(0)
    #     response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
    #     response['Content-Disposition'] = 'attachment; filename=test11111111.xls'
    #     response.write(sio.getvalue())
    #     return response

def host(request):
    return render(request,'host.html')