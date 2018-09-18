from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
# Create your views here.
from main.models import User, Admin, Jiaxun, IMG
import json
from django.core import serializers
from hashlib import sha1
from django.forms.models import model_to_dict


@csrf_exempt
def index(request):
    if request.method == 'POST':
        page_sum = request.POST.get('page')
        if page_sum and int(page_sum) != 0:
            i1 = (int(page_sum) - 2) * 3
            i2 = i1 + 3
            ac = User.objects.all()[i1:i2]
            data = serializers.serialize("json", ac)
            print(data)
            return HttpResponse(data)
        else:
            return HttpResponse('no')
    count = User.objects.all().count() / 3
    dd = int(count) + 1
    pp = User.objects.all()[0:dd]
    sum = User.objects.all()
    return render(request, 'index.html', locals())


@csrf_exempt
def get_num(request):
    a = 'bucuo'
    users = User.objects.all()
    set_list1 = []
    set_list2 = []
    set_list3 = []
    set_list4 = []
    set_list5 = []
    set_list6 = []
    for i in users:
        father_Detail = User.objects.filter(father_id=i.father_id)[0]
        if i.id % 3 == 0:
            set_list3.append({'id': i.id, 'name': i.name, 'father': i.father_id, 'sex': i.sex, 'content': i.content,
                              'shi': i.generation, 'line': i.line})
        elif i.id % 2 == 0:
            set_list2.append({'id': i.id, 'name': i.name, 'father': i.father_id, 'sex': i.sex, 'content': i.content,
                              'shi': i.generation, 'line': i.line})
        else:
            set_list1.append({'id': i.id, 'name': i.name, 'father': i.father_id, 'sex': i.sex, 'content': i.content,
                              'shi': i.generation, 'line': i.line})
    back_list = []
    for i in range(int(len(users)/6)):
        if i <= len(set_list2):
            bool = True
            if i % 2 == 0:
                bool = False
            # print(set_list1[i],set_list2[i], set_list3[i], set_list4[i], set_list5[i], set_list6[i])
            back_list.append({'data': [set_list1[i], set_list2[i], set_list3[i]], 'show': bool})
    jiaxuns = Jiaxun.objects.all()
    imgs = IMG.objects.all()
    return render(request, 'test1.html', locals())


@csrf_exempt
def new_page(request):
    if request.method == 'POST':
        raise 'sorry'
    objs = User.objects.all()
    user_list = list()
    re_list = []

    for i in objs:
        father_detail = User.objects.filter(father_id=i.father_id)[0]
        user_list.append({'id': i.id, 'name': i.name, 'father': i.father_id, 'sex': i.sex, 'content': i.content,
                              'shi': i.generation, 'line': i.line, 'line_str': i.line_str, 'girl': i.girl_num, 'son': i.son_num,
                          'house': i.house, 'father_son': father_detail.son_num, 'father_girl': father_detail.girl_num,
                          'father_house': father_detail.house})
    for i in range(len(user_list)-1):
        fool = False

        if i >= 0 and str(user_list[i]['father']) == str(user_list[i-1]['father']):
            fool = True
        re_list.append({'id': user_list[i]['id'], 'name': user_list[i]['name'], 'father': user_list[i]['father'], 'sex':
            user_list[i]['sex'], 'content': user_list[i]['content'],
                              'shi': user_list[i]['shi'], 'line': user_list[i]['line'], 'line_str': user_list[i]['line_str'],
                        'girl': user_list[i]['girl'], 'son': user_list[i]['son'],
                          'house': user_list[i]['house'], 'fool': fool, 'father_son': user_list[i]['father_son'], 'father_girl': user_list[i]['father_girl'],
                          'father_house': user_list[i]['father_house']})

    # for i in re_list:
    #     print(i)
    return render(request, 'new.html', locals())


@csrf_exempt
def get_right(request):
    if request.method == 'POST':
        page_sum = request.POST.get('page')
        if page_sum and int(page_sum) >= 0:
            i1 = (int(page_sum) - 2) * 3
            i2 = i1 + 3
            ac = User.objects.all()[i1:i2]
            data = serializers.serialize("json", ac)
            return HttpResponse(data)
        else:
            return HttpResponse('no')


@csrf_exempt
def home(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        userlife = request.POST.get('shu')
        userline = request.POST.get('hang')
        usersex = request.POST.get('sex')
        userfather = request.POST.get('ufather')
        userdesc = request.POST.get('ucontent')
        if username:
            if userlife:
                if userline:
                    if usersex:
                        if userfather:
                            if userdesc:
                                print('okokoko')
                            else:
                                return HttpResponse('no userdesc')
                        return HttpResponse('no userfather')
                    return HttpResponse('no usersex')
                return HttpResponse('no userline')
            return HttpResponse
        return HttpResponse('no username')
    return render(request, 'home.html')


@csrf_exempt
def user(request):
    obj = User.objects.all()
    sum_count = obj.count()
    print(sum_count)
    return render(request, 'user.html', locals())


@csrf_exempt
def login(request):
    return render(request, 'login.html')


@csrf_exempt
def register(request):
    username = request.POST.get('name')
    userpwd = request.POST.get('pwd')
    # 判断用户名是否重复
    try:
        users = Admin.objects.filter(name=username)
        if users:
            return HttpResponse('double')
        else:
            s1 = sha1()
            s1.update(userpwd.encode("utf8"))
            upwd2 = s1.hexdigest()
            user = Admin()
            user.name = username
            user.password = upwd2
            user.save()
            return HttpResponse('ok')
    except Exception as e:
        print(e)
        return HttpResponse('error')


@csrf_exempt
def relogin(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        userpwd = request.POST.get('pwd')
        try:
            users_name = Admin.objects.filter(name=username)
        except Exception as e:
            print(e)
        if users_name:
            s1 = sha1()
            s1.update(userpwd.encode("utf8"))
            if s1.hexdigest() == users_name[0].password:
                return HttpResponse('ok')
            else:
                return HttpResponse('nouser')
        else:
            return HttpResponse('failed')


@csrf_exempt
def submit(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        userlife = request.POST.get('shu')
        userline = request.POST.get('hang')
        usersex = request.POST.get('sex')
        userfather = request.POST.get('father')
        userdesc = request.POST.get('content')
        if username:
            if userlife:
                if userline:
                    if usersex:
                        if userfather:
                            if userdesc:
                                 user = User()
                                 user.name = username
                                 user.generation = userlife
                                 user.line = userline
                                 user.sex = usersex
                                 user.content = userdesc
                                 user.father_id = userfather
                                 user.save()
                                 return  HttpResponse('ok')
                            else:
                                return HttpResponse('no userdesc')
                        return HttpResponse('no userfather')
                    return HttpResponse('no usersex')
                return HttpResponse('no userline')
            return HttpResponse('no userlife')
        return HttpResponse('no username')


# 向上搜索五代
@csrf_exempt
def search(request):
    if request.method == "POST":
        son = request.POST.get('son')
        father = request.POST.get('father')
        print(son, father)
        name_list = []
        if son:
            if father:
                obj = User.objects.filter(name=son, father_id=father)
                if obj:
                    name_list.append({'name': '一代', 'detail': son})
                    obj1 = User.objects.filter(father_id=father)
                    if obj1:
                        for i in obj1:
                            name_list.append({'name': '二代', 'detail': i.father_id})
                            obj2 = User.objects.filter(name=i.father_id)
                            print(name_list, type(name_list))
                            if obj2:
                                for j in obj2:
                                    name_list.append({'name': '三代', 'detail': j.father_id})
                                    obj3 = User.objects.filter(name=j.father_id)
                                    if obj3:
                                        for k in obj3:
                                            name_list.append({'name': '四代', 'detail': k.father_id})
                                            obj4 = User.objects.filter(name=k.father_id)
                                            for p in obj4:
                                                name_list.append({'name': '五代', 'detail': p.father_id})
                                                return HttpResponse(json.dumps(name_list),
                                                                    content_type="application/json")
                                    else:
                                        return HttpResponse(json.dumps(name_list), content_type="application/json")

                            else:
                                return HttpResponse(json.dumps(name_list), content_type="application/json")
                    else:
                        return HttpResponse(json.dumps(name_list), content_type="application/json")
                else:
                    return HttpResponse('no user')
            else:
                return HttpResponse('no father')
        else:
            return HttpResponse('no son')