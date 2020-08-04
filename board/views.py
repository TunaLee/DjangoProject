from django.shortcuts import render , redirect
from .models import Board
from .forms import BoardForm
from fcuser.models import Fcuser
# Create your views here.


def board_write(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid(): # 유효한 게시글이 입력이 되면 게시글 제목과 내용과 작성자 정보를 저장하는 역할을 하는 것

            user_id = request.session.get('user') # 로그인 된 세션의 사용자 명을 받아옴
            fcuser = Fcuser.objects.get(pk=user_id) # 아이디와 같은 키값의 유저정보를 get

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()

            return redirect('/board/list/')
    else:
        form = BoardForm()

    return render(request,'board_write.html',{'form':form})


def board_list(request):
    boards = Board.objects.all().order_by('-id') 
    return render(request, 'board_list.html',{'boards':boards}) # 템플릿에 전달