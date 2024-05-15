from django.shortcuts import render
from django.http import HttpResponse, FileResponse

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.
def cartel(request):
    return FileResponse(open(BASE_DIR / "files/cartel_jojo.jpg"))