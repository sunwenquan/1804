from django.db import models


class Consumer(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Survey(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(to=Consumer, to_field='id',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    survey = models.ForeignKey(to=Survey,to_field='id',on_delete=models.CASCADE)


    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    selected = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text

class Answer(models.Model):
    content = models.CharField(max_length=500)
    owner = models.CharField(max_length=50)
    survey = models.ForeignKey(Survey,on_delete=models.CASCADE)

