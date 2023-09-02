from django.shortcuts import render
from django.http import HttpResponse
from playground.forms import Login

def login(request):
  form = Login()
  if request.method == "POST":
    print(request.POST)
    archivo = open("archivo.txt","w")
    data = request.POST
    archivo.write(str((data)))
    archivo.close()
  return render(request,
            'hello.html',
            {'form': form})