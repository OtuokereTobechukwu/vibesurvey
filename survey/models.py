from django.db import models

# Create your models here.


class createQuestion(models.Model):
    title = models.CharField(max_length=50, default='Question')
    question_text = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    file_upload = models.FileField()

    def __str__(self):
        return self.title


class reponses(models.Model):
    question = models.ForeignKey(createQuestion, on_delete=models.CASCADE)
    response_text = models.CharField(max_length=200)


    def __str__(self):
        return self.question