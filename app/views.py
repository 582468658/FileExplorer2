import markdown
from markdown.extensions.toc import TocExtension
from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, response
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app import models
from app.models import UserInfo
from app import check_code
from io import BytesIO
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.utils.text import slugify
from .models import Post, Category, Tag



def register(request):
    error_msg=""
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        teamDirect = {0: 'DQA部门', 1: '产品合规', 2: '体系组', 3: '可靠性保证', 4: '标准化实验室', 5: '硬件测试', 6: '软件测试'}
        userId = request.POST.get('gonghao')
        password = request.POST.get('pass')
        repassword = request.POST.get('repass')
        username = request.POST.get('username')
        L_team = request.POST.get('team')
        L_team = teamDirect[L_team]
        post_check_code = request.POST.get('check_code')
        session_check_code = request.session['check_code']
        if post_check_code.lower() == session_check_code.lower():
            if (password == repassword):
                UserInfo.objects.get_or_create(userId='userId',
                                               defaults={'password': password, 'username': username, 'L_team': L_team})
            else:
                error_msg = "两次输入的密码不一致"
                return render_to_response('register.html', {'error_msg': error_msg})
    return HttpResponseRedirect('../templates/login/')



def login(request):
    error_msg = ""
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        post_check_code = request.POST.get('check_code')   #人类验证
        session_check_code = request.session['check_code']
        if post_check_code.lower() == session_check_code.lower():
            userId = request.POST.get('gonghao')
            password = request.POST.get('pass')
            user = auth.authenticate(userId=userId, password=password)  # 去auth_user表中查数据（默认）不知道username是不是必填项
            if user:
                auth.login(request, user)  # 设置session
                response = HttpResponseRedirect('../templates/mainpage/')
                response.set_cookie('userId', userId, 3600)  # 设置cookie
                return response
            else:
                error_msg = '用户名或密码错误'
                return render_to_response('login.html', {'error_msg': error_msg})  # data还未在前端设置


def dglogout(request):
    if request.method == 'GET':
        auth.logout(request)
        response = HttpResponse('退出成功')
        response.delete_cookie('username')
        return response
    return HttpResponseRedirect('../templates/login/')

@login_required
def change_pwd(request):
    error_msg=""
    if request.method == 'POST':
        userId=request.COOKIES["userId"]
        password = request.POST.get('nowpass')
        obj = models.UserInfo.objects.get(userId=userId)
        pas = obj.password
        if (pas == password):
            passw = request.POST.get('pass')
            repassw = request.POST.get('repass')
            if(passw == repassw):
                obj.update(password=passw)
            else:
                error_msg = "两次输入的密码不一致！"
                return render_to_response('set.html', {'error_msg': error_msg})  #应该加一个弹窗
        else:
            error_msg = "密码不正确"
            return render_to_response('set.html', {'error_msg': error_msg})
    else:
        return render(request,'login.html')


def create_code_img(request):
    f = BytesIO()  # 直接在内存开辟一点空间存放临时生成的图片
    img, code = check_code.create_validate_code()  # 调用check_code生成照片和验证码
    request.session['check_code'] = code  # 将验证码存在服务器的session中，用于校验
    img.save(f, 'PNG')  # 生成的图片放置于开辟的内存中
    return HttpResponse(f.getvalue())  # 将内存的数据读取出来，并以HttpResponse返回

@login_required
def addblog(request):
    if request.method == 'GET':
        return render(request, 'addblog.html')


def blogindex(request):
    value = request.COOKIES["userId"]
    if(value.isdigit()):     #判断cookie是否全为数字
        post_list = Post.objects.filter(author_userId=value)
        return render(request, 'blogindex.html', context={'post_list': post_list})
    else:
        return render(request,'login.html')



class IndexView(ListView):
    model = Post
    template_name = 'blogindex.html'
    context_object_name = 'post_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        """
        在视图函数中将模板变量传递给模板是通过给 render 函数的 context 参数传递一个字典实现的，
        例如 render(request, 'blog/index.html', context={'post_list': post_list})，
        这里传递了一个 {'post_list': post_list} 字典给模板。
        在类视图中，这个需要传递的模板变量字典是通过 get_context_data 获得的，
        所以我们复写该方法，以便我们能够自己再插入一些我们自定义的模板变量进去。
        """

        # 首先获得父类生成的传递给模板的字典。
        context = super(IndexView, self).get_context_data(**kwargs)
