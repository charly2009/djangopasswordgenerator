from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    
    characters = list('abcdefghijklmnopqrstvwxyz')

    #to ask user if he wants uppercase, SO IT WILL ADD THEM TO CHARACTERS 
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) 

    if request.GET.get('special'):
        characters.extend(list('#$!%^&*())_+@')) 

    if request.GET.get('number'):
        characters.extend(list('0123646789')) 



    length= int(request.GET.get('length',16))# questo dato length viene dalla pagina home.html select, il 16 e lunghezza per default
    
    
    thepassword =''
    for password in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})

