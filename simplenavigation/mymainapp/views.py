from django.shortcuts import render

from datetime import datetime


# Create your views here.
def wherenext(request):
    today = datetime.today()

    if today.weekday() in [0, 1, 2, 3, 4]:
        return render(request, 'mymainapp/weekday.html')
    else:
        return render(request, 'mymainapp/weekend.html')