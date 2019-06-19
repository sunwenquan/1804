from django.contrib import admin
from question.models import Consumer,Question,Choice,Survey

admin.site.register(Consumer)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Survey)

