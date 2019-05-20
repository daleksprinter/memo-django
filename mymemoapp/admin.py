from django.contrib import admin
from mymemoapp.models import Memo
from mymemoapp.models import User
# Register your models here.

admin.site.register(Memo)
admin.site.register(User)