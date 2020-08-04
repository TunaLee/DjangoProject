from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password
class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요' #required에 있는 함수에 에러를 띄움
        },
        max_length=32, label="사용자 이름")
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput , label="비밀번호")

    def clean(self):
        cleaned_data = super().clean() # 값이 들어있지 않으면 여기서 실패처리를 먼저함
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password: # 유저네임과 비밀번호를 받았으면
            fcuser = Fcuser.objects.get(username = username) # 받아온 이름과 같은 정보를 fcuser에 받아오고
            if not check_password(password,fcuser.password): # 입력한 비밀번호와 fcuser에 담은 비밀번호가 같지않으면 에러메시지
                self.add_error('password','비밀번호가 틀렸습니다')

            else:
                self.user_id = fcuser.id # 로그인이 됐을 때 세션을 사용하기 위해 저장
