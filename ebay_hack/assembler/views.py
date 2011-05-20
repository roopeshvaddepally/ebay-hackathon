from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    print request.GET
    return render_to_response("assembler/index.html", {"p": request.GET})