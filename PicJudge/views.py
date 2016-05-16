from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.

def home(request):
    IMG_list = os.listdir(os.path.abspath('.')+"/PicJudge/www.mzitu.com/")
    return render(request,'index.html',{'IMG_list':IMG_list})
