from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
  return render(request, 'account/login.html')