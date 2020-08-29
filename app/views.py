from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Record
import datetime


def index(request):
    return render(request, 'app/index.html')


def form(request):
    if request.method == 'POST':
        record = Record()
        record.ownerName = request.POST.get('name')
        record.ownerSurname = request.POST.get('surname')
        record.description = request.POST.get('description')
        record.address = request.POST.get('address')
        record.phone = request.POST.get('phone')
        record.model = request.POST.get('model')
        record.brand = request.POST.get('brand')
        record.deviceType = request.POST.get('type')
        record.time = datetime.datetime.now()
        record.save()
        return render(request, 'app/form.html')
    else:
        return render(request, 'app/form.html')


def statusForm(request):
    if request.method == 'POST':
        try:
            record = {
                'record': Record.objects.get(id=request.POST.get('name'))}
            return render(request, 'app/statusForm.html', record)
        except:
            pass
    return render(request, 'app/statusForm.html')
