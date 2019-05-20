from django.shortcuts import render
from django.http import HttpResponse
from mymemoapp.models import Memo, User

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
