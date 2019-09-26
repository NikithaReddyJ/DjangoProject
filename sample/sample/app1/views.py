from django.shortcuts import render
from .models import table,table1,table2
from django.http import HttpResponseRedirect
# Create your views here.
def app1view(request):
    return render(request, 'land.html')
def dashboardview(request):
    return render(request, 'dashboard.html')
def Tview(request):
    c=table1.objects.all()
    e=table2.objects.all()
    return render(request, 'T.html')
def newframeview(request):
    a=table.objects.all()
    return render(request, 'newframe.html',{'alldata':a})
def userprofileview(request):
    return render(request, 'userprofile.html')
def ftableview(request):
    b=table.objects.all()
    return render(request, 'table.html',{'alldata':b})
def ftable1view(request):
    d=table1.objects.all()
    return render(request, 'table1.html',{'data':d})
def ftable2view(request):
    f=table2.objects.all()
    return render(request, 'table2.html',{'data':f})
def deleteview(request,k_id):
    d=table1.objects.get(id = k_id)
    x=table1.objects.all()
    d.delete()
    return render(request, 'table1.html',{'data':x})
