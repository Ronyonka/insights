from django.shortcuts import render

def do_this(request):
    return render(request, 'index.html')
