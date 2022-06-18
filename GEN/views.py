from django.shortcuts import render
#from django.http import HttpResponse
import random 

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def psw(request):

    caracteres = list('abcdefghijklmnopqrstuvwxyz1234567890')
    psw_gen = ''

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        caracteres.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        caracteres.extend(list('*+-_?/%$'))

    if request.GET.get('numbers'):
        caracteres.extend(list('1234567890'))
    

    for x in range(length):
        psw_gen += random.choice(caracteres)


    return render(request, 'psw.html', {'psw': psw_gen})
