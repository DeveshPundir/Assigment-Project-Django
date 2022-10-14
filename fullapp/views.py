from django.shortcuts import render
from .models import data
def index(request):
    data_all=data.objects.all()
    print(len(data_all))
   
    print(data_all[0].snippet)
    print(data_all[1].snippet)
    print(data_all[2].snippet)
    print(data_all[3].snippet)
    return render(request,'index.html',{'geo':data_all[0].snippet,'his':data_all[1].snippet,'cul':data_all[2].snippet,'lan':data_all[3].snippet})
# Create your views here.
