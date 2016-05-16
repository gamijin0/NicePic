from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.

def home(request):
    IMG_list = os.listdir("/home/ftp/MyPic")
    return render(request,'index.html',{'IMG_list':IMG_list})
