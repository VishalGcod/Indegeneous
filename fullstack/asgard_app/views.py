from django.http import HttpResponse
from django.shortcuts import render
from .models import Asgard_Data
# Create your views here.


def index(request):
    data = Asgard_Data.objects.all()
    return render(request, "index.html", {
        "data": data
    })


def show_data(request):
    if request.method == "GET":
        data_id = request.GET['data_id']
        data = Asgard_Data.objects.get(pk=data_id)
        print(data)
        return HttpResponse(data.text)
    else:
        return HttpResponse("Invalid Method")