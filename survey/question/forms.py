from django import formsfrom .models import Consumer, Survey, Question, Choiceclass ConsumerForm(forms.ModelForm):    class Meta:        model = Consumer        fields = ['name']class SurveyForm(forms.ModelForm):    class Meta:        model = Survey        fields = ['name', 'owner']class QuestionForm(forms.ModelForm):    class Meta:        model = Question        fields = ['question_text']class ChoiceForm(forms.ModelForm):    class Meta:        model = Choice        fields = ['choice_text', 'selected', 'question']