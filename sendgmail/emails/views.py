from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
import datetime

# Create your views here.

def emailList(request):
    return render(request, 'emails/list.html')

