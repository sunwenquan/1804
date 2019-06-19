from django.shortcuts import render
from django.views import View
import json

from .models import Consumer, Survey, Question, Choice,Answer
from .forms import ConsumerForm, SurveyForm, QuestionForm, ChoiceForm

class SurveyListView(View):
    def get(self,request,survey_id):
        print("get请求")
        survey = Survey.objects.get(pk=survey_id)
        questions = survey.question_set.all() # 某个问卷里的所有问题
        context = {
            'survey':survey,
            'questions':questions
        }
        return render(request,template_name='question/survey_detail.html',
                      context=context)

    def post(self,request):
        print('post请求')
        print(request.POST)
        anwser = Answer()
        anwser.owner = "gavinsun"
        data = json.dumps(request.POST)
        print(json.loads(data))
        anwser.content = json.dumps(request.POST)
        anwser.survey_id = request.POST.get('survey_id')
        anwser.save()
        anwser = Answer.objects.get(pk=6)
        print(anwser.content)
        r = json.loads(anwser.content)
        print(type(r))
        return render(request,template_name='question/survey_detail.html')





