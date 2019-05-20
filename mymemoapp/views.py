from django.shortcuts import render
from django.http import HttpResponse
from mymemoapp.models import Memo

def index(request):
    memos = Memo.objects.all()
    return render(request, 'index.html', {"memos" : memos})
