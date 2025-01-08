from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def ipo_info(request):
    ipo_info = requests.get("http://127.0.0.1:8000/api/ipo_info").json()
    return render(request, 'ipo_info.html', {'ipo_info': ipo_info})