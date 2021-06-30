from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'genarator\home.html')

def about(request):
    return render(request,'genarator\about.html')

def password(request):
    thepassword = "testing"

    Characters = list('abcdefghigklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        Characters.extend(list('ABCDEFGHIGKLMNOPQRSTUVWXYZ'))

    if request.GET.get('number'):
        Characters.extend(list('1234567890'))

    if request.GET.get('special'):
        Characters.extend(list(('()!@#$%^&')))


    lenght = int(request.GET.get('lenght',12))

    thepassword = ''

    for i in range(lenght):
        thepassword +=random.choice(Characters)

    return render(request,'genarator\password.html',{'password':thepassword})
