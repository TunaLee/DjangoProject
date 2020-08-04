from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=128,verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('fcuser.Fcuser', verbose_name='작성자',on_delete=models.CASCADE,) # 사용자가 삭제 되면 같이 삭제한다(CASCADE)
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')



    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fastcampus_board'
        verbose_name = '패스트캠퍼스 게시글'
        verbose_name_plural = '패스트캠퍼스 게시글'