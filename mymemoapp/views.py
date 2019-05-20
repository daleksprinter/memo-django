from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from mymemoapp.models import Memo, User
from django.urls import reverse

def index(request):
    if request.method == 'POST':
        txt = request.POST['text']
        usr = User.objects.get(username = 'root')
        memo = Memo.objects.create(author = usr, text = txt)
        memo.save()

    memos = Memo.objects.all()
    return render(request, 'index.html', {"memos" : memos})

def detail(request, id):
    
    memo = Memo.objects.get(id = id)
    
    return render(request, 'detail.html', {"memo" : memo})

def delete(request, id):
    Memo.objects.get(id = id).delete()
    return HttpResponseRedirect(reverse('index'))