from django.shortcuts import render
from django.http.response import HttpResponse
from django.core.files.storage import FileSystemStorage


# Create your views here.
from django.http import HttpResponse
from app.forms import *
def imageData(request):
    form=imageForm()
    if request.method=='POST' and request.FILES:
        form_data=imageForm(request.POST,request.FILES)
        if form_data.is_valid():
            img=form_data.cleaned_data['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
            image_url=fs.url(file)
            return render(request,'image_display.html',context={'image_url':image_url})
            


    return render(request,'image.html',context={'form':form})