from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from .models import Upload

class HomeView(View):
    def get(self,request):
        return render(request,'base.html',{})

class DisplayView(View):
    def get(self,request,code):
        u = Upload.objects.filter(code=str(code))
        if u:
            for i in u:
                i.DownloadDocount +=1
                i.save()
        return render(request,'content.html',{"content":u})
