from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def hi(request):
    print('1.',type(request))
    print('2.',request)
    if request.method == 'GET':
        return JsonResponse({'method':'GET'})
    elif request.method == 'POST':
        return JsonResponse({'method':'POST'})
    return JsonResponse({'method':'others'})

def home(request):
    return render(request,'payload.html')