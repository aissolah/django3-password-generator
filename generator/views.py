from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
  return render(request, 'generator/home.html')

def password(request):
  password=''
  numbers = list('1234567890')
  capitals = list('acdefghijklmnopqrstuvwxyz'.upper())
  special_chars = list('@!$_-%&([)]=?*+'.upper())
  
  my_list=list('acdefghijklmnopqrstuvwxyz')

  length = int(request.GET.get('length'))
  is_uppercase = request.GET.get('uppercase')
  is_numbers = request.GET.get('numbers')
  is_specialchars = request.GET.get('specialchars')
  
  if is_uppercase : 
    my_list.extend(capitals)

  if is_numbers : 
    my_list.extend(numbers)

  if is_specialchars:
    my_list.extend(special_chars)

  for x in range(length):
    password += random.choice(my_list)

  return render(request, 'generator/password.html', {'password':password})


def about(request):
  return render(request, 'generator/about.html')

