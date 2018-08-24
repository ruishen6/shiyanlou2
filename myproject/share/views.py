from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from .models import Upload

from django.http import HttpResponsePermanentRedirect

import random
import string
import datetime

class HomeView(View):
    def get(self,request):
        return render(request,'base.html',{})

    def post(self,request):
        if request.FILES:
            file = request.FILES.get("file")
            name = file.name
            size = int(file.size)
            with open('static/file/'+name,'wb') as f:
                f.write(file.read())
            code = ''.join(random.sample(string.digits,8))
            u = Upload(
                path = 'static/file/'+name,
                name = name,
                Filesize = size,
                code = code,
		PCIP = str(request.META['REMOTE_ADDR']),
            )
            u.save()
            return HttpResponseRermanentRedirect('/s/'+code)

class DisplayView(View):
    def get(self,request,code):
        u = Upload.objects.filter(code=str(code))
        if u:
            for i in u:
                i.DownloadDocount +=1
                i.save()
        return render(request,'content.html',{"content":u})
