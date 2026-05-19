from django.shortcuts import render
from .models import Bug

def bug_list(request):
  bugs=Bug.objects.filter(status='Open').order_by('created_at')
  return render(request, 'bugs/bugs_list.html'. {'bugs': bugs})

# Create your views here.
