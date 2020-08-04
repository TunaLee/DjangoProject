from django import forms
class BoardForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요.' #required에 있는 함수에 에러를 띄움
        },
        max_length=128, label="제목")
    contents = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요'
        },
        widget=forms.Textarea , label="내용")
