from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from django.http import HttpResponse
from .forms import LoginForm
# Create your views here.

def home(request):
    user_id = request.session.get('user')

    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id) # Fcuser 아이디 목록에서 저장 돼 있는 키중에 user_id와 같은 걸 찾아냄
        return HttpResponse(fcuser.username) # 로그인하면 아이디를 띄움

    return HttpResponse('Home!') #로그인 되어 있지 않으면 Home!를 띄움

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid(): # 유효한 값이 들어오면 홈으로 return
            request.session['user'] = form.user_id # 로그인이 됐을 때 세션에 넣기 위한 함수 request를 사용하여 user 키에 form로 부터 입력한 id 정보를 넣음, 세션생성
            return redirect('/')
    else:
        form = LoginForm()

    return render(request,'login.html',{'form':form})



def register(request): # 등록하기 또는 불러오기를 통한 접근방법 두가지

    if request.method =='GET': # url을 통해 들어온 경우
        return render(request,'register.html')
    elif request.method == 'POST': # 등록한 다음 다시 돌아오는 경우
        username = request.POST.get('username',None) # 기본 조건으로 None로 넣음 ( 공백으로 입력됐을 때를 대비해서 ) 즉, None 또는 username로 받아지는 것
        password = request.POST.get('password',None)
        useremail = request.POST.get('useremail',None)
        re_password = request.POST.get('re-password',None)


        res_data = {}
        if not(username):
            res_data['error'] = '아이디를 입력하세요.'
        elif not(useremail):
            res_data['error'] = '이메일을 입력하세요'
        elif not(password):
            res_data['error'] = '비밀번호를 입력하세요.'
        elif not(re_password):
            res_data['error'] = '비밀번호 확인을 입력하세요'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.' # error 라는 키에 저장

        else:
            fcuser = Fcuser(
                username = username,
                useremail = useremail,
                password = make_password(password)
            )

            fcuser.save() # 모델에 저장

        return render(request,'register.html', res_data) # html 코드에 res_data로 보냄